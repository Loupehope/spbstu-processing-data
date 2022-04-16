import numpy as np
from Models.SPDImage import *
import struct
from Drivers.ImageModelDriver import *

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
    def image_binary_read(folder, name, extension, dtype, width, height, offset, file_type='.xcr') -> SPDImage:
        with open(folder + name + file_type, mode='rb') as file:
            data = np.fromfile(file, dtype=dtype)[offset:].reshape(height, width)

        return SPDImage(folder, name, extension, data, dtype)

    @staticmethod
    def dat_image_binary_read(folder, name, extension, width, height) -> SPDImage:
        file = open(folder + name + '.dat', 'rb')
        data = []
        buffer = file.read(4)
        while buffer:
            [x] = struct.unpack('f', buffer)
            data.append(x)
            buffer = file.read(4)

        data = np.reshape(data, (height, width))
        return SPDImage(folder, name, extension, data, 'f')

    @staticmethod
    def data_binary_read(folder, name, file_type, dtype, height, width) -> np.ndarray:
        with open(folder + name + file_type, mode='rb') as file:
            data = np.fromfile(file, dtype=dtype).reshape(height, width)
        return np.array(data)
