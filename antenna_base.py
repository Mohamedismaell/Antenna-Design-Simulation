from abc import ABC, abstractmethod
import math


class Antenna(ABC):

    def __init__(self, frequency, Rr, RL):
        self.f = frequency
        self.Rr = Rr
        self.RL = RL
        self.c = 3e8

    def wavelength(self):
        return self.c / self.f

    def efficiency(self):
        return self.Rr / (self.Rr + self.RL)

    def gain_db(self):
        return 10 * math.log10(self.gain_linear())

    def gain_linear(self):
        return self.directivity() * self.efficiency()

    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def directivity(self):
        pass

    # @abstractmethod
    # def beamwidth(self):
    #     pass
