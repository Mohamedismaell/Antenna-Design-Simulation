from antenna_base import Antenna
import numpy as np


class Yagi(Antenna):
    def length(self):
        return self.wavelength() / 2

    def directivity(self):
        return 8

    def pattern(self, theta):
        return np.cos(theta) ** 4


class Helical(Antenna):
    def length(self):
        return self.wavelength()

    def directivity(self):
        return 10

    def pattern(self, theta):
        return np.cos(theta) ** 2


class Parabolic(Antenna):
    def length(self):
        return self.wavelength() * 3

    def directivity(self):
        return 25

    def pattern(self, theta):
        return np.exp(-(theta / 0.2) ** 2)


class Horn(Antenna):
    def length(self):
        return self.wavelength() * 2

    def directivity(self):
        return 15

    def pattern(self, theta):
        return np.cos(theta) ** 3


class CellSite(Antenna):
    def length(self):
        return self.wavelength() / 2

    def directivity(self):
        return 12

    def pattern(self, theta):
        return np.where(np.abs(theta) < np.pi/4, 1, 0)


class Microstrip(Antenna):
    def length(self):
        return self.wavelength() / 2.5

    def directivity(self):
        return 6

    def pattern(self, theta):
        return np.cos(theta) ** 2
