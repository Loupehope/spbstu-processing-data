# Models
from Models.LinearModel import *
from Models.ExponentialModel import *
from Models.RandomModel import *
from Models.PrimitiveRandomModel import *

# Analyze
from Analyze.AnalyzeModel import *

# Drivers
from Drivers.DisplayDriver import *
from Drivers.ModelDriver import *

# Display
import tkinter as tk


# Helpers
def draw_info(title, info_value):
    info_window = tk.Tk()
    info_window.title(title)
    info_label = tk.Label(info_window, text=info_value, justify="left")
    info_label.pack()
    info_window.mainloop()


def on_click(event):
    x = display_model.size[0] / 2
    y = display_model.size[1] / 2

    if event.inaxes is not None:
        if event.x < x and event.y > y:
            draw_info("First graph", first_analyze.full_info())
        elif event.x > x and event.y > y:
            draw_info("Second graph", second_analyze.full_info())
        elif event.x < x and event.y < y:
            draw_info("Third graph", third_analyze.full_info())
        elif event.x > x and event.y < y:
            draw_info("Forth graph", forth_analyze.full_info())


# Устанавливаем окно и обьект графиков
window = tk.Tk()
window.title("Методы обработки экспериментальных данных")

display_model = DisplayDriver(window)
display_model.fig.canvas.callbacks.connect('button_press_event', on_click)

# Считаем данные

# Первый график
first = ModelDriver.trend([
    LinearModel(1, 2, 0, 250), # Линейный восходящий
    LinearModel(-1, 2, 250, 500), # Линейный нисходящий
    ExponentialModel(-0.02, 0.01, 500, 750), # Экспонента восходящая
    ExponentialModel(0.02, 2, 750, 1000), # Экспонента нисходящая
])

# first = ModelDriver.multi(first, RandomModel(0, 1, 0, 1000).trend())
first_analyze = AnalyzeModel(first)

# Второй график
second = ModelDriver.trend([
    RandomModel(0, 1, 0, 450),  # Встроенный рандом
    LinearModel(0, 1, 450, 550),  # Разделитель
    PrimitiveRandomModel(0, 1, 550, 1000),  # Мой рандом
])

# second = ModelDriver.multi(second, PrimitiveRandomModel(0, 1, 0, 1000).trend())
second_analyze = AnalyzeModel(second)

# Третий график
third = ModelDriver.trend([
    LinearModel(2, 3, 0, 300),
    ExponentialModel(0.02, 2, 300, 600),
    LinearModel(5, 3, 600, 700),
    ExponentialModel(-0.02, 0.01, 700, 1000),
])
# third = ModelDriver.multi(third, RandomModel(0, 1, 0, 1000, 100).trend())
third = ModelDriver.add(third, RandomModel(0, 1, 0, 1000, 100).trend())
third_analyze = AnalyzeModel(third)

# Четвертый график
forth = ModelDriver.trend([
    RandomModel(0, 1, 0, 10000)
])

# forth = ModelDriver.multi(forth, RandomModel(0, 1, 0, 1000).trend())
forth_analyze = AnalyzeModel(forth)

# Отрисовываем
display_model.plot("First graph", first)
display_model.plot("Second graph", second)
display_model.plot("Third graph", third)
display_model.plot("Forth graph", forth)

# Запускаем
display_model.display()
window.mainloop()
