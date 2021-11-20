import math


class Impuls:

    # Initialization
    def __init__(self, impulses: {int: int}, n_from, n_to, scale=1, dt=1):
        self.impulses = impulses
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
            dy = self.scale - previous_y

        for i in range(self.n_from, self.n_to):
            if self.impulses.get(i) is not None:
                y = self.impulses.get(i)
            else:
                y = 0
            x_array.append(x + previous_x)
            y_array.append(y - dy)
            x += self.dt

        return [x_array, y_array]