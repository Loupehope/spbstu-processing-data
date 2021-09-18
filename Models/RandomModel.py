import random


class RandomModel:

    # Initialization
    def __init__(self, a, b, n_from, n_to, scale=1, dt=1):
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
            y = self.scale * random.uniform(self.a, self.b)
            x_array.append(x)
            y_array.append(y)
            x += self.dt

        return [x_array, y_array]