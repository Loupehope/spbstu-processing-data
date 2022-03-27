from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Drivers.PlotDriver import *
from Models.Cardio import *

class ImageLesson7:

    @staticmethod
    def run():
        folder = 'lesson7/'

        # ----------------------
        # Берем кардиограмму и строим её графики
        # ----------------------

        cardio_data = Cardio(10, 4, 0, 200, 1, 0.005).trend()
        PlotDriver.plot_by_x_and_y(cardio_data, folder + 'cardio/', 'cardio')

        cardio_one_d_fourier = AnalyzeModel.one_d_fourier(cardio_data[1], 0.005)
        PlotDriver.plot_by_x_and_y(cardio_one_d_fourier.amplitude(), folder + 'cardio/', 'one_d_fourier_amps')

        back_cardio_one_d_fourier = cardio_one_d_fourier.one_d_back_transform()
        PlotDriver.plot_by_x_and_y(back_cardio_one_d_fourier, folder + 'cardio/', 'back_one_d_fourier')

        # ----------------------
        # Берем grace.jpg
        # ----------------------

        loaded_image_grace = SPDImage.fromFile('lesson7/', 'grace', '.jpg', np.uint8)

        grace_two_d_fourier = AnalyzeModel.two_d_fourier(loaded_image_grace.modified_image, 1)

        back_grace_two_d_fourier = grace_two_d_fourier.two_d_back_transform()
        loaded_image_grace.modified_folder = loaded_image_grace.modified_folder + 'grace/'
        loaded_image_grace.update(back_grace_two_d_fourier, '_back_two_d_fourier')

        ImageDisplayDriver.save(loaded_image_grace)

        back_grace_two_d_fourier = grace_two_d_fourier.upscale(1.5)
        loaded_image_grace.update(back_grace_two_d_fourier, '_upscale_two_d_fourier')
        ImageDisplayDriver.save(loaded_image_grace)


