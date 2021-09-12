class LinearModel:
    @staticmethod
    def name(): return "Линейный"

    @staticmethod
    def trend(a, b, m=1, n=1000, dt=1):
        x_array = []
        y_array = []
        x = 0

        for i in range(n):
            y = a * x + b
            x_array.append(x)
            y_array.append(y)
            x += dt

        return [x_array, y_array]