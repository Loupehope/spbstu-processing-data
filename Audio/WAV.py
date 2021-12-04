import scipy.io.wavfile


class WAV:

    @staticmethod
    def read(filename: str):
        return scipy.io.wavfile.read(filename)

    @staticmethod
    def write(filename, rate, data):
        scipy.io.wavfile.write(filename, rate, data[1])

    @staticmethod
    def format(rate, data):
        x_array = []
        dt = 1 / rate
        x = 0
        for i in range(len(data)):
            x_array.append(x)
            x += dt
        return  [x_array, data]

    @staticmethod
    def volume(amp, data):
        x_array = data[0].copy()
        y_array = data[1].copy()

        for i in range(len(y_array)):
            y_array[i] *= amp

        return [x_array, y_array]
