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

        # Убираем шум
        ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)
        ImageModelDriver.threshold(loaded_image_model, 200)

        loaded_image_model_x = loaded_image_model.copy()
        loaded_image_model_x.modified_folder = loaded_image_model.modified_folder

        loaded_image_model_y = loaded_image_model.copy()
        loaded_image_model_y.modified_folder = loaded_image_model.modified_folder

        ImageModelDriver.sobel_gradient(loaded_image_model)
        # ImageDisplayDriver.save(loaded_image_model)

        ImageModelDriver.sobel_gradient_x(loaded_image_model_x)
        ImageModelDriver.sobel_gradient_y(loaded_image_model_y)

        ImageModelDriver.grayscale(loaded_image_model)
        ImageModelDriver.grayscale(loaded_image_model_x)
        ImageModelDriver.grayscale(loaded_image_model_y)

        ImageDisplayDriver.save(loaded_image_model)
        ImageDisplayDriver.save(loaded_image_model_x)
        ImageDisplayDriver.save(loaded_image_model_y)

        # ----------------------
        # Загружаем фото model_salt_and_pepper_and_noize.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson10/', 'model_salt_and_pepper_and_noize', '.jpg', np.uint8)

        # Убираем шум
        ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)
        ImageModelDriver.threshold(loaded_image_model, 200)

        ImageModelDriver.sobel_gradient(loaded_image_model)
        # ImageDisplayDriver.save(loaded_image_model)

        ImageModelDriver.grayscale(loaded_image_model)

        ImageDisplayDriver.save(loaded_image_model)

        # ----------------------
        # Загружаем фото model_linear_filter.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson10/', 'model_linear_filter', '.jpg', np.uint8)

        # Убираем шум
        ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)
        ImageModelDriver.threshold(loaded_image_model, 200)

        ImageModelDriver.sobel_gradient(loaded_image_model)
        # ImageDisplayDriver.save(loaded_image_model)

        ImageModelDriver.grayscale(loaded_image_model)

        ImageDisplayDriver.save(loaded_image_model)

        # ----------------------
        # Загружаем фото model_median_filter.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson10/', 'model_median_filter', '.jpg', np.uint8)

        # Убираем шум
        ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)
        ImageModelDriver.threshold(loaded_image_model, 200)

        ImageModelDriver.sobel_gradient(loaded_image_model)
        # ImageDisplayDriver.save(loaded_image_model)

        ImageModelDriver.grayscale(loaded_image_model)

        ImageDisplayDriver.save(loaded_image_model)
