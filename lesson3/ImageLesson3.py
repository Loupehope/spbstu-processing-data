from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Drivers.ReadDriver import *
from PIL import Image


class ImageLesson3:

    @staticmethod
    def run():

        # ----------------------
        # Загружаем фото c12-85v.xcr
        # ----------------------

        loaded_image_c12_85v = ReadDriver.image_binary_read(
            'lesson3/', 'c12-85v', '.jpg', '>H', 1024, 1024, 5120
        )

        # Обрабатываем
        ImageModelDriver.rotate90(loaded_image_c12_85v)
        ImageModelDriver.negative(loaded_image_c12_85v)
        ImageModelDriver.grayscale(loaded_image_c12_85v)
        ImageDisplayDriver.save(loaded_image_c12_85v)

        # ----------------------
        # Загружаем фото u0.xcr
        # ----------------------

        loaded_image_u0 = ReadDriver.image_binary_read(
            'lesson3/', 'u0', '.jpg', '>H', 2048, 2500, 5120
        )

        # Обрабатываем
        ImageModelDriver.rotate90(loaded_image_u0)
        ImageModelDriver.negative(loaded_image_u0)
        ImageModelDriver.grayscale(loaded_image_u0)
        ImageDisplayDriver.save(loaded_image_u0)

        # ----------------------
        # Загружаем фото grace.jpg
        # ----------------------

        loaded_image_grace = SPDImage.fromFile('lesson3/', 'grace', '.jpg', np.uint8)

        # Обрабатываем
        ImageModelDriver.negative(loaded_image_grace)
        ImageModelDriver.grayscale(loaded_image_grace)
        ImageDisplayDriver.save(loaded_image_grace)

        # ----------------------
        # Загружаем фото photo1.jpg
        # ----------------------

        loaded_image_photo1 = SPDImage.fromFile('lesson3/', 'photo1', '.jpg', np.uint8)

        # Обрабатываем
        ImageModelDriver.gamma_correction(loaded_image_photo1, 1, 0.4)
        ImageModelDriver.grayscale(loaded_image_photo1)
        ImageDisplayDriver.save(loaded_image_photo1)

        # ----------------------
        # Загружаем фото photo2.jpg
        # ----------------------

        loaded_image_photo2 = SPDImage.fromFile('lesson3/', 'photo2', '.jpg', np.uint8)

        # Обрабатываем
        ImageModelDriver.gamma_correction(loaded_image_photo2, 1, 0.4)
        ImageModelDriver.grayscale(loaded_image_photo2)
        ImageDisplayDriver.save(loaded_image_photo2)

        # ----------------------
        # Загружаем фото photo3.jpg
        # ----------------------

        loaded_image_photo3 = SPDImage.fromFile('lesson3/', 'photo3', '.jpg', np.uint8)

        # Обрабатываем
        ImageModelDriver.gamma_correction(loaded_image_photo3, 1, 0.4)
        ImageModelDriver.grayscale(loaded_image_photo3)
        ImageDisplayDriver.save(loaded_image_photo3)

        # ----------------------
        # Загружаем фото photo4.jpg
        # ----------------------

        loaded_image_photo4 = SPDImage.fromFile('lesson3/', 'photo4', '.jpg', np.uint8)

        # Обрабатываем
        ImageModelDriver.gamma_correction(loaded_image_photo4, 1, 0.4)
        ImageModelDriver.grayscale(loaded_image_photo4)
        ImageDisplayDriver.save(loaded_image_photo4)

        # ----------------------
        # Загружаем фото HollywoodLC.jpg
        # ----------------------

        loaded_image_HollywoodLC = SPDImage.fromFile('lesson3/', 'HollywoodLC', '.jpg', np.uint8)

        # Обрабатываем
        ImageModelDriver.gamma_correction(loaded_image_HollywoodLC, 1, 2)
        ImageModelDriver.grayscale(loaded_image_HollywoodLC)
        ImageDisplayDriver.save(loaded_image_HollywoodLC)

