import math
import numpy as np


class Filters:


    # низкочастотный фильтр
    # f - частота
    # dt - шаг
    # m - длиннее - более крутой склон, короче - более пологий склон
    @staticmethod
    def lpw_filter(f, dt, m, return_with_minus=True):
        window = [0.35577019, 0.2436983, 0.07211497, 0.00630165]

        factor = 2 * f * dt
        right_y_results = [factor]
        arg = factor * math.pi

        for i in range(1, m + 1):
            right_y_results.append(math.sin(arg * i) / (math.pi * i))

        right_y_results[m] /= 2.0

        sumg = right_y_results[0]

        for i in range(1, m + 1):
            sums = window[0]
            arg = math.pi * i / m
            for k in range(1, 4):
                sums += 2.0 * window[k] * math.cos(arg * k)
            right_y_results[i] *= sums
            sumg += 2.0 * right_y_results[i]

        for i in range(m + 1):
            right_y_results[i] /= sumg

        right_x_results = []
        x = 0
        for i in range(len(right_y_results)):
            right_x_results.append(x)
            x += 1

        if not return_with_minus:
            return [right_x_results, right_y_results]

        left_y_results = []
        left_x_results = []
        for i in range(0, len(right_y_results)):
            left_y_results.append(right_y_results[len(right_y_results) - 1 - i])
            left_x_results.append(right_x_results[len(right_y_results) - 1 - i] * -1.0)

        return [left_x_results[:len(right_y_results) - 1] + right_x_results,
                left_y_results[:len(right_y_results) - 1] + right_y_results]

    # фильтр высоких частот
    # f - частота
    # dt - шаг
    # m - длиннее - более крутой склон, короче - более пологий склон
    @staticmethod
    def hpw_filter(f, dt, m):
        values = Filters.lpw_filter(f, dt, m, True)

        for k in range(len(values[0])):
            if k == m:
                values[1][k] = 1.0 - values[1][k]
            else:
                values[1][k] = -values[1][k]

        return values

    # полосовой фильтр
    # f1, f2 - частоты
    # dt - шаг
    # m - длиннее - более крутой склон, короче - более пологий склон
    @staticmethod
    def bpw_filter(f1, f2, dt, m):
        values1 = Filters.lpw_filter(f1, dt, m, True)
        values2 = Filters.lpw_filter(f2, dt, m, True)

        for k in range(len(values1[0])):
            values1[1][k] = values2[1][k] - values1[1][k]

        return values1

    # режекторный фильтр
    # f1, f2 - частоты
    # dt - шаг
    # m - длиннее - более крутой склон, короче - более пологий склон
    @staticmethod
    def bsw_filter(f1, f2, dt, m):
        values1 = Filters.lpw_filter(f1, dt, m, True)
        values2 = Filters.lpw_filter(f2, dt, m, True)

        for k in range(len(values1[0])):
            if k == m:
                values1[1][k] = 1.0 + values1[1][k] - values2[1][k]
            else:
                values1[1][k] = values1[1][k] - values2[1][k]

        return values1

    @staticmethod
    def normalized(values, m):
        for k in range(len(values[0])):
            values[1][k] *= 2 * m + 1
        return values
