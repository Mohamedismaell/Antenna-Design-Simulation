from antenna_input import AntennaInput
from antenna_plot import AntennaPlot


system = AntennaInput()
antenna = system.get_antenna()

print("\n--- ANTENNA RESULTS ---")
print("Wavelength:", round(antenna.wavelength(), 4), "m")
print("Antenna Length:", round(antenna.length(), 4), "m")
print("Gain:", round(antenna.gain_db(), 2), "dB")
print("Directivity:", antenna.directivity())
print("Efficiency:", round(antenna.efficiency()*100, 2), "%")

#! Not working
# print("Beamwidth:", antenna.beamwidth(), "degrees")

plotter = AntennaPlot()
plotter.plot(type(antenna).__name__)

# Enter frequency (Hz): 100000000   # 100 MHz
# Enter radiation resistance Rr: 50
# Enter loss resistance RL: 5
# Enter number: 2   # Dipole
