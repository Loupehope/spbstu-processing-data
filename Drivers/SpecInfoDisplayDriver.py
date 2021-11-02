import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import tkinter as tk

matplotlib.use('TkAgg')


class SpecInfoDisplayDriver:

    def __init__(self, window):
        self.window = window
        self.fig = Figure()
        self.fig.subplots_adjust(wspace=0.5, hspace=0.5)
        self.plot_index = 1
        self.size = self.fig.get_size_inches() * self.fig.dpi

    def plot(self, data, title="", x_label="t", y_label="x(t)"):
        x_array = data[0]
        y_array = data[1]

        subplot = self.fig.add_subplot(2, 1, self.plot_index)
        subplot.plot(x_array, y_array)
        subplot.set_title(title)
        subplot.set_ylabel(y_label)
        subplot.set_xlabel(x_label)

        self.plot_index += 1

    def hist(self, data, title="", x_label="t", y_label="x(t)"):
        y_array = data

        subplot = self.fig.add_subplot(2, 1, self.plot_index)
        subplot.hist(y_array, bins=20, density=True)
        subplot.set_title(title)
        subplot.set_ylabel(y_label)
        subplot.set_xlabel(x_label)

        self.plot_index += 1

    def draw_info(self, info_value):
        info_label = tk.Label(self.window, text=info_value, justify="left")
        info_label.pack()

    def display(self):
        canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()