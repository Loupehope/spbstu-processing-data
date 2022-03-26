from Models.SPDImage import *
from PIL import Image
import os

class ImageDisplayDriver:

    @staticmethod
    def save(data: SPDImage, dtype=np.uint8):
        if not os.path.exists(data.modified_folder):
            os.makedirs(data.modified_folder)

        Image.fromarray(data.modified_image.astype(dtype)).save(data.modified_folder + data.modified_name + data.extension)
