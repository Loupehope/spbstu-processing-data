class Windows:

    @staticmethod
    def calc(count, dt, left, right):
        right_x_results = []
        right_y_results = []
        x = 0

        for i in range(int(count / 2)):
            if i < left or i > right:
                right_y_results.append(0)
            else:
                right_y_results.append(1)
            right_x_results.append(x)
            x += dt

        left_y_results = []
        left_x_results = []
        for i in range(0, len(right_y_results)):
            left_y_results.append(right_y_results[len(right_y_results) - 1 - i])
            left_x_results.append(right_x_results[len(right_y_results) - 1 - i] * -1.0)

        return [left_x_results + right_x_results, left_y_results + right_y_results]
