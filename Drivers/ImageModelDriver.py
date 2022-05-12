from Models.SPDImage import *
from Analyze.AnalyzeModel import *
from PIL import Image
from Analyze.Filters import *
from Drivers.HistogramModelDriver import *

import numpy as np
import numba
import random
import cv2
from scipy import misc,ndimage
from ctypes import *


class ImageModelDriver:

    # -------------------------------
    # Лекция 1
    # -------------------------------

    @staticmethod
    def multi_shift(data: SPDImage, c):
        result_array = []

        for row in data.modified_image:
            y_array = [y * c for y in row]
            result_array.append(y_array)

        data.update(np.array(result_array), '_multi_shift')

    @staticmethod
    def add_shift(data: SPDImage, c):
        result_array = []

        for row in data.modified_image:
            y_array = [y + c for y in row]
            result_array.append(y_array)

        data.update(np.array(result_array), '_add_shift')

    @staticmethod
    def grayscale(data: SPDImage, dtype=np.uint8):
        max_a = np.max(data.modified_image)
        min_a = np.min(data.modified_image)
        diff_a = max_a - min_a
        result_array = []

        for row in data.modified_image:
            y_array = [(y - min_a) * np.iinfo(dtype).max / diff_a for y in row]
            result_array.append(y_array)

        data.update(np.array(result_array), '_grayscale')

    # -------------------------------
    # Лекция 2
    # -------------------------------

    @staticmethod
    def rotate90(data: SPDImage):
        data.update(np.rot90(data.modified_image), '_rotated')

    @staticmethod
    def resize(data: SPDImage, resample: int, scale_const: float, dtype=np.uint8):
        resize_height = int(data.modified_image.shape[0] * scale_const)
        resize_width = int(data.modified_image.shape[1] * scale_const)

        image_from_array = Image.fromarray(data.modified_image.astype(dtype))
        resized_image = image_from_array.resize((resize_width, resize_height), resample)

        if resample == Image.NEAREST:
            resample_type_text = "nearest"
        elif resample == Image.BOX:
            resample_type_text = "box"
        elif resample == Image.BILINEAR:
            resample_type_text = "bilinear"
        else:
            resample_type_text = str(resample)

        data.update(np.array(resized_image, copy=True), '_resized_' + resample_type_text)

    # -------------------------------
    # Лекция 3
    # -------------------------------

    @staticmethod
    def negative(data: SPDImage):
        max_a = np.max(data.modified_image)
        result_array = []

        for row in data.modified_image:
            y_array = [max_a - 1 - y for y in row]
            result_array.append(y_array)

        data.update(np.array(result_array), '_negative')

    @staticmethod
    def gamma_correction(data: SPDImage, const, gamma):
        result_array = []

        for row in data.modified_image:
            y_array = np.array([const * (np.power(y, gamma)) for y in row])
            result_array.append(y_array)

        data.update(np.array(result_array), '_gamma_correction')

    # Делаем изображение более контрастным при увеличении const
    # Делаем изображение менее констрастным при уменьшении const
    @staticmethod
    def log_correction(data: SPDImage, const):
        result_array = []

        for row in data.modified_image:
            y_array = [const * (np.log(y + 1)) for y in row]
            result_array.append(y_array)

        data.update(np.array(result_array), '_log_correction')

    # -------------------------------
    # Лекция 5
    # -------------------------------

    @staticmethod
    @numba.jit(nopython=True)
    def convolution(main_data: np.ndarray, add_data: np.ndarray, dt: float):
        x_array = []
        y_array = []

        for i in range(len(main_data) + len(add_data)):
            sum = 0

            for j in range(len(add_data)):
                if 0 <= (i - j) < len(main_data):
                    sum += main_data[i - j] * add_data[j]
                else:
                    sum += 0

            if (len(add_data) / 2) <= i < (len(main_data) + len(add_data) / 2):
                y_array.append(sum)
                x_array.append((i - len(add_data) / 2) * dt)

        return [x_array, y_array]

    @staticmethod
    def find_moire_for_image(image: SPDImage, m, quantile=0.7, dt=1):
        diff_im = []
        for row_idx in range(0, len(image.modified_image), m):
            row = image.modified_image[row_idx]
            diff_im.append(AnalyzeModel.diff(row))

        max_auto_freq = []
        for diff in diff_im:
            auto = AnalyzeModel.auto_corr_array(diff)
            auto_fourier = AnalyzeModel.amplitude(auto, dt)
            max_auto_fourier_freq_idx = np.argmax(auto_fourier[1])
            max_auto_fourier_freq = auto_fourier[0][max_auto_fourier_freq_idx] // 0.01 * 0.01
            max_auto_freq.append(max_auto_fourier_freq)

        max_mutal_freq = []
        for row_idx in range(0, len(diff_im)):
            row_f = diff_im[row_idx]
            row_s = diff_im[(row_idx + 1) % len(diff_im)]
            mutal = AnalyzeModel.mutual_corr_array(row_f, row_s)
            mutal_fourier = AnalyzeModel.amplitude(mutal, dt)
            max_mutal_fourier_freq_idx = np.argmax(mutal_fourier[1])
            max_mutal_fourier_freq = mutal_fourier[0][max_mutal_fourier_freq_idx] // 0.01 * 0.01
            max_mutal_freq.append(max_mutal_fourier_freq)

        all_freqs = max_auto_freq + max_mutal_freq
        freqs_counts = {}

        for freq in all_freqs:
            if freq in freqs_counts:
                freqs_counts[freq] += 1
            else:
                freqs_counts[freq] = 1

        result_freqs = []

        for key in freqs_counts:
            if (freqs_counts[key] / len(all_freqs)) >= quantile:
                result_freqs.append(key)

        return result_freqs

    @staticmethod
    def fix_moire_for_image(
            image: SPDImage,
            result_freqs,
            apply_vertical_fix,
            shift,
            m
    ) -> bool:
        if len(result_freqs) == 0:
            print('Не нашлась решетка на изображении!')
            return False

        first_top_freq = result_freqs[0]
        filter = Filters.bsw_filter(first_top_freq - shift, first_top_freq + shift, 1, m)[1]

        print('Работаем с частотой: ' + str(first_top_freq))

        result = []
        for row in image.modified_image:
            conv = ImageModelDriver.convolution(np.array(row), np.array(filter), 1)[1]
            result.append(conv)

        if apply_vertical_fix:
            rotated = np.rot90(result)
            result = []
            for row in rotated:
                conv = ImageModelDriver.convolution(np.array(row), np.array(filter), 1)[1]
                result.append(conv)
            image.update(np.rot90(result, k=3), '_fixed')
        else:
            image.update(result, '_fixed')

        print('Изображение ' + image.name + ' исправлено!\n')

        return True

    # -------------------------------
    # Лекция 6
    # -------------------------------

    @staticmethod
    def salt_pepper(image: SPDImage, dots_count: int):
        final_image = []

        for row in image.modified_image:
            result = ImageModelDriver.salt_pepper_per_line(row, dots_count)
            final_image.append(result)

        image.update(final_image, '_salt_and_pepper')

    @staticmethod
    @numba.jit(nopython=True)
    def salt_pepper_per_line(image_data: np.ndarray, dots_count: int) -> np.ndarray:
        result_row = []

        for item in image_data:
            possibility = random.randint(0, 1000)

            if possibility < dots_count:
                result_row.append(0)
            elif 300 < possibility < (300 + dots_count):
                result_row.append(255)
            else:
                result_row.append(item)

        return np.array(result_row)

    @staticmethod
    def random_noize(image: SPDImage, intensity: int):
        final_image = []

        for row in image.modified_image:
            result = ImageModelDriver.random_noize_per_line(row, intensity)
            final_image.append(result)

        image.update(final_image, '_random_noize')

    @staticmethod
    @numba.jit(nopython=True)
    def random_noize_per_line(image_data: np.ndarray, intensity: int) -> np.ndarray:
        result_row = []

        for item in image_data:
            noize = random.randint(0, intensity)
            sign = random.randint(0, 1000)

            if sign > 500:
                result_row.append((item + noize) % 255)
            else:
                result_row.append((item - noize) % 255)
        return np.array(result_row)

    @staticmethod
    def linear_filter(image_sd: SPDImage, kernel_count: int):
        image = image_sd.modified_image
        kernel = np.ones([kernel_count, kernel_count], dtype=int)

        image_row, image_col = image.shape
        kernel_row, kernel_col = kernel.shape

        output = np.zeros(image.shape)

        pad_height = int((kernel_row - 1) / 2)
        pad_width = int((kernel_col - 1) / 2)

        padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))

        padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = image

        for row in range(image_row):
            for col in range(image_col):
                output[row, col] = np.mean(kernel * padded_image[row:row + kernel_row, col:col + kernel_col])

        processed_image = np.array(output)

        image_sd.update(processed_image, '_linear_filter')

    @staticmethod
    def median_filter(image_sd: SPDImage, kernel_count: int):
        image = image_sd.modified_image
        kernel = np.ones([kernel_count, kernel_count], dtype=int)

        image_row, image_col = image.shape
        kernel_row, kernel_col = kernel.shape

        output = np.zeros(image.shape)

        pad_height = int((kernel_row - 1) / 2)
        pad_width = int((kernel_col - 1) / 2)

        padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))

        padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = image

        for row in range(image_row):
            for col in range(image_col):
                output[row, col] = np.median(kernel * padded_image[row:row + kernel_row, col:col + kernel_col])

        processed_image = np.array(output)

        image_sd.update(processed_image, '_median_filter')

    # -------------------------------
    # Лекция 9
    # -------------------------------

    @staticmethod
    def blur_fix(image_sd: SPDImage, kernel: np.ndarray, alpha: float):
        kernel = np.pad(
            kernel, [
                (0, image_sd.modified_image.shape[0] - kernel.shape[0]),
                (0, image_sd.modified_image.shape[1] - kernel.shape[1])
            ]
        )

        kernel_f = AnalyzeModel.two_d_fourier(kernel, 1)
        image_sd_f = AnalyzeModel.two_d_fourier(image_sd.modified_image, 1)

        diff = (np.conj(kernel_f.complex_data) / (np.abs(kernel_f.complex_data) ** 2 + alpha * alpha)) * image_sd_f.complex_data
        diff_f = Fourier(diff, 1).two_d_back_transform()

        image_sd.modified_folder = image_sd.modified_folder + image_sd.name + '/'
        image_sd.update(diff_f, '_back_two_d_fourier')

        ImageModelDriver.grayscale(image_sd)

    # -------------------------------
    # Лекция 9
    # -------------------------------

    @staticmethod
    def high_pass_filter(image_sd: SPDImage, type: str, filter_radius):
        image_sd_f = AnalyzeModel.two_d_fourier(image_sd.modified_image, 1)
        img = np.fft.fftshift(image_sd_f.complex_data)

        height, weight = img.shape
        center_h = int(height / 2)
        center_w = int(weight / 2)

        if type == 'ideal':
            high_pass_filter = np.ones_like(img)

            for i in range(height):
                for j in range(weight):
                    dist_from_center = np.sqrt((i - center_h) ** 2 + (j - center_w) ** 2)
                    if dist_from_center < filter_radius:
                        high_pass_filter[i][j] = 0

        elif type == 'gausse':
            high_pass_filter = np.zeros_like(img)

            for i in range(height):
                for j in range(weight):
                    dist_from_center = np.sqrt((i - center_h) ** 2 + (j - center_w) ** 2)
                    high_pass_filter[i][j] = 1 - np.exp(-(dist_from_center ** 2) / (2 * filter_radius ** 2))
        else:
            return

        result_f = Fourier(np.fft.ifftshift(img * high_pass_filter), image_sd_f.dt)
        new_image = result_f.two_d_back_transform()

        image_sd.modified_folder = image_sd.modified_folder + '_hpf_' + type + '_' + str(filter_radius) + '/'
        image_sd.update(new_image, '_hpf_' + type)
        ImageModelDriver.grayscale(image_sd)

    @staticmethod
    def low_pass_filter(image_sd: SPDImage, type: str, filter_radius):
        image_sd_f = AnalyzeModel.two_d_fourier(image_sd.modified_image, 1)
        img = np.fft.fftshift(image_sd_f.complex_data)

        height, weight = img.shape
        center_h = int(height / 2)
        center_w = int(weight / 2)

        if type == 'ideal':
            low_pass_filter = np.zeros_like(img)

            for i in range(height):
                for j in range(weight):
                    dist_from_center = np.sqrt((i - center_h) ** 2 + (j - center_w) ** 2)
                    if dist_from_center < filter_radius:
                        low_pass_filter[i][j] = 1

        elif type == 'gausse':
            low_pass_filter = np.zeros_like(img)

            for i in range(height):
                for j in range(weight):
                    dist_from_center = np.sqrt((i - center_h) ** 2 + (j - center_w) ** 2)
                    low_pass_filter[i][j] = np.exp(-(dist_from_center ** 2) / (2 * filter_radius ** 2))
        else:
            return

        result_f = Fourier(np.fft.ifftshift(img * low_pass_filter), image_sd_f.dt)
        new_image = result_f.two_d_back_transform()

        image_sd.modified_folder = image_sd.modified_folder + '_lpf_' + type + '_' + str(filter_radius) + '/'
        image_sd.update(new_image, '_lpf_' + type)
        ImageModelDriver.grayscale(image_sd)

    @staticmethod
    def threshold(image_sd: SPDImage, threshold_const=127):
        image = image_sd.modified_image

        image[image > threshold_const] = np.iinfo(image_sd.dtype).max
        image[image != np.iinfo(image_sd.dtype).max] = np.iinfo(image_sd.dtype).min

        image_sd.update(image, '_threshold_' + str(threshold_const))

    # -------------------------------
    # Лекция 10
    # -------------------------------

    @staticmethod
    def simple_gradient(image_sd: SPDImage):
        mask_x = np.array([
            [-1, -1, -1], [0, 0, 0], [1, 1, 1],
        ])

        mask_y = np.array([
            [-1, 0, 1], [-1, 0, 1], [-1, 0, 1]
        ])

        processed_image_x = ImageModelDriver.convolution_2d(image_sd, mask_x)
        processed_image_y = ImageModelDriver.convolution_2d(image_sd, mask_y)
        processed_image = np.sqrt(np.square(processed_image_x) + np.square(processed_image_y))

        image_sd.modified_folder = image_sd.modified_folder + '_simple_gradient_filter/'
        image_sd.update(processed_image, '_simple_gradient_filter')

    @staticmethod
    def simple_gradient_x(image_sd: SPDImage):
        mask = np.array([
            [-1, -1, -1], [0, 0, 0], [1, 1, 1],
        ])

        processed_image = ImageModelDriver.convolution_2d(image_sd, mask)

        image_sd.modified_folder = image_sd.modified_folder + '_simple_gradient_x_filter' + '/'
        image_sd.update(processed_image, '_simple_gradient_x_filter')

    @staticmethod
    def simple_gradient_y(image_sd: SPDImage):
        mask = np.array([
            [-1, 0, 1], [-1, 0, 1], [-1, 0, 1]
        ])

        processed_image = ImageModelDriver.convolution_2d(image_sd, mask)

        image_sd.modified_folder = image_sd.modified_folder + '_simple_gradient_y_filter' + '/'
        image_sd.update(processed_image, '_simple_gradient_y_filter')

    @staticmethod
    def sobel_gradient(image_sd: SPDImage):
        mask_x = np.array([
            [-1, -2, -1], [0, 0, 0], [1, 2, 1],
        ])

        mask_y = np.array([
            [-1, 0, 1], [-2, 0, 2], [-1, 0, 1]
        ])

        processed_image_x = ImageModelDriver.convolution_2d(image_sd, mask_x)
        processed_image_y = ImageModelDriver.convolution_2d(image_sd, mask_y)
        processed_image = np.sqrt(np.square(processed_image_x) + np.square(processed_image_y))

        image_sd.modified_folder = image_sd.modified_folder + '_sobel_gradient_filter' + '/'
        image_sd.update(processed_image, '_sobel_gradient_filter')



    @staticmethod
    def sobel_gradient_x(image_sd: SPDImage):
        mask = np.array([
            [-1, -2, -1], [0, 0, 0], [1, 2, 1],
        ])

        processed_image = ImageModelDriver.convolution_2d(image_sd, mask)

        image_sd.modified_folder = image_sd.modified_folder + '_sobel_gradient_x_filter' + '/'
        image_sd.update(processed_image, '_sobel_gradient_x_filter')

    @staticmethod
    def sobel_gradient_y(image_sd: SPDImage):
        mask = np.array([
            [-1, 0, 1], [-2, 0, 2], [-1, 0, 1]
        ])

        processed_image = ImageModelDriver.convolution_2d(image_sd, mask)

        image_sd.modified_folder = image_sd.modified_folder + '_sobel_gradient_y_filter' + '/'
        image_sd.update(processed_image, '_sobel_gradient_y_filter')

    @staticmethod
    def laplas_gradient(image_sd: SPDImage):
        mask = np.array([
            [-1, -1, -1], [-1, 8, -1], [-1, -1, -1]
        ])

        processed_image = ImageModelDriver.convolution_2d(image_sd, mask)

        ShF = 100
        processed_image = processed_image * ShF / np.amax(processed_image)

        image_sd.modified_folder = image_sd.modified_folder + '_laplas_gradient_filter' + '/'
        image_sd.update(processed_image, '_laplas_gradient_filter')

    @staticmethod
    def convolution_2d(image_sd: SPDImage, kernel):
        image = image_sd.modified_image
        image_row, image_col = image.shape
        kernel_row, kernel_col = kernel.shape

        output = np.zeros_like(image)

        pad_height = int((kernel_row - 1) / 2)
        pad_width = int((kernel_col - 1) / 2)

        padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))

        padded_image[pad_height:-pad_height, pad_width:-pad_width] = image

        for row in range(image_row):
            for col in range(image_col):
                output[row, col] = np.sum(kernel * padded_image[row:row + kernel_row, col:col + kernel_col])

        return output

    @staticmethod
    def dilate(image_sd: SPDImage, dilation_level=3):
        dilation_level = 3 if dilation_level < 3 else dilation_level

        structuring_kernel = np.full(shape=(dilation_level, dilation_level), fill_value=255)
        image_src = image_sd.modified_image

        orig_shape = image_src.shape
        pad_width = dilation_level - 2

        image_pad = np.pad(array=image_src, pad_width=pad_width, mode='constant')
        pimg_shape = image_pad.shape
        h_reduce, w_reduce = (pimg_shape[0] - orig_shape[0]), (pimg_shape[1] - orig_shape[1])

        flat_submatrices = np.array([
            image_pad[i:(i + dilation_level), j:(j + dilation_level)]
            for i in range(pimg_shape[0] - h_reduce) for j in range(pimg_shape[1] - w_reduce)
        ])

        image_dilate = np.array([255 if (i == structuring_kernel).any() else 0 for i in flat_submatrices])
        image_dilate = image_dilate.reshape(orig_shape)
        image_sd.update(image_dilate, '_dilate_')

    @staticmethod
    def erode(image_sd: SPDImage, erosion_level=3):
        erosion_level = 3 if erosion_level < 3 else erosion_level

        structuring_kernel = np.full(shape=(erosion_level, erosion_level), fill_value=255)
        image_src = image_sd.modified_image

        orig_shape = image_src.shape
        pad_width = erosion_level - 2

        image_pad = np.pad(array=image_src, pad_width=pad_width, mode='constant')
        pimg_shape = image_pad.shape
        h_reduce, w_reduce = (pimg_shape[0] - orig_shape[0]), (pimg_shape[1] - orig_shape[1])

        flat_submatrices = np.array([
            image_pad[i:(i + erosion_level), j:(j + erosion_level)]
            for i in range(pimg_shape[0] - h_reduce) for j in range(pimg_shape[1] - w_reduce)
        ])

        image_erode = np.array([255 if (i == structuring_kernel).all() else 0 for i in flat_submatrices])
        image_erode = image_erode.reshape(orig_shape)
        image_sd.update(image_erode, '_erode_')
        image.update(final_img, '_otsu')

    @staticmethod
    def automatic_brightness_and_contrast(image: SPDImage, clip_hist_percent=1):
        hist = HistogramModelDriver.histogram(image.modified_image, image.max_type_colors_count())[0]
        accumulator = HistogramModelDriver.cdf(hist)[0]
        maximum = accumulator[-1]
        clip_hist_percent *= (maximum / 100.0)

        minimum_gray = 0
        while accumulator[minimum_gray] < clip_hist_percent:
            minimum_gray += 1

        maximum_gray = len(hist) - 1
        while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
            maximum_gray -= 1

        median = np.median(accumulator)
        medium_gray = 0
        while accumulator[medium_gray] < median:
            medium_gray += 1

        gamma = np.log(np.abs(medium_gray - minimum_gray)/np.abs(maximum_gray - medium_gray))
        print(gamma)
        ImageModelDriver.gamma_correction(image, 1, gamma)
