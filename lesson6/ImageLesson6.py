from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Drivers.PlotDriver import *


class ImageLesson6:

    @staticmethod
    def run():
        # ----------------------
        # Загружаем фото model.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson6/', 'model', '.jpg', np.uint8)
        loaded_image_model.modified_folder = loaded_image_model.folder + "salt_pepper/"

        ImageModelDriver.salt_pepper(loaded_image_model, 3)
        ImageDisplayDriver.save(loaded_image_model)

        loaded_image_model_linear_filter = loaded_image_model.copy()
        loaded_image_model_linear_filter.modified_folder = loaded_image_model.folder + "salt_pepper/"

        ImageModelDriver.linear_filter(loaded_image_model_linear_filter, 3)
        ImageDisplayDriver.save(loaded_image_model_linear_filter)

        loaded_image_model_median_filter = loaded_image_model.copy()
        loaded_image_model_median_filter.modified_folder = loaded_image_model.folder + "salt_pepper/"

        ImageModelDriver.median_filter(loaded_image_model_median_filter, 3)
        ImageDisplayDriver.save(loaded_image_model_median_filter)

        loaded_image_model.reset()

        loaded_image_model.modified_folder = loaded_image_model.folder + "random_noize/"

        ImageModelDriver.random_noize(loaded_image_model, 10)
        ImageDisplayDriver.save(loaded_image_model)

        loaded_image_model_linear_filter = loaded_image_model.copy()
        loaded_image_model_linear_filter.modified_folder = loaded_image_model.folder + "random_noize/"

        ImageModelDriver.linear_filter(loaded_image_model_linear_filter, 3)
        ImageDisplayDriver.save(loaded_image_model_linear_filter)

        loaded_image_model_median_filter = loaded_image_model.copy()
        loaded_image_model_median_filter.modified_folder = loaded_image_model.folder + "random_noize/"

        ImageModelDriver.median_filter(loaded_image_model_median_filter, 3)
        ImageDisplayDriver.save(loaded_image_model_median_filter)
