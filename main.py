# Models
from Models.AmpF import *

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

# Первый график
first = data

# Второй график
# second = AmpF.calc(data, 1 / rate, 1)

# Третий график
third = WAV.volume(0.1, data)
WAV.write("audio_mod.wav", rate, third)
# Четвертый график

# Отрисовываем
display_model.plot("Сигнал", first, "t", "x(t)")
# display_model.plot("Спектр офильтрованных данных", second, "Гц", "")
display_model.plot("Измененный сигнал", third, "t", "x(t)")
# display_model.plot("Веса фильтра", forth, "[index]", "")

# Запускаем
display_model.display()
window.mainloop()
