import matplotlib.pyplot as plt
from Models.SPDImage import *
import os


class PlotDriver:

    @staticmethod
    def plot(data: (list, str), spd_image: SPDImage, suffix='', sub_folder='plots'):
        plt.plot(data[0])

        folder_path = spd_image.folder + sub_folder + '_' + spd_image.name + '/'

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        plt.savefig(folder_path + suffix + spd_image.name + data[1] + '.jpg')
        plt.clf()

    @staticmethod
    def plot_raw(data, folder: str, name: str):
        plt.plot(data[0], data[1])

        if not os.path.exists(folder):
            os.makedirs(folder)

        plt.savefig(folder + name + '.jpg')
        plt.clf()
