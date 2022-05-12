from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Drivers.ReadDriver import *
from Drivers.PlotDriver import *
from Drivers.HistogramModelDriver import *

class ImageLesson4:

    @staticmethod
    def evaluate(image: SPDImage):
        # Считаем гистограммы
        histogram = HistogramModelDriver.histogram(
            image.modified_image,
            image.max_type_colors_count()
        )
        cdf = HistogramModelDriver.cdf(histogram[0])
        cdf_inverse = HistogramModelDriver.inverse_cdf(cdf[0])

        PlotDriver.plot(histogram, image, 'original_')
        PlotDriver.plot(cdf, image, 'original_')
        PlotDriver.plot_by_x_and_y(cdf_inverse, image.folder + 'inv_' + image.name + '/', 'test')
        # Эквализация гистограммы
        HistogramModelDriver.equalize_image(image)

        # Сохраняем итоговое изображение
        ImageDisplayDriver.save(image)

        loaded_image = SPDImage.fromFile('lesson4/', image.modified_name, '.jpg', np.uint8)

        new_histogram = HistogramModelDriver.histogram(
            loaded_image.modified_image,
            loaded_image.max_type_colors_count()
        )
        new_cdf = HistogramModelDriver.cdf(new_histogram[0])

        PlotDriver.plot_raw(new_histogram, 'lesson4/plots_' + image.name + '/', 'eq_' + image.name + '_hist')
        PlotDriver.plot_raw(new_cdf, 'lesson4/plots_' + image.name + '/', 'eq_' + image.name + '_cdf')

    @staticmethod
    def run():

        # ----------------------
        # Загружаем ренгены
        # ----------------------

        loaded_rengens = [
            # ReadDriver.image_binary_read(
            #     'lesson4/', 'c12-85v', '.jpg', '>H', 1024, 1024, 5120
            # ),
            # ReadDriver.image_binary_read(
            #     'lesson4/', 'u0', '.jpg', '>H', 2048, 2500, 5120
            # )
        ]

        for image in loaded_rengens:
            # Обрабатываем
            ImageModelDriver.rotate90(image)
            ImageModelDriver.negative(image)
            ImageModelDriver.grayscale(image)
            ImageDisplayDriver.save(image)

            image.reset()

            ImageModelDriver.rotate90(image)
            ImageModelDriver.negative(image)
            # Считаем гистограммы
            ImageLesson4.evaluate(image)

        # ----------------------
        # Загружаем обычные jpg
        # ----------------------

        loaded_jpgs = [
            SPDImage.fromFile('lesson4/', 'photo1', '.jpg', np.uint8),
            SPDImage.fromFile('lesson4/', 'photo2', '.jpg', np.uint8),
            # SPDImage.fromFile('lesson4/', 'photo3', '.jpg', np.uint8),
            # SPDImage.fromFile('lesson4/', 'photo4', '.jpg', np.uint8),
            # SPDImage.fromFile('lesson4/', 'grace', '.jpg', np.uint8),
            # SPDImage.fromFile('lesson4/', 'HollywoodLC', '.jpg', np.uint8)
        ]

        for image in loaded_jpgs:
            # Считаем гистограммы
            ImageLesson4.evaluate(image)

