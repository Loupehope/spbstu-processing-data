import math


class ExponentialModel:

    @staticmethod
    def simplified(a, b, n, dt=1):
        return ExponentialModel(a, b, 1, dt, 0, n)

    # Initialization
    def __init__(self, a, b, n_from, n_to, scale=100, dt=1):
        self.a = a
        self.b = b
        self.scale = scale
        self.dt = dt
        self.n_from = n_from
        self.n_to = n_to

    # Trend
    def trend(self, previous_x, previous_y):
        x_array = []
        y_array = []
        x = 0

        if previous_y is None:
            dy = 0
        else:
            dy = self.scale * self.b - previous_y

        for i in range(self.n_from, self.n_to):
            y = self.scale * self.b * math.exp(-self.a * x)
            x_array.append(x + previous_x)
            y_array.append(y - dy)
            x += self.dt

        return [x_array, y_array]


