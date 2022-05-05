from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Drivers.ReadDriver import *

class ImageLesson8:

    @staticmethod
    def run():
        folder = 'lesson8/'

        # ----------------------
        # Берем kernL64_f4
        # ----------------------

        kernL64_f4 = ReadDriver.data_binary_read(
            folder, 'kernL64_f4', '.dat', "float32", 1, 64
        )

        # ----------------------
        # Берем blur259x185L
        # ----------------------

        loaded_image_blur259x185L = ReadDriver.dat_image_binary_read(
            folder, 'blur259x185L', '.jpg', 259, 185
        )

        ImageDisplayDriver.save(loaded_image_blur259x185L)
        ImageModelDriver.blur_fix(loaded_image_blur259x185L, kernL64_f4, 0)
        ImageDisplayDriver.save(loaded_image_blur259x185L)

        # ----------------------
        # Берем blur259x185L_N
        # ----------------------

        loaded_image_blur259x185L = ReadDriver.dat_image_binary_read(
            folder, 'blur259x185L_N', '.jpg', 259, 185
        )

        ImageDisplayDriver.save(loaded_image_blur259x185L)
        ImageModelDriver.blur_fix(loaded_image_blur259x185L, kernL64_f4, 2)
        ImageDisplayDriver.save(loaded_image_blur259x185L)

