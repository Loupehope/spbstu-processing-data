import numpy as np
import math
import numba


class AnalyzeModel:

    @staticmethod
    @numba.jit(nopython=True)
    def diff(data, dx=1):
        return np.diff(data) / dx

    @staticmethod
    @numba.jit(nopython=True)
    def auto_corr_array(data: np.ndarray) -> np.ndarray:
        mean = np.mean(data)
        var = np.var(data)
        auto_array = []

        def auto_corr(shift):
            auto_corr_value = 0

            for j in range(len(data) - shift):
                temp = (data[j] - mean) * (data[j + shift] - mean)
                auto_corr_value = auto_corr_value + temp
            return round(auto_corr_value / (var * len(data)), 3)

        for i in range(len(data)):
            auto_array.append(auto_corr(i))

        return np.array(auto_array)

    # Взаимнокорреляционная функция
    @staticmethod
    @numba.jit(nopython=True)
    def mutual_corr_array(first: np.ndarray, second: np.ndarray) -> np.ndarray:
        mean_f = np.mean(first)
        mean_s = np.mean(second)
        count = len(first)
        auto_array = []

        def auto_corr(shift):
            auto_corr_value = 0
            for j in range(count - shift):
                temp = (first[j] - mean_f) * (second[j + shift] - mean_s)
                auto_corr_value = auto_corr_value + temp
            return round(auto_corr_value / count, 3)

        for i in range(count):
            auto_array.append(auto_corr(i))

        return np.array(auto_array)

    @staticmethod
    @numba.jit(nopython=True)
    def fourier(data: np.ndarray, dt: int) -> np.ndarray:
        x_results = []
        y_results = []

        f_d = (1 / (2 * dt)) / (len(data) / 2)
        f = 0

        half = int(len(data) / 2)
        y_arr = data.copy()

        for j in range(0, half):
            re = 0
            im = 0

            for i in range(len(y_arr)):
                re += y_arr[i] * math.cos(2 * math.pi * j * i / len(y_arr))
                im += y_arr[i] * math.sin(2 * math.pi * j * i / len(y_arr))

            re /= len(y_arr)
            im /= len(y_arr)

            x_results.append(f)
            f += f_d
            y_results.append(math.sqrt(re ** 2 + im ** 2))

        return np.array([x_results, y_results])
