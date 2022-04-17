from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Drivers.ReadDriver import *

class ImageLesson9:

    @staticmethod
    def run():
        # ----------------------
        # Загружаем фото model.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson9/', 'model', '.jpg', np.uint8)

        ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)
        ImageModelDriver.high_pass_filter(loaded_image_model, 'gausse', 100)
        ImageModelDriver.threshold(loaded_image_model, 20)

        ImageDisplayDriver.save(loaded_image_model)

        # ----------------------
        # Загружаем фото model_salt_and_pepper_and_noize.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson9/', 'model_salt_and_pepper_and_noize', '.jpg', np.uint8)

        ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)
        ImageModelDriver.high_pass_filter(loaded_image_model, 'gausse', 100)
        ImageModelDriver.threshold(loaded_image_model, 35)

        ImageDisplayDriver.save(loaded_image_model)

        # ----------------------
        # Загружаем фото model_linear_filter.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson9/', 'model_linear_filter', '.jpg', np.uint8)

        ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)
        ImageModelDriver.high_pass_filter(loaded_image_model, 'gausse', 100)
        ImageModelDriver.threshold(loaded_image_model, 35)

        ImageDisplayDriver.save(loaded_image_model)

        # ----------------------
        # Загружаем фото model_median_filter.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson9/', 'model_median_filter', '.jpg', np.uint8)

        ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)
        ImageModelDriver.high_pass_filter(loaded_image_model, 'gausse', 100)
        ImageModelDriver.threshold(loaded_image_model, 25)

        ImageDisplayDriver.save(loaded_image_model)