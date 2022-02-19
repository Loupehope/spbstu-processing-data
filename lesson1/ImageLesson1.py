from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Models.SPDImage import *
from PIL import Image


class ImageLesson1:

    @staticmethod
    def run():
        # Загружаем фото
        loaded_image = SPDImage.fromFile('lesson1/', 'photo', '.jpg', np.uint8)

        # Обрабатываем
        ImageModelDriver.add_shift(loaded_image, 30)
        ImageDisplayDriver.save(loaded_image)

        ImageModelDriver.multi_shift(loaded_image, 1.3)
        ImageDisplayDriver.save(loaded_image)

        ImageModelDriver.grayscale(loaded_image)
        ImageDisplayDriver.save(loaded_image)

        ImageModelDriver.resize(loaded_image, Image.NEAREST, 1.3)
        ImageDisplayDriver.save(loaded_image)
