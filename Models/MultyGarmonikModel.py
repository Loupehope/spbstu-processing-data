class MultyGarmonikModel:

    @staticmethod
    def trend(models):
        x_array = []
        y_array = []

        for model in models:
            x_array = model[0]
            if len(y_array) == 0:
                y_array = model[1]
            else:
                y_array = [x + y for x, y in zip(y_array, model[1])]

        return [x_array, y_array]
