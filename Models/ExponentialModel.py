import math


class ExponentialModel:
    @staticmethod
    def name(): return "Экспоненциальный"

    @staticmethod
    def trend(a, b, m=1, n=1000, dt=1):
        x_array = []
        y_array = []
        x = 0

        for i in range(n):
            y = b * math.exp(-a * x)
            x_array.append(x)
            y_array.append(y)
            x += dt

        return [x_array, y_array]
