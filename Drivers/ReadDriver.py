import numpy as np
from Models.SPDImage import *

class ReadDriver:

    @staticmethod
    def read(file, dtype):
        x_array = []
        y_array = []
        data = np.fromfile(file, dtype)

        for i in range(len(data)):
            x_array.append(i * 0.002)
            y_array.append(data[i])
        return [x_array, y_array]

    @staticmethod
    def image_binary_read(folder, name, extension, dtype, width, height, offset) -> SPDImage:
        with open(folder + name + '.xcr', mode='rb') as file:
            data = np.fromfile(file, dtype=dtype)[offset:].reshape(height, width)

        return SPDImage(folder, name, extension, data, dtype)
