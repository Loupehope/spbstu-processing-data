import math


class AmpF:

    @staticmethod
    def calc(data, dt, window=1):
        x_results = []
        y_results = []

        f_d = (1 / (2 * dt)) / (len(data[1]) / 2)
        f = -(1 / (2 * dt))

        half = int(len(data[1]) / 2)
        zeros_count = half * (1 - window)

        y_arr = data[1].copy()

        for i in range(half):
            if zeros_count > 0:
                y_arr[i] = 0
                y_arr[len(data[1]) - i - 1] = 0
                zeros_count -= 1
            else:
                break

        for j in range(-half, half):
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

        return [x_results[half + 1:], y_results[half + 1:]]

    @staticmethod
    def get_garmoniks_from(data, min):
        counter = 0
        for i in range(len(data[0])):
            if data[1][i] >= min:
                print("Гармоника " + str(counter) + "\n   Амплитуда: " + str(round(data[1][i] * 2)) + "\n   Частота: " +
                      str(round(data[0][i])))
                counter += 1

