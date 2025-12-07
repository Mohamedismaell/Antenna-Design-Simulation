import numpy as np
import matplotlib.pyplot as plt


class AntennaPlot:

    def plot(self, antenna_name):

        theta = np.linspace(0, 2*np.pi, 360)

        if antenna_name in ["Dipole", "FoldedDipole", "Monopole", "Loop"]:
            pattern = np.abs(np.sin(theta))
            title = f"{antenna_name} Radiation Pattern"

        elif antenna_name in ["Discone", "CellSite"]:
            pattern = np.ones(360)
            title = f"{antenna_name} Radiation Pattern"

        else:
            pattern = np.abs(np.cos(theta))**4
            title = f"{antenna_name} Radiation Pattern"

        plt.figure()
        plt.polar(theta, pattern)
        plt.title(title)
        plt.show()
