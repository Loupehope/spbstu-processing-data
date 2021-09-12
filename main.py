# Models
from Models.LinearModel import *
from Models.ExponentialModel import *

# Display
import tkinter as tk
from Drivers.DisplayDriver import *

# Устанавливаем окно и обьект графиков
window = tk.Tk()
window.title("Методы обработки экспериментальных данных")

display_model = DisplayDriver(window)

# Считаем данные
data_linear_up = LinearModel.trend(2, 3)
data_linear_down = LinearModel.trend(-1, 2)
data_exp_up = ExponentialModel.trend(-0.002, 0.001)
data_exp_down = ExponentialModel.trend(0.01, 0.001)

# Создаем графики
display_model.plot(LinearModel.name(), data_linear_up)
display_model.plot(ExponentialModel.name(), data_exp_up)
display_model.plot(LinearModel.name(), data_linear_down)
display_model.plot(ExponentialModel.name(), data_exp_down)

# Запускаем и отрисовываем
display_model.display()
window.mainloop()
