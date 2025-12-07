import numpy as np
import matplotlib.pyplot as plt


class AntennaPlot:
    def plot(self, antenna):
        theta = np.linspace(0, 2*np.pi, 360)
        pattern = antenna.pattern(theta)

        plt.figure(figsize=(6, 6))
        plt.polar(theta, pattern)
        plt.title(f"{type(antenna).__name__} Radiation Pattern")
        plt.show()
