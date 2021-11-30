import random
import time
import numpy as np
from Models.RandomModel import *
from Analyze.AnalyzeModel import *

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

    @staticmethod
    def shift(data, c):
        x_array = data[0]
        y_array = [y + c for y in data[1]]

        return [x_array, y_array]

    @staticmethod
    def anti_shift(data):
        c = np.mean(data[1])

        return ModelDriver.shift(data, -c)

    @staticmethod
    def spikes(data, count, anchor, shift):
        spike_x = []
        x_array = data[0]
        y_array = data[1]

        for i in range(count):
            n = random.randint(0, len(data[0]))

            if not spike_x.__contains__(n):
                spike_x.append(n)
                sign = random.randint(0, 50)
                value = anchor + (random.uniform(-shift, shift))
                if sign > 25:
                    y_array[n] = value
                else:
                    y_array[n] = -value
        return [x_array, y_array]

    @staticmethod
    def anti_spikes(data, min_q, max_q):
        x_array = data[0]
        y_array = data[1]

        for i in range(len(y_array)):
            left_val = 0
            right_val = 0

            try:
                left_val = y_array[i - 1]
            except:
                left_val = y_array[i + 1]

            try:
                right_val = y_array[i + 1]
            except:
                right_val = y_array[i - 1]

            medium = (right_val + left_val) / 2

            if y_array[i] < min_q or y_array[i] > max_q:
                y_array[i] = medium

        return [x_array, y_array]

    @staticmethod
    def anti_trend(data, l=10):
        x_array = data[0]
        y_array = data[1]
        new_y_array = []

        max = len(y_array) - l

        for i in range(max):
            y_i = 0
            for j in range(i, i + l):
                y_i += y_array[j]
            y_i = y_i / l
            new_y_array.append(y_i)

        for i in range(l):
            y_i = 0
            for j in range(i, i + l):
                y_i += y_array[len(y_array) - j - 1]
            y_i = y_i / l
            new_y_array.append(y_i)

        for i in range(len(y_array)):
            new_y_array[i] = y_array[i] - new_y_array[i]

        return [x_array, new_y_array]

    @staticmethod
    def rand_collect():
        x_array = []
        y_array = []
        aver_y_array = []
        res_x_array = [0]
        res_y_array = []

        for i in range(1000):
            x_array.append(i)
            y_array.append(0)

        for i in range(0, 10000, 10):
            for j in range(i, i + 10):
                new_values = RandomModel(-100, 100, 0, 1000, 1).trend()
                y_array = [x + y for x, y in zip(y_array, new_values[1])]

                if i == 0 and j == 0:
                    analize = AnalyzeModel([x_array, y_array])
                    res_y_array.append(1)
                    print("Ст. отклонение " + str(i) + ": " + str(round(analize.fstd, 3)))

            for k in range(len(y_array)):
                aver_y_array.append(y_array[k] / (i + 10))

            analize = AnalyzeModel([x_array, aver_y_array])
            res_y_array.append(res_y_array[0] / analize.fstd)
            res_x_array.append(i + 10)
            print("Ст. отклонение " + str(i + 10) + ": " + str(round(analize.fstd, 3)))
            aver_y_array = []

        return [res_x_array[1:], res_y_array[1:]]

    @staticmethod
    def trend_collect(data, a, b, dt):
        x_array = data[0]
        y_array = []
        aver_y_array = []
        res_y_array = []

        for i in range(len(data[0])):
            y_array.append(0)

        for i in range(0, 10000, 10):
            for j in range(i, i + 10):
                new_values = RandomModel(-a, b, 0, len(data[0]), dt).trend()
                temp_y_array = [x + y for x, y in zip(data[1], new_values[1])]
                y_array = [x + y for x, y in zip(y_array, temp_y_array)]

            for k in range(len(y_array)):
                aver_y_array.append(y_array[k] / (i + 10))

            res_y_array = aver_y_array.copy()
            aver_y_array = []

        return [x_array, res_y_array]

    @staticmethod
    def convolution(main_data, add_data, dt):
        x_array = []
        y_array = []

        for i in range(len(main_data[1]) + len(add_data[1])):
            sum = 0

            for j in range(len(add_data[1])):
                if range(len(main_data[1])).__contains__(i - j):
                    sum += main_data[1][i - j] * add_data[1][j]
                else:
                    sum += 0

            if (len(add_data[1]) / 2) <= i <= (len(main_data[1]) + len(add_data[1]) / 2):
                y_array.append(sum)
                x_array.append((i - len(add_data[1]) / 2) * dt)

        return [x_array, y_array]
