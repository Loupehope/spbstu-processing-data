from Analyze.AnalyzeModel import *


class MutualModel:

    def __init__(self, trend_f, trend_s):
        self.trend_f = AnalyzeModel(trend_f)
        self.trend_s = AnalyzeModel(trend_s)

    # Взаимнокорреляционная функция
    def mutual_corr_array(self):
        auto_array = []
        count = len(self.trend_f.data_y)

        def auto_corr(shift):
            auto_corr_value = 0
            for j in range(count - shift):
                temp = (self.trend_f.data_y[j] - self.trend_f.fmean) \
                       * (self.trend_s.data_y[j + shift] - self.trend_s.fmean)
                auto_corr_value = auto_corr_value + temp
            return round(auto_corr_value / count, 3)

        for i in range(count):
            auto_array.append(auto_corr(i))

        return [self.trend_f.data_x, auto_array]