import numpy as np

from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Drivers.ReadDriver import *
from Drivers.HistogramModelDriver import *
from Drivers.PlotDriver import *
import cv2

class ImageLesson12:

    @staticmethod
    def run():

        def very_simple(image_sd: SPDImage):
            ImageModelDriver.grayscale(image_sd)
            ImageDisplayDriver.save(image_sd)

            image_sd.reset()

            HistogramModelDriver.equalize_image(image_sd, is_inverse_cdf=False)
            ImageModelDriver.automatic_brightness_and_contrast(image_sd, 5)
            ImageModelDriver.grayscale(image_sd)

            ImageDisplayDriver.save(image_sd)

        def clahe(image_sd: SPDImage):
            ImageModelDriver.grayscale(image_sd)
            ImageDisplayDriver.save(image_sd)

            image_sd.reset()

            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(12, 12))
            equalized = clahe.apply(image_sd.modified_image)
            image_sd.update(equalized, '_clahe')
            ImageModelDriver.grayscale(image_sd)

            ImageDisplayDriver.save(image_sd)

        # Загружаем фото brain-H_x512
        loaded_image_c12_85v = ReadDriver.image_binary_read(
            'lesson12/', 'brain-H_x512', '.jpg', '<H', 512, 512, 0, '.bin'
        )

        very_simple(loaded_image_c12_85v)

        # Загружаем фото c12-85v.xcr
        loaded_image_c12_85v = ReadDriver.image_binary_read(
            'lesson12/', 'brain-V_x256', '.jpg', '<H', 256, 256, 0, '.bin'
        )

        very_simple(loaded_image_c12_85v)

        # Загружаем фото c12-85v.xcr
        loaded_image_c12_85v = ReadDriver.image_binary_read(
            'lesson12/', 'spine-H_x256', '.jpg', '<H', 256, 256, 0, '.bin'
        )

        very_simple(loaded_image_c12_85v)

        # Загружаем фото c12-85v.xcr
        loaded_image_c12_85v = ReadDriver.image_binary_read(
            'lesson12/', 'spine-V_x512', '.jpg', '<H', 512, 512, 0, '.bin'
        )

        very_simple(loaded_image_c12_85v)

