import math
import numpy as np


class Cardio:

    # Initialization
    def __init__(self, a, b, n_from, n_to, scale=100, dt=1):
        self.a = a
        self.b = b
        self.scale = scale
        self.dt = dt
        self.n_from = n_from
        self.n_to = n_to

    # Trend
    def trend(self):
        x_array = []
        y_array = []
        x = 0

        for i in range(self.n_from, self.n_to):
            y = self.scale * math.sin(2 * math.pi * self.b * x) * math.exp(-self.a * x)
            x_array.append(x)
            y_array.append(y)
            x += self.dt

        max = np.max(y_array)

        for i in range(self.n_from, self.n_to):
            y_array[i] = y_array[i] / max

        return [x_array, y_array]
