from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Drivers.ReadDriver import *
from Drivers.PlotDriver import *
from Drivers.HistogramModelDriver import *

class ImageLesson4:

    @staticmethod
    def run():
        # ----------------------
        # Загружаем фото grace.jpg
        # ----------------------

        loaded_image_grace = SPDImage.fromFile('lesson4/', 'grace', '.jpg', np.uint8)

        # Считаем гистограммы
        histogram_grace = HistogramModelDriver.histogram(loaded_image_grace)
        cdf_grace = HistogramModelDriver.cdf(histogram_grace[0], loaded_image_grace)

        PlotDriver.plot(histogram_grace, loaded_image_grace, 'original_')
        PlotDriver.plot(cdf_grace, loaded_image_grace, 'original_')

        # Эквализация гистограммы
        HistogramModelDriver.equalize_image(loaded_image_grace)

        n_histogram_u0 = HistogramModelDriver.histogram(loaded_image_grace)
        n_cdf_u0 = HistogramModelDriver.cdf(n_histogram_u0[0], loaded_image_grace)

        PlotDriver.plot(n_histogram_u0, loaded_image_grace, 'eq_')
        PlotDriver.plot(n_cdf_u0, loaded_image_grace, 'eq_')

        # Сохраняем итоговое изображение
        ImageModelDriver.grayscale(loaded_image_grace)
        ImageDisplayDriver.save(loaded_image_grace)

        # ----------------------
        # Загружаем фото c12-85v.xcr
        # ----------------------

        loaded_image_c12_85v = ReadDriver.image_binary_read(
            'lesson4/', 'c12-85v', '.jpg', '>H', 1024, 1024, 5120
        )

        # Обрабатываем
        ImageModelDriver.rotate90(loaded_image_c12_85v)
        ImageModelDriver.negative(loaded_image_c12_85v)

        # Считаем гистограммы
        histogram_c12_85v = HistogramModelDriver.histogram(loaded_image_c12_85v)
        cdf_c12_85v = HistogramModelDriver.cdf(histogram_c12_85v[0], histogram_c12_85v)

        PlotDriver.plot(histogram_c12_85v, loaded_image_c12_85v, 'original_')
        PlotDriver.plot(cdf_c12_85v, loaded_image_c12_85v, 'original_')

        # Эквализация гистограммы
        ImageModelDriver.grayscale(loaded_image_c12_85v)
        HistogramModelDriver.equalize_image(loaded_image_c12_85v)

        n_histogram_u0 = HistogramModelDriver.histogram(loaded_image_c12_85v)
        n_cdf_u0 = HistogramModelDriver.cdf(n_histogram_u0[0], loaded_image_c12_85v)

        PlotDriver.plot(n_histogram_u0, loaded_image_c12_85v, 'eq_')
        PlotDriver.plot(n_cdf_u0, loaded_image_c12_85v, 'eq_')

        # Сохраняем итоговое изображение
        ImageModelDriver.grayscale(loaded_image_c12_85v)
        ImageDisplayDriver.save(loaded_image_c12_85v)

        # ----------------------
        # Загружаем фото u0.xcr
        # ----------------------

        loaded_image_u0 = ReadDriver.image_binary_read(
            'lesson4/', 'u0', '.jpg', '>H', 2048, 2500, 5120
        )

        # Обрабатываем
        ImageModelDriver.rotate90(loaded_image_u0)
        ImageModelDriver.negative(loaded_image_u0)

        # Считаем гистограммы
        histogram_u0 = HistogramModelDriver.histogram(loaded_image_u0)
        cdf_u0 = HistogramModelDriver.cdf(histogram_u0[0], histogram_u0)

        PlotDriver.plot(histogram_u0, loaded_image_u0, 'original_')
        PlotDriver.plot(cdf_u0, loaded_image_u0, 'original_')

        # Эквализация гистограммы
        ImageModelDriver.grayscale(loaded_image_u0)
        HistogramModelDriver.equalize_image(loaded_image_u0)

        n_histogram_u0 = HistogramModelDriver.histogram(loaded_image_u0)
        n_cdf_u0 = HistogramModelDriver.cdf(n_histogram_u0[0], loaded_image_u0)

        PlotDriver.plot(n_histogram_u0, loaded_image_u0, 'eq_')
        PlotDriver.plot(n_cdf_u0, loaded_image_u0, 'eq_')

        # Сохраняем итоговое изображение
        ImageModelDriver.grayscale(loaded_image_u0)
        ImageDisplayDriver.save(loaded_image_u0)

        # ----------------------
        # Загружаем фото photo1.jpg
        # ----------------------

        loaded_image_photo1 = SPDImage.fromFile('lesson4/', 'photo1', '.jpg', np.uint8)

        # Обрабатываем
        # Считаем гистограммы
        histogram_photo1 = HistogramModelDriver.histogram(loaded_image_photo1)
        cdf_photo1 = HistogramModelDriver.cdf(histogram_photo1[0], histogram_photo1)

        PlotDriver.plot(histogram_photo1, loaded_image_photo1, 'original_')
        PlotDriver.plot(cdf_photo1, loaded_image_photo1, 'original_')

        # Эквализация гистограммы
        HistogramModelDriver.equalize_image(loaded_image_photo1)

        n_histogram_u0 = HistogramModelDriver.histogram(loaded_image_photo1)
        n_cdf_u0 = HistogramModelDriver.cdf(n_histogram_u0[0], loaded_image_photo1)

        PlotDriver.plot(n_histogram_u0, loaded_image_photo1, 'eq_')
        PlotDriver.plot(n_cdf_u0, loaded_image_photo1, 'eq_')

        # Сохраняем итоговое изображение
        ImageModelDriver.grayscale(loaded_image_photo1)
        ImageDisplayDriver.save(loaded_image_photo1)

        # ----------------------
        # Загружаем фото photo2.jpg
        # ----------------------

        loaded_image_photo2 = SPDImage.fromFile('lesson4/', 'photo2', '.jpg', np.uint8)

        # Обрабатываем
        # Считаем гистограммы
        histogram_photo2 = HistogramModelDriver.histogram(loaded_image_photo2)
        cdf_photo2 = HistogramModelDriver.cdf(histogram_photo2[0], histogram_photo2)

        PlotDriver.plot(histogram_photo2, loaded_image_photo2, 'original_')
        PlotDriver.plot(cdf_photo2, loaded_image_photo2, 'original_')

        # Эквализация гистограммы
        HistogramModelDriver.equalize_image(loaded_image_photo2)

        n_histogram_u0 = HistogramModelDriver.histogram(loaded_image_photo2)
        n_cdf_u0 = HistogramModelDriver.cdf(n_histogram_u0[0], loaded_image_photo2)

        PlotDriver.plot(n_histogram_u0, loaded_image_photo2, 'eq_')
        PlotDriver.plot(n_cdf_u0, loaded_image_photo2, 'eq_')

        # Сохраняем итоговое изображение
        ImageModelDriver.grayscale(loaded_image_photo2)
        ImageDisplayDriver.save(loaded_image_photo2)

        # ----------------------
        # Загружаем фото photo3.jpg
        # ----------------------

        loaded_image_photo3 = SPDImage.fromFile('lesson4/', 'photo3', '.jpg', np.uint8)

        # Обрабатываем
        # Считаем гистограммы
        histogram_photo3 = HistogramModelDriver.histogram(loaded_image_photo3)
        cdf_photo3 = HistogramModelDriver.cdf(histogram_photo3[0], histogram_photo3)

        PlotDriver.plot(histogram_photo3, loaded_image_photo3, 'original_')
        PlotDriver.plot(cdf_photo3, loaded_image_photo3, 'original_')

        # Эквализация гистограммы
        HistogramModelDriver.equalize_image(loaded_image_photo3)

        n_histogram_u0 = HistogramModelDriver.histogram(loaded_image_photo3)
        n_cdf_u0 = HistogramModelDriver.cdf(n_histogram_u0[0], loaded_image_photo3)

        PlotDriver.plot(n_histogram_u0, loaded_image_photo3, 'eq_')
        PlotDriver.plot(n_cdf_u0, loaded_image_photo3, 'eq_')

        # Сохраняем итоговое изображение
        ImageModelDriver.grayscale(loaded_image_photo3)
        ImageDisplayDriver.save(loaded_image_photo3)

        # ----------------------
        # Загружаем фото photo4.jpg
        # ----------------------

        loaded_image_photo4 = SPDImage.fromFile('lesson4/', 'photo4', '.jpg', np.uint8)

        # Обрабатываем
        # Считаем гистограммы
        histogram_photo4 = HistogramModelDriver.histogram(loaded_image_photo4)
        cdf_photo4 = HistogramModelDriver.cdf(histogram_photo4[0], histogram_photo4)

        PlotDriver.plot(histogram_photo4, loaded_image_photo4, 'original_')
        PlotDriver.plot(cdf_photo4, loaded_image_photo4, 'original_')

        # Эквализация гистограммы
        HistogramModelDriver.equalize_image(loaded_image_photo4)

        n_histogram_u0 = HistogramModelDriver.histogram(loaded_image_photo4)
        n_cdf_u0 = HistogramModelDriver.cdf(n_histogram_u0[0], loaded_image_photo4)

        PlotDriver.plot(n_histogram_u0, loaded_image_photo4, 'eq_')
        PlotDriver.plot(n_cdf_u0, loaded_image_photo4, 'eq_')

        # Сохраняем итоговое изображение
        ImageModelDriver.grayscale(loaded_image_photo4)
        ImageDisplayDriver.save(loaded_image_photo4)

        # ----------------------
        # Загружаем фото HollywoodLC.jpg
        # ----------------------

        loaded_image_HollywoodLC = SPDImage.fromFile('lesson4/', 'HollywoodLC', '.jpg', np.uint8)

        # Обрабатываем
        # Считаем гистограммы
        histogram_HollywoodLC = HistogramModelDriver.histogram(loaded_image_HollywoodLC)
        cdf_HollywoodLC = HistogramModelDriver.cdf(histogram_HollywoodLC[0], loaded_image_HollywoodLC)

        PlotDriver.plot(histogram_HollywoodLC, loaded_image_HollywoodLC, 'original_')
        PlotDriver.plot(cdf_HollywoodLC, loaded_image_HollywoodLC, 'original_')

        # Эквализация гистограммы
        HistogramModelDriver.equalize_image(loaded_image_HollywoodLC)

        n_histogram_u0 = HistogramModelDriver.histogram(loaded_image_HollywoodLC)
        n_cdf_u0 = HistogramModelDriver.cdf(n_histogram_u0[0], loaded_image_HollywoodLC)

        PlotDriver.plot(n_histogram_u0, loaded_image_HollywoodLC, 'eq_')
        PlotDriver.plot(n_cdf_u0, loaded_image_HollywoodLC, 'eq_')

        # Сохраняем итоговое изображение
        ImageModelDriver.grayscale(loaded_image_HollywoodLC)
        ImageDisplayDriver.save(loaded_image_HollywoodLC)


