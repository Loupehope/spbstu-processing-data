# Models
from Models.AmpF import *
from Models.Filters import *

# Audio
from Audio.WAV import *

# Drivers
from Drivers.DisplayDriver import *
from Drivers.ModelDriver import *

# Display
import tkinter as tk


# Helpers
def get_window(title):
    info_window = tk.Tk()
    info_window.title(title)
    return info_window


random.seed(time.monotonic_ns())

# Устанавливаем окно и обьект графиков
window = tk.Tk()
window.title("Методы обработки экспериментальных данных")

display_model = DisplayDriver(window)
# display_model.fig.canvas.callbacks.connect('button_press_event', on_click)

# Считаем данные
file_path = "audio.wav"
rate, readed = WAV.read(file_path)
data = WAV.format(rate, readed)

# Буква О
# data_o = [data[0][10000:].copy(), data[1][10000:].copy()]
data_o = [data[0][14000:17000].copy(), data[1][14000:17000].copy()]

# Первый график
first = data_o

# Второй график
second = ModelDriver.convolution(first, Filters.bpw_filter(3200, 3600, 1 / rate, 64), 1)

# Третий график
third = AmpF.calc(first, 1 / rate, 1)
# WAV.write("audio_mod.wav", rate, third)
# Четвертый график
forth = AmpF.calc(second, 1 / rate, 1)

# Отрисовываем
display_model.plot("Исходная фонема ""О""", first, "t [ms]", "x(t)")
display_model.plot("Фонема ""О"" только с 4-й формантой", second, "t [ms]", "x(t)")
display_model.plot("Исходный спектр до 5000 Гц", [third[0][:600], third[1][:600]], "Гц", "")
display_model.plot("Новый спектр до 5000 Гц", [forth[0][:600], forth[1][:600]], "Гц", "")
# display_model.plot("Спектр до 3000 Гц", [second[0][:400], second[1][:400]], "Гц", "")

# Запускаем
display_model.display()
window.mainloop()
