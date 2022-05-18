import numpy as np
import numba
import random
from Models.SPDImage import *


class Stones:

    @staticmethod
    def enumerate_stones(image_sd) -> int:
        image_row, image_col = image_sd.shape
        pad_height = 1
        pad_width = 1

        padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))
        padded_image[pad_height:-pad_height, pad_width:-pad_width] = image_sd

        stones = 0

        for i in range(1, image_row + 2, 1):
            for j in range(1, image_col + 2, 1):
                if padded_image[i][j] == 0:
                    continue

                is_stone = padded_image[i - 1][j - 1]
                is_stone += padded_image[i - 1][j]
                is_stone += padded_image[i - 1][j + 1]

                is_stone += padded_image[i][j - 1]
                is_stone += padded_image[i][j + 1]

                is_stone += padded_image[i + 1][j - 1]
                is_stone += padded_image[i + 1][j]
                is_stone += padded_image[i + 1][j + 1]

                if is_stone == 0:
                    stones += 1

        return stones