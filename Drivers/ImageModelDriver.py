import numpy as np
from Models.SPDImage import *


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
