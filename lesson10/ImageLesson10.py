from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Drivers.ReadDriver import *

class ImageLesson10:

    @staticmethod
    def run():
        # ----------------------
        # Загружаем фото model.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson10/', 'model', '.jpg', np.uint8)

        ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)
        ImageModelDriver.threshold(loaded_image_model, 200)
        ImageModelDriver.sobel_gradient(loaded_image_model)
        ImageModelDriver.threshold(loaded_image_model, 20)

        ImageDisplayDriver.save(loaded_image_model)

        # ----------------------
        # Загружаем фото model_salt_and_pepper_and_noize.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson10/', 'model_salt_and_pepper_and_noize', '.jpg', np.uint8)

        ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)
        ImageModelDriver.threshold(loaded_image_model, 200)
        ImageModelDriver.sobel_gradient(loaded_image_model)
        ImageModelDriver.threshold(loaded_image_model, 20)

        ImageDisplayDriver.save(loaded_image_model)

        # ----------------------
        # Загружаем фото model_linear_filter.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson10/', 'model_linear_filter', '.jpg', np.uint8)

        ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)
        ImageModelDriver.threshold(loaded_image_model, 200)
        ImageModelDriver.sobel_gradient(loaded_image_model)
        ImageModelDriver.threshold(loaded_image_model, 15)

        ImageDisplayDriver.save(loaded_image_model)

        # ----------------------
        # Загружаем фото model_median_filter.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson10/', 'model_median_filter', '.jpg', np.uint8)

        ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)
        ImageModelDriver.threshold(loaded_image_model, 200)
        ImageModelDriver.sobel_gradient(loaded_image_model)
        ImageModelDriver.threshold(loaded_image_model, 15)

        ImageDisplayDriver.save(loaded_image_model)