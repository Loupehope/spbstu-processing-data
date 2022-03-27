import numpy as np
import math
import numba
from Models.Fourier import *


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
    def one_d_fourier(data: np.ndarray, dt) -> Fourier:
        return Fourier(np.fft.fft(data), dt)

    @staticmethod
    def two_d_fourier(data: np.ndarray, dt) -> Fourier:
        return Fourier(np.fft.fft2(data), dt)

    @staticmethod
    def amplitude(data: np.ndarray, dt) -> Fourier:
        return AnalyzeModel.one_d_fourier(data, dt).amplitude()