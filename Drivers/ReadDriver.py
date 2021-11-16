import numpy as np


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
