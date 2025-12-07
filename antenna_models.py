from antenna_base import Antenna

# -------- Omni / Wire Antennas --------


class Dipole(Antenna):
    def length(self):
        return self.wavelength() / 2

    def directivity(self):
        return 1.64


class FoldedDipole(Antenna):
    def length(self):
        return self.wavelength() / 2

    def directivity(self):
        return 1.7


class Monopole(Antenna):
    def length(self):
        return self.wavelength() / 4

    def directivity(self):
        return 1.5


class Loop(Antenna):
    def length(self):
        return self.wavelength()

    def directivity(self):
        return 1.2


class Discone(Antenna):
    def length(self):
        return self.wavelength() / 4

    def directivity(self):
        return 1.1


# -------- Directive Antennas --------

class Yagi(Antenna):
    def length(self):
        return self.wavelength()

    def directivity(self):
        return 8


class Helical(Antenna):
    def length(self):
        return self.wavelength()

    def directivity(self):
        return 10


class Parabolic(Antenna):
    def length(self):
        return self.wavelength() * 3

    def directivity(self):
        return 25


class Horn(Antenna):
    def length(self):
        return self.wavelength() * 2

    def directivity(self):
        return 15


class CellSite(Antenna):
    def length(self):
        return self.wavelength() / 2

    def directivity(self):
        return 12


class Microstrip(Antenna):
    def length(self):
        return self.wavelength() / 2.5

    def directivity(self):
        return 6
