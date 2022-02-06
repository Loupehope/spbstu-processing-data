from Models.SPDImage import *
from PIL import Image


class ImageDisplayDriver:

    @staticmethod
    def save(data: SPDImage):
        Image.fromarray(data.modified_image.astype(np.uint8)).save(data.folder + data.modified_name + data.extension)
