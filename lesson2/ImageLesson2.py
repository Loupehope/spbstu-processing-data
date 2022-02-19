from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Drivers.ReadDriver import *
from PIL import Image


class ImageLesson2:

    @staticmethod
    def run():
        # Загружаем фото c12-85v.xcr
        loaded_image_c12_85v = ReadDriver.image_binary_read(
            'lesson2/', 'c12-85v', '.jpg', '>H', 1024, 1024, 5120
        )

        # Обрабатываем
        ImageModelDriver.rotate90(loaded_image_c12_85v)
        ImageModelDriver.grayscale(loaded_image_c12_85v)
        ImageDisplayDriver.save(loaded_image_c12_85v)

        ImageModelDriver.resize(loaded_image_c12_85v, Image.BILINEAR, 0.6)
        ImageDisplayDriver.save(loaded_image_c12_85v)

        # Загружаем фото u0.xcr
        loaded_image_u0 = ReadDriver.image_binary_read(
            'lesson2/', 'u0', '.jpg', '>H', 2048, 2500, 5120
        )

        # Обрабатываем
        ImageModelDriver.rotate90(loaded_image_u0)
        ImageModelDriver.grayscale(loaded_image_u0)
        ImageDisplayDriver.save(loaded_image_u0)

        ImageModelDriver.resize(loaded_image_u0, Image.BILINEAR, 0.6)
        ImageDisplayDriver.save(loaded_image_u0)

