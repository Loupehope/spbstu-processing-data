import numpy as np
from Models.SPDImage import *
from Analyze.AnalyzeModel import *
from PIL import Image
from Analyze.Filters import *
import numba


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
            y_array = [const * (np.power(y, gamma)) for y in row]
            result_array.append(y_array)

        data.update(np.array(result_array), '_gamma_correction')

    # Делаем изображение более контрастным при увеличении const
    # Делаем изображение менее констрастным при уменьшении const
    @staticmethod
    def log_correction(data: SPDImage, const):
        result_array = []

        for row in data.modified_image:
            y_array = [const * (np.log10(y + 1)) for y in row]
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
            auto_fourier = AnalyzeModel.fourier(auto, dt)
            max_auto_fourier_freq_idx = np.argmax(auto_fourier[1])
            max_auto_fourier_freq = auto_fourier[0][max_auto_fourier_freq_idx] // 0.01 * 0.01
            max_auto_freq.append(max_auto_fourier_freq)

        max_mutal_freq = []
        for row_idx in range(0, len(diff_im)):
            row_f = diff_im[row_idx]
            row_s = diff_im[(row_idx + 1) % len(diff_im)]
            mutal = AnalyzeModel.mutual_corr_array(row_f, row_s)
            mutal_fourier = AnalyzeModel.fourier(mutal, dt)
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
    def fix_moire_for_image(image: SPDImage, result_freqs) -> bool:
        if len(result_freqs) == 0:
            print('Не нашлась решетка на изображении!')
            return False

        first_top_freq = result_freqs[0]
        filter = Filters.bsw_filter(first_top_freq - 0.05, first_top_freq + 0.05, 1, 32)[1]

        print('Работаем с частотой: ' + str(first_top_freq))

        result = []
        for row in image.modified_image:
            conv = ImageModelDriver.convolution(np.array(row), np.array(filter), 1)[1]
            result.append(conv)

        image.update(result, '_fixed')

        print('Изображение ' + image.name + ' исправлено!\n')

        return True
