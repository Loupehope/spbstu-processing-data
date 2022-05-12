import numpy as np
from Models.SPDImage import *
from PIL import Image
import numba
from scipy.optimize import minimize


class HistogramModelDriver:

    @staticmethod
    @numba.jit(nopython=True)
    def histogram(image: np.ndarray, pixel_colors_count: int) -> (np.ndarray, str):
        h = [0] * pixel_colors_count
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                i = int(image[x, y])
                h[i] = h[i] + 1
        return np.array(h), '_hist'

    @staticmethod
    @numba.jit(nopython=True)
    def cdf(histogram: np.ndarray) -> (np.ndarray, str):
        h = [0] * len(histogram)
        for x in range(len(histogram)):
            for y in range(x + 1):
                h[x] = h[x] + histogram[y]

        return np.array(h), '_cdf'

    @staticmethod
    def inverse_cdf(cdf: np.ndarray):
        x_array = np.linspace(0, len(cdf) - 1, len(cdf))
        y_array = cdf

        max_x = x_array[len(cdf) - 1]
        max_y = y_array[len(cdf) - 1]

        new_x_array = y_array.astype(np.float64)
        new_y_array = x_array

        new_y_array *= int(max_y / max_x)
        new_x_array /= int(max_y / max_x)

        for i in range(len(new_x_array)):
            new_x_array[i] = round(new_x_array[i])

        return [new_x_array.astype(np.int64), new_y_array]

    @staticmethod
    @numba.jit(nopython=True)
    def equalize_numba(image: np.ndarray, cdf_x: np.ndarray, cdf_y: np.ndarray) -> np.ndarray:
        new_image = image
        cdf_min = np.min(cdf_y)

        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                idx = int(cdf_x[new_image[x, y]])
                new_image[x, y] = round(
                    (cdf_y[idx] - cdf_min) * 255.0 / (image.shape[0] * image.shape[1] - 1)
                )

        return new_image

    @staticmethod
    def equalize_image(image: SPDImage, max_type_colors_count=-1, is_inverse_cdf=False):
        if max_type_colors_count < 0:
            max_type_colors_count = int(image.max_type_colors_count())

        histogram = np.array(HistogramModelDriver.histogram(
            np.array(image.modified_image),
            max_type_colors_count
        )[0])

        cdf_y = np.array(HistogramModelDriver.cdf(histogram)[0])
        cdf_x = np.linspace(0, len(cdf_y) - 1, len(cdf_y))

        if is_inverse_cdf:
            cdf = HistogramModelDriver.inverse_cdf(cdf_y)
            cdf_y = cdf[1]
            cdf_x = cdf[0]

        cdf_x = np.array(cdf_x)
        cdf_y = np.array(cdf_y)

        image_equalized = HistogramModelDriver.equalize_numba(np.array(image.modified_image), cdf_x, cdf_y)

        image.update(np.abs(image_equalized), '_cdf_normalize')
