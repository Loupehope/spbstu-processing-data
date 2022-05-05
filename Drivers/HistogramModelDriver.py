import numpy as np
from Models.SPDImage import *
from PIL import Image
import numba
from scipy.optimize import minimize


class HistogramModelDriver:

    @staticmethod
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
    @numba.jit(nopython=True)
    def equalize_numba(image: np.ndarray, cdf: np.ndarray) -> np.ndarray:
        new_image = image
        cdf_min = cdf[cdf != 0].min()

        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                new_image[x, y] = round(
                    (cdf[new_image[x, y]] - cdf_min) * 255.0 / (image.shape[0] * image.shape[1] - 1)
                )

        return new_image

    @staticmethod
    def equalize_image(image: SPDImage):
        histogram = HistogramModelDriver.histogram(
            image.modified_image,
            image.max_type_colors_count()
        )[0]

        cdf = HistogramModelDriver.cdf(histogram)[0]
        image_equalized = HistogramModelDriver.equalize_numba(image.modified_image, cdf)

        image.update(image_equalized, '_cdf_normalize')
