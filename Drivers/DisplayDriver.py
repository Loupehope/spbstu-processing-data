import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

matplotlib.use('TkAgg')


class DisplayDriver:

    def __init__(self, window):
        self.window = window
        self.fig = Figure(figsize=(8, 8))
        self.fig.subplots_adjust(wspace=0.5, hspace=0.5)
        self.plot_index = 1

    def plot(self, title, data, x_label="t", y_label="x(t)"):
        x_array = data[0]
        y_array = data[1]

        subplot = self.fig.add_subplot(2, 2, self.plot_index)
        subplot.plot(x_array, y_array)
        subplot.set_title(title)
        subplot.set_ylabel(y_label)
        subplot.set_xlabel(x_label)

        self.plot_index += 1

    def display(self):
        canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()