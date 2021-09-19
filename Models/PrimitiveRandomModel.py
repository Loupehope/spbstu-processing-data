import time


class PrimitiveRandomModel:

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
            modulus = ((time.monotonic_ns() * 21448367) % 5343345) / 2147483647
            tik = modulus * 400

            y = self.scale * tik
            x_array.append(x)
            y_array.append(y)
            x += self.dt

        return [x_array, y_array]