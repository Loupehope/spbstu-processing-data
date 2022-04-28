from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Drivers.ReadDriver import *

class ImageLesson11:

    @staticmethod
    def run():

        def dilate_and_erode(image_sd: SPDImage):
            # Убираем шум
            ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)
            ImageModelDriver.threshold(loaded_image_model, 200)

            original_image = image_sd.copy()

            ImageModelDriver.dilate(image_sd, 3)
            image_sd.modified_image = image_sd.modified_image - original_image.modified_image
            ImageDisplayDriver.save(image_sd)

            image_sd.reset()

            # Убираем шум
            ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)
            ImageModelDriver.threshold(loaded_image_model, 200)

            original_image = image_sd.copy()

            ImageModelDriver.erode(image_sd, 3)
            image_sd.modified_image = original_image.modified_image - image_sd.modified_image
            ImageDisplayDriver.save(image_sd)

        # ----------------------
        # Загружаем фото model.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson11/', 'model', '.jpg', np.uint8)
        dilate_and_erode(loaded_image_model)

        # ----------------------
        # Загружаем фото model_salt_and_pepper_and_noize.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson11/', 'model_salt_and_pepper_and_noize', '.jpg', np.uint8)
        dilate_and_erode(loaded_image_model)

        # ----------------------
        # Загружаем фото model_linear_filter.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson11/', 'model_linear_filter', '.jpg', np.uint8)
        dilate_and_erode(loaded_image_model)

        # ----------------------
        # Загружаем фото model_median_filter.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson11/', 'model_median_filter', '.jpg', np.uint8)
        dilate_and_erode(loaded_image_model)

