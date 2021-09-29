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
    def trend(self, previous_x=None, previous_y=None):
        x_array = []
        y_array = []
        x = 0

        if previous_y is None:
            dy = 0
        else:
            dy = self.scale * self.b - previous_y

        if previous_x is None:
            previous_x = 0

        for i in range(self.n_from, self.n_to):
            y = self.scale * random.uniform(self.a, self.b)
            x_array.append(x + previous_x)
            y_array.append(y - dy)
            x += self.dt

        return [x_array, y_array]