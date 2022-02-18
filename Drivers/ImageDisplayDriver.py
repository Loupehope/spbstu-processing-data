from Models.SPDImage import *
from PIL import Image


class ImageDisplayDriver:

    @staticmethod
    def save(data: SPDImage, dtype=np.uint8):
        Image.fromarray(data.modified_image.astype(dtype)).save(data.folder + data.modified_name + data.extension)
