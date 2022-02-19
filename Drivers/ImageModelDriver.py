import numpy as np
from Models.SPDImage import *
from PIL import Image


class ImageModelDriver:

    @staticmethod
    def multi_shift(data: SPDImage, c):
        result_array = []

        for row in data.modified_image:
            y_array = [y * c for y in row]
            result_array.append(y_array)

        data.modified_image = np.array(result_array)
        data.counter += 1
        data.modified_name = data.name + '_' + str(data.counter) + '_multi_shift'

    @staticmethod
    def add_shift(data: SPDImage, c):
        result_array = []

        for row in data.modified_image:
            y_array = [y + c for y in row]
            result_array.append(y_array)

        data.modified_image = np.array(result_array)
        data.counter += 1
        data.modified_name = data.name + '_' + str(data.counter) + '_add_shift'

    @staticmethod
    def grayscale(data: SPDImage, dtype=np.uint8):
        max_a = np.max(data.modified_image)
        min_a = np.min(data.modified_image)
        diff_a = max_a - min_a
        result_array = []

        for row in data.modified_image:
            y_array = [(y - min_a) * np.iinfo(dtype).max / diff_a for y in row]
            result_array.append(y_array)

        data.modified_image = np.array(result_array)
        data.counter += 1
        data.modified_name = data.name + '_' + str(data.counter) + '_grayscale'

    @staticmethod
    def rotate90(data: SPDImage):
        data.modified_image = np.rot90(data.modified_image)
        data.counter += 1
        data.modified_name = data.name + '_' + str(data.counter) + '_rotated'

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

        data.modified_image = np.array(resized_image, copy=True)
        data.counter += 1
        data.modified_name = data.name + '_' + str(data.counter) + '_resized_' + resample_type_text
