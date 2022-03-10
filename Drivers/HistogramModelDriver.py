import numpy as np
from Models.SPDImage import *
from PIL import Image


class HistogramModelDriver:

    @staticmethod
    def histogram(data: SPDImage) -> (list, str):
        image_from_array = Image.fromarray(data.modified_image.astype(data.dtype))
        return image_from_array.histogram(), '_hist'

    @staticmethod
    def cdf(histogram, data: SPDImage) -> (list, str):
        return np.cumsum(histogram, axis=0), '_cdf'

    @staticmethod
    def equalize_image(data: SPDImage):
        histogram = HistogramModelDriver.histogram(data)[0]
        cdf = HistogramModelDriver.cdf(histogram, data)[0]
        image_equalized = np.interp(data.modified_image, range(0, 256), cdf)

        data.update(image_equalized, '_cdf_normalize')
