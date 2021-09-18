class ModelDriver:

    @staticmethod
    def trend(models):
        x_array = []
        y_array = []
        previous_y = None
        previous_x = 0

        for model in models:
            trend_data = model.trend(previous_x, previous_y)

            x_array += trend_data[0]
            y_array += trend_data[1]
            previous_x = x_array[-1]
            previous_y = y_array[-1]

        return [x_array, y_array]

    @staticmethod
    def add(f_data, s_data):
        x_array = f_data[0]
        y_array = [x + y for x, y in zip(f_data[1], s_data[1])]

        return [x_array, y_array]

    @staticmethod
    def multi(f_data, s_data):
        x_array = f_data[0]
        y_array = [x * y for x, y in zip(f_data[1], s_data[1])]

        return [x_array, y_array]
