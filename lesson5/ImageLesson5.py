from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Drivers.ReadDriver import *
from Drivers.PlotDriver import *

from Analyze.AnalyzeModel import *
from Analyze.Filters import *


class ImageLesson5:

    @staticmethod
    def run():
        # ----------------------
        # Загружаем фото c12-85v.jpg
        # ----------------------

        loaded_image_c12_85v = SPDImage.fromFile('lesson5/', 'c12-85v', '.jpg', np.uint8)

        # Обрабатываем
        is_fixed = ImageModelDriver.fix_moire_for_image(
            loaded_image_c12_85v,
            ImageModelDriver.find_moire_for_image(loaded_image_c12_85v, 200)
        )

        # Сохраняем
        if is_fixed:
            ImageDisplayDriver.save(loaded_image_c12_85v)

        # ----------------------
        # Загружаем фото u0.jpg
        # ----------------------

        loaded_image_u0 = SPDImage.fromFile('lesson5/', 'u0', '.jpg', np.uint8)

        # Обрабатываем
        is_fixed = ImageModelDriver.fix_moire_for_image(
            loaded_image_u0,
            ImageModelDriver.find_moire_for_image(loaded_image_u0, 500)
        )

        # Сохраняем
        if is_fixed:
            ImageDisplayDriver.save(loaded_image_u0)



