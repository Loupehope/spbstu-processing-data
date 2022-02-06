import numpy as np
from PIL import Image


class SPDImage:

    def __init__(self, folder, name, extension):
        self.folder = folder
        self.name = name
        self.extension = extension
        self.modified_name = name
        self.counter = 0
        self.original_image = np.array(Image.open(folder + name + extension).convert('L'))
        self.modified_image = np.array(Image.open(folder + name + extension).convert('L'))
