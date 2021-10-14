# Models
from Models.LinearModel import *
from Models.ExponentialModel import *
from Models.RandomModel import *
from Models.PrimitiveRandomModel import *
from Models.GarmonikModel import *
from Models.MultyGarmonikModel import *

# Analyze
from Analyze.AnalyzeModel import *
from Analyze.MutualModel import *

# Drivers
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

    spec_driver = SpecInfoDisplayDriver(tk.Tk())

    if event.inaxes is not None:
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
# Гармоника
first = MultyGarmonikModel.trend([
        GarmonikModel(10, 3, 0, 1000, 1, 1 / 1000).trend(0, 0),
        GarmonikModel(100, 37, 0, 1000, 1, 1 / 1000).trend(0, 0),
        GarmonikModel(15, 173, 0, 1000, 1, 1 / 1000).trend(0, 0)
    ])

# Тренд
# first = ModelDriver.trend([
#     ExponentialModel(0.01, 3, 0, 1000, 1000)
# ])

first = ModelDriver.spikes(ModelDriver.shift(first, -10), 5, 10 ** 3, 10 ** 1)
first_analyze = AnalyzeModel(first)

# Второй график
# Гармоника
second = ModelDriver.trend([
    GarmonikModel(10, 3, 0, 1000, 1, 1 / 1000)
])

# Тренд
# second = ModelDriver.trend([
#     ExponentialModel(0.01, 3, 0, 1000, 1000)
# ])
random = ModelDriver.trend([
    RandomModel(0, 10, 0, 1000, 100)
])
second = ModelDriver.add(random, second)
second = ModelDriver.spikes(ModelDriver.shift(second, 50), 4, 10 ** 3, 10 ** 1)
second_analyze = AnalyzeModel(second)

# Третий график
third = ModelDriver.trend([
    LinearModel(-1, 0, 0, 1000)
])
third = ModelDriver.add(random, third)
third = ModelDriver.spikes(ModelDriver.shift(third, 10), 3, 10 ** 3, 10 ** 1)
third_analyze = AnalyzeModel(third)

# Четвертый график
forth = MutualModel(first, second).mutual_corr_array()
forth_analyze = AnalyzeModel(forth)

# Отрисовываем
display_model.plot("First graph", first)
display_model.plot("Second graph", second)
display_model.plot("Third graph", third)
display_model.plot("Forth graph", forth)

# Запускаем
display_model.display()
window.mainloop()
