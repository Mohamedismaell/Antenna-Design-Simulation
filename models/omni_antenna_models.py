import numpy as np
from antenna_base import Antenna

# -------- Omni / Wire Antennas --------


class Dipole(Antenna):

    def length(self):
        return self.wavelength() / 2

    def directivity(self):
        return 1.64

    def pattern(self, theta, degrees=False):

        if degrees:
            theta = np.radians(theta)
        raw = np.abs(np.sin(theta))
        return raw * self.efficiency()


class FoldedDipole(Antenna):

    def length(self):
        return self.wavelength() / 2

    def directivity(self):
        return 1.7

    def pattern(self, theta, degrees=False):
        if degrees:
            theta = np.radians(theta)
        return np.abs(np.sin(theta)) * self.efficiency()


class Monopole(Antenna):

    def length(self):
        return self.wavelength() / 4

    def directivity(self):
        return 1.5

    def pattern(self, theta, degrees=False):

        if degrees:
            theta = np.radians(theta)
        return np.abs(np.sin(theta)) * self.efficiency()


class Loop(Antenna):

    def length(self):
        return self.wavelength()

    def directivity(self):
        return 1.2

    def pattern(self, theta, degrees=False):
        if degrees:
            theta = np.radians(theta)
        raw = np.sin(theta)**2
        return raw * self.efficiency()


class Discone(Antenna):

    def length(self):
        return self.wavelength() / 4

    def directivity(self):
        return 1.1

    def pattern(self, theta, degrees=False):

        if degrees:
            theta = np.radians(theta)
        return np.ones_like(theta) * self.efficiency()
