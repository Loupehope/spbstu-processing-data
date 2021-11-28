# Models
from Models.LinearModel import *
from Models.ExponentialModel import *
from Models.RandomModel import *
from Models.PrimitiveRandomModel import *
from Models.GarmonikModel import *
from Models.MultyGarmonikModel import *
from Models.AmpF import *
from Models.Cardio import *
from Models.Impuls import *
from Models.Filters import *

# Analyze
from Analyze.AnalyzeModel import *
from Analyze.MutualModel import *

# Drivers
from Drivers.ReadDriver import *
from Drivers.DisplayDriver import *
from Drivers.ModelDriver import *
from Drivers.SpecInfoDisplayDriver import *

# Display
import tkinter as tk


# Helpers
def get_window(title):
    info_window = tk.Tk()
    info_window.title(title)
    return info_window


def on_click(event):
    x = display_model.size[0] / 2
    y = display_model.size[1] / 2

    if event.inaxes is not None:
        spec_driver = SpecInfoDisplayDriver(tk.Tk())

        if event.x < x and event.y > y:
            spec_driver.window.title("First graph")
            spec_driver.draw_info(first_analyze.full_info())
            spec_driver.hist(first_analyze.data_y)
            spec_driver.plot(first_analyze.n_auto_corr_array())
        elif event.x > x and event.y > y:
            spec_driver.window.title("Second graph")
            spec_driver.draw_info(second_analyze.full_info())
            spec_driver.hist(second_analyze.data_y)
            spec_driver.plot(second_analyze.n_auto_corr_array())
        elif event.x < x and event.y < y:
            spec_driver.window.title("Third graph")
            spec_driver.draw_info(third_analyze.full_info())
            spec_driver.hist(third_analyze.data_y)
            spec_driver.plot(third_analyze.n_auto_corr_array())
        elif event.x > x and event.y < y:
            spec_driver.window.title("Forth graph")
            spec_driver.draw_info(forth_analyze.full_info())
            spec_driver.hist(forth_analyze.data_y)
            spec_driver.plot(forth_analyze.n_auto_corr_array())
        spec_driver.display()
        spec_driver.window.mainloop()


random.seed(time.monotonic_ns())

# Устанавливаем окно и обьект графиков
window = tk.Tk()
window.title("Методы обработки экспериментальных данных")

display_model = DisplayDriver(window)
display_model.fig.canvas.callbacks.connect('button_press_event', on_click)

# Считаем данные

# Первый график
# Poly Гармоника
# first = MultyGarmonikModel.trend([
#         GarmonikModel(10, 3, 0, 300, 1, 1 / 100).trend(0, 0),
#         GarmonikModel(100, 37, 0, 300, 1, 1 / 100).trend(0, 0),
#         GarmonikModel(15, 45, 0, 300, 1, 1 / 100).trend(0, 0)
#     ])

# Читаем
#
#
#
# first = ModelDriver().trend([
#     Impuls({200: 120, 400: 130, 600: 110}, 0, 1000, 1, 0.005)
# ])
# first = ReadDriver.read("pgp_float4_1000_2ms.dat", "float32")
first = Filters.lpw_filter(100, 0.002, 32)

# Второй график
# second = ModelDriver.trend([
#     Cardio(10, 4, 0, 200, 1, 0.005)
# ])
# ФНЧ
nomalized = Filters.normalized([first[0].copy(), first[1].copy()], 32)
second = AmpF.calc(nomalized, 0.002, 1)
#
# second = ModelDriver.spikes(second, 1, 2, 10**2)

# Третий график
third = AmpF.calc(first, 0.002, 1)


# Четвертый график
forth = AmpF.calc(second, 0.002, 1)
# AmpF.get_garmoniks_from(third, 4)

# Отрисовываем
display_model.plot("Potter LPF weights", first, "[index]", "")
display_model.plot("Potter LPF TF", second, "Гц", "")
display_model.plot("Кардиоограмма", third, "t", "y(t)")
display_model.plot("Спектр h", forth, "Гц", "|Xn|")

# Запускаем
display_model.display()
window.mainloop()
