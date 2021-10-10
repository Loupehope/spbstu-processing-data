import numpy as np


class AnalyzeModel:

    def __init__(self, data, stationarity_m=10):
        self.data_x = data[0]
        self.data_y = data[1]
        self.fmin = self.min()
        self.fmax = self.max()
        self.fmean = self.mean()
        self.fvar = self.var()
        self.fstd = self.std()
        self.fmean_sq = self.mean_sq()
        self.fmean_sq_err = self.mean_sq_err()
        self.fasym = self.asym()
        self.fasym_coef = self.asym_coef()
        self.fexc = self.exc()
        self.fexc_coef = self.exc_coef()
        self.stationarity = self.calc_stationarity(stationarity_m)

    def min(self):
        return np.min(self.data_y)

    def max(self):
        return np.max(self.data_y)

    # Мат. ожидание
    def mean(self):
        return np.mean(self.data_y)

    # Дисперсия
    def var(self):
        return np.var(self.data_y)

    # Стандартное отклонение
    def std(self):
        return np.std(self.data_y)

    # Средний квадрат
    def mean_sq(self):
        sq_array = [i ** 2 for i in self.data_y]
        return np.mean(sq_array)

    # Средний квадрат ошибки
    def mean_sq_err(self):
        return self.fmean_sq ** 0.5

    # Ассимметрия - момент 3 п-ка
    def asym(self):
        sq_array = [(i - self.fmean) ** 3 for i in self.data_y]
        return np.mean(sq_array)

    # Ассимметрия коэф. - а > 0 - сдвиг влево, а < 0 - сдвиг вправо
    def asym_coef(self):
        return self.fasym / (self.fstd ** 3)

    # Эксцесс - момент 4 п-ка
    def exc(self):
        sq_array = [(i - self.fmean) ** 4 for i in self.data_y]
        return np.mean(sq_array)

    # Коэффициент эксцесса - а > 0 - пологая, а < 0 - крутая
    def exc_coef(self):
        return (self.fexc / (self.fstd ** 4)) - 3

    # Стационарность
    def calc_stationarity(self, m):
        if m is None:
            return False

        sub_arrays = np.split(np.array(self.data_y), m)
        analyzes = []

        stationarity = True

        for i in sub_arrays:
            model = AnalyzeModel([[], i], None)
            analyzes.append([model.fmean, model.fvar])

        def in_range(f, s):
            return abs(s/f) < 1.1

        for i in analyzes:
            for j in analyzes:
                if i == j:
                    continue
                else:
                    min_mean = min(i[0], j[0])
                    min_var = min(i[1], j[1])
                    max_mean = max(i[0], j[0])
                    max_var = max(i[1], j[1])
                    stationarity &= in_range(min_mean, max_mean) & in_range(min_var, max_var)

        return stationarity

    # Автокорреляционная функция
    def auto_corr_array(self):
        auto_array = []

        def auto_corr(shift):
            auto_corr_value = 0

            for j in range(len(self.data_y) - shift):
                temp = (self.data_y[j] - self.fmean) * (self.data_y[j + shift] - self.fmean)
                auto_corr_value = auto_corr_value + temp
            return round(auto_corr_value / (self.fvar * len(self.data_y)), 3)

        for i in range(len(self.data_y)):
            auto_array.append(auto_corr(i))

        return [self.data_x, auto_array]

    def n_auto_corr_array(self):
        auto_array = []

        def auto_corr(shift):
            auto_corr_value = 0

            for j in range(len(self.data_y) - shift):
                temp = (self.data_y[j] - self.fmean) * (self.data_y[j + shift] - self.fmean)
                auto_corr_value = auto_corr_value + temp
            return round(auto_corr_value / len(self.data_y), 3)

        for i in range(len(self.data_y)):
            auto_array.append(auto_corr(i))

        return [self.data_x, auto_array]

    # -------------------
    # Вывод информации о тренде
    def full_info(self):
        if self.stationarity:
            is_stationarity = "да"
        else:
            is_stationarity = "нет"

        return "Мин: " + str(round(self.fmin, 3)) + "\n" + \
            "Мах: " + str(round(self.fmax, 3)) + "\n" + \
            "Мат. ожидание: " + str(round(self.fmean, 3)) + "\n" + \
            "Дисперсия: " + str(round(self.fvar, 3)) + "\n" \
            "Стандартное отклонение: " + str(round(self.fstd, 3)) + "\n" + \
            "Средний квадрат: " + str(round(self.fmean_sq, 3)) + "\n" + \
            "Средний квадрат ошибки: " + str(round(self.fmean_sq_err, 3)) + "\n" + \
            "Ассимметрия: " + str(round(self.fasym, 3)) + "; Ассимметрия коэф.: " + str(round(self.fasym_coef, 3)) + "\n" +  \
            "Эксцесс: " + str(round(self.fexc, 3)) + "; Эксцесс коэф.: " + str(round(self.fexc_coef, 3)) + "\n" + \
            "Стационарный: " + is_stationarity + "\n"
