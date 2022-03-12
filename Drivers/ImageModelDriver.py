import numpy as np
from Models.SPDImage import *
from PIL import Image


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
    def convolution(main_data, add_data, dt):
        x_array = []
        y_array = []

        for i in range(len(main_data) + len(add_data)):
            sum = 0

            for j in range(len(add_data)):
                if range(len(main_data)).__contains__(i - j):
                    sum += main_data[i - j] * add_data[j]
                else:
                    sum += 0

            if (len(add_data) / 2) <= i < (len(main_data) + len(add_data) / 2):
                y_array.append(sum)
                x_array.append((i - len(add_data) / 2) * dt)

        return [x_array, y_array]
