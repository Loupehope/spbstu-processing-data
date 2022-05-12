from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Drivers.ReadDriver import *
from Drivers.HistogramModelDriver import *
from Drivers.PlotDriver import *
from PIL import Image, ImageFilter
import pythreshold.utils
import cv2

class ImageLesson13:

    @staticmethod
    def run():

        def enumerate_stones(image_sd: SPDImage) -> int:
            image_row, image_col = image_sd.modified_image.shape
            pad_height = 1
            pad_width = 1

            padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))
            padded_image[pad_height:-pad_height, pad_width:-pad_width] = image_sd.modified_image

            stones = 0
            
            for i in range(1, image_row + 2, 1):
                for j in range(1, image_col + 2, 1):
                    if padded_image[i][j] == 0:
                        continue

                    is_stone = padded_image[i - 1][j - 1]
                    is_stone += padded_image[i - 1][j]
                    is_stone += padded_image[i - 1][j + 1]
                    
                    is_stone += padded_image[i][j - 1]
                    is_stone += padded_image[i][j + 1]
                    
                    is_stone += padded_image[i + 1][j - 1]
                    is_stone += padded_image[i + 1][j]
                    is_stone += padded_image[i + 1][j + 1]

                    if is_stone == 0:
                        stones += 1
                    
            return stones

        loaded_image = SPDImage.fromFile('lesson13/', 'stones', '.jpg', np.uint8)
        erosion_level = 6

        # ImageModelDriver.gamma_correction(loaded_image, 1, 2)
        # ImageModelDriver.grayscale(loaded_image)
        # ImageDisplayDriver.save(loaded_image)
        # ImageModelDriver.threshold(loaded_image, 50)

        ImageModelDriver.otsu(loaded_image)

        ImageDisplayDriver.save(loaded_image)
        ImageModelDriver.erode(loaded_image, erosion_level)
        ImageDisplayDriver.save(loaded_image)
        
        stones = enumerate_stones(loaded_image)

        print(stones)
