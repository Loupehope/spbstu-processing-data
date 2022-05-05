from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Drivers.ReadDriver import *
from Drivers.HistogramModelDriver import *
from Drivers.PlotDriver import *

class ImageLesson9:

    @staticmethod
    def run():
        # ----------------------
        # Загружаем фото model.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson9/', 'model', '.jpg', np.uint8)

        ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)
        ImageModelDriver.threshold(loaded_image_model, 200)
        ImageModelDriver.high_pass_filter(loaded_image_model, 'gausse', 100)
        ImageModelDriver.threshold(loaded_image_model, 20)

        ImageDisplayDriver.save(loaded_image_model)

        # ----------------------
        # Загружаем фото model_salt_and_pepper_and_noize.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson9/', 'model_salt_and_pepper_and_noize', '.jpg', np.uint8)

        ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)
        ImageModelDriver.threshold(loaded_image_model, 200)
        ImageDisplayDriver.save(loaded_image_model)

        ImageModelDriver.high_pass_filter(loaded_image_model, 'gausse', 100)
        ImageModelDriver.threshold(loaded_image_model, 20)

        ImageDisplayDriver.save(loaded_image_model)

        # ----------------------
        # Загружаем фото model_linear_filter.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson9/', 'model_linear_filter', '.jpg', np.uint8)

        ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)

        histogram = HistogramModelDriver.histogram(
            loaded_image_model.modified_image,
            loaded_image_model.max_type_colors_count()
        )
        PlotDriver.plot(histogram, loaded_image_model, 'original_')

        ImageModelDriver.threshold(loaded_image_model, 200)
        ImageModelDriver.high_pass_filter(loaded_image_model, 'gausse', 100)
        ImageModelDriver.threshold(loaded_image_model, 20)

        ImageDisplayDriver.save(loaded_image_model)

        # ----------------------
        # Загружаем фото model_median_filter.jpg
        # ----------------------

        loaded_image_model = SPDImage.fromFile('lesson9/', 'model_median_filter', '.jpg', np.uint8)

        ImageModelDriver.low_pass_filter(loaded_image_model, 'gausse', 60)

        histogram = HistogramModelDriver.histogram(
            loaded_image_model.modified_image,
            loaded_image_model.max_type_colors_count()
        )
        PlotDriver.plot(histogram, loaded_image_model, 'original_')

        ImageModelDriver.threshold(loaded_image_model, 200)
        ImageModelDriver.high_pass_filter(loaded_image_model, 'gausse', 100)
        ImageModelDriver.threshold(loaded_image_model, 20)

        ImageDisplayDriver.save(loaded_image_model)