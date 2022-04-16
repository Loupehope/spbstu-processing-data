import numpy as np
from PIL import Image


class Fourier:

    def __init__(self, complex_data, dt: int):
        self.complex_data = complex_data
        self.dt = dt

    def amplitude(self):
        data_y = np.abs(self.complex_data * self.dt)

        data_x = np.fft.fftfreq(len(self.complex_data), self.dt)
        zero_index = data_x.tolist().index(np.max(data_x))

        return np.array([data_x[:zero_index], data_y[:zero_index]])

    def one_d_back_transform(self):
        data_y = np.fft.ifft(self.complex_data).real
        data_x = np.arange(len(data_y)) * self.dt

        return np.array([data_x, data_y])

    def two_d_back_transform(self):
        return np.abs(np.fft.ifft2(self.complex_data))

    def upscale(self, a):
        scale = float((a * 100) % 100) / 100

        FT = np.fft.fftshift(self.complex_data)
        vertical_padding = int(scale * self.complex_data.shape[0] / 2)
        horizontal_padding = int(scale * self.complex_data.shape[1] / 2)

        FT = np.pad(FT, [(vertical_padding, vertical_padding), (horizontal_padding, horizontal_padding)])

        return np.abs(np.fft.ifft2(np.fft.ifftshift(FT)))



