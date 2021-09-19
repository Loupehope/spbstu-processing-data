# Models
from Models.LinearModel import *
from Models.ExponentialModel import *
from Models.RandomModel import *
from Models.PrimitiveRandomModel import *

# Drivers
from Drivers.DisplayDriver import *
from Drivers.ModelDriver import *

# Display
import tkinter as tk

# Устанавливаем окно и обьект графиков
window = tk.Tk()
window.title("Методы обработки экспериментальных данных")

display_model = DisplayDriver(window)

# Считаем данные

# Первый график
first = ModelDriver.trend([
    LinearModel(2, 3, 0, 200),
    LinearModel(-8, 0, 200, 500),
    LinearModel(1, 3, 500, 700),
    LinearModel(5, 3, 700, 1000)
])

first = ModelDriver.add(first, RandomModel(0, 1, 0, 1000, 1000).trend())

# Второй график
second = ModelDriver.trend([
    ExponentialModel(0.02, 2, 300, 600),
    LinearModel(-8, 0, 600, 650),
    LinearModel(1, 3, 650, 700),
    LinearModel(5, 3, 700, 1000)
])

second = ModelDriver.multi(second, PrimitiveRandomModel(0, 1, 0, 1000).trend())

# Третий график
third = ModelDriver.trend([
    LinearModel(2, 3, 0, 300),
    ExponentialModel(0.02, 2, 300, 600),
    LinearModel(5, 3, 600, 700),
    ExponentialModel(-0.02, 0.01, 700, 1000),
])

third = ModelDriver.add(third, RandomModel(0, 1, 0, 1000, 100).trend())

# Четвертый график
forth = ModelDriver.trend([
    ExponentialModel(0.02, 2, 0, 300),
    ExponentialModel(-0.02, 0.02, 300, 500),
    ExponentialModel(-0.02, 0.02, 500, 700),
    ExponentialModel(0.02, 4, 700, 1000),
])

forth = ModelDriver.multi(forth, RandomModel(0, 1, 0, 1000).trend())

display_model.plot("First graph", first)
display_model.plot("Second graph", second)
display_model.plot("Third graph", third)
display_model.plot("Forth graph", forth)

# Запускаем и отрисовываем
display_model.display()
window.mainloop()
