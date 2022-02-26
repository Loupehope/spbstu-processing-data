import numpy as np
from PIL import Image


class SPDImage:

    def __init__(self, folder, name, extension, data, dtype):
        self.folder = folder
        self.name = name
        self.extension = extension
        self.modified_name = name
        self.counter = 0
        self.dtype = dtype
        self.original_image = np.array(data, copy=True)
        self.modified_image = np.array(data, copy=True)

    @classmethod
    def fromFile(cls, folder, name, extension, dtype):
        return cls(folder, name, extension, np.array(Image.open(folder + name + extension).convert('L')), dtype)

    def update(self, new_data, suffix_name):
        self.modified_image = new_data
        self.counter += 1
        self.modified_name = self.name + '_' + str(self.counter) + suffix_name
