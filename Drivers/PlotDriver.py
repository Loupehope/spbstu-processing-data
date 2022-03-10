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
