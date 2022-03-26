import numpy as np
from PIL import Image


class SPDImage:

    def __init__(self, folder, name, extension, data, dtype):
        self.folder = folder
        self.modified_folder = folder
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
        self.modified_image = np.array(new_data, copy=True)
        self.counter += 1
        self.modified_name = self.name + '_' + str(self.counter) + suffix_name

    def max_type_colors_count(self) -> int:
        return np.iinfo(self.dtype).max + 1

    def reset(self):
        self.modified_image = np.array(self.original_image, copy=True)
        self.modified_name = self.name

    def copy(self):
        return SPDImage(self.folder, self.name, self.extension, np.array(self.modified_image, copy=True), self.dtype)
