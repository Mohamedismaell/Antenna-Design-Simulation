import tkinter as tk
from tkinter import ttk, messagebox
from models.directive_antennas_model import *
from models.omni_antenna_models import *
from antenna_plot import AntennaPlot


class AntennaGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Antenna Characteristics Calculator")
        self.root.geometry("420x450")

        tk.Label(self.root, text="Frequency (Hz):").pack()
        self.freq_entry = tk.Entry(self.root)
        self.freq_entry.pack()

        tk.Label(self.root, text="Radiation Resistance Rr (Ω):").pack()
        self.rr_entry = tk.Entry(self.root)
        self.rr_entry.pack()

        tk.Label(self.root, text="Loss Resistance Rl (Ω):").pack()
        self.rl_entry = tk.Entry(self.root)
        self.rl_entry.pack()

        tk.Label(self.root, text="Select Antenna Type").pack(pady=10)

        self.antennas = [
            "Monopole",
            "Dipole",
            "Folded Dipole",
            "Loop",
            "Discone",
            "Yagi",
            "Helical",
            "Parabolic",
            "Horn",
            "Cell Site",
            "Microstrip"
        ]

        # * select only => readonly
        self.combo = ttk.Combobox(
            self.root, values=self.antennas, state="readonly")
        self.combo.pack()
        self.combo.current(1)

        tk.Button(self.root, text="Calculate",
                  command=self.calculate).pack(pady=10)
        tk.Button(self.root, text="Show Pattern",
                  command=self.plot_pattern).pack(pady=5)

        self.result = tk.Text(self.root, height=10, width=45)
        self.result.pack()
        self.plotter = AntennaPlot()
        self.antenna = None

        self.root.mainloop()

    def get_antenna_object(self, f, Rr, Rl, name):

        mapping = {
            "Dipole": Dipole,
            "Monopole": Monopole,
            "Folded Dipole": FoldedDipole,
            "Loop": Loop,
            "Discone": Discone,
            "Yagi": Yagi,
            "Helical": Helical,
            "Parabolic": Parabolic,
            "Horn": Horn,
            "Cell Site": CellSite,
            "Microstrip": Microstrip
        }

        return mapping[name](f, Rr, Rl)

    def calculate(self):
        try:
            f = float(self.freq_entry.get())
            Rr = float(self.rr_entry.get())
            Rl = float(self.rl_entry.get())
        except ValueError:
            messagebox.showerror(
                "Input Error", "Please enter valid numeric values")
            return

        antenna_name = self.combo.get()
        try:
            self.antenna = self.get_antenna_object(f, Rr, Rl, antenna_name)
            self.result.delete(1.0, tk.END)
            self.result.insert(tk.END, f"Antenna Type: {antenna_name}\n")
            self.result.insert(
                tk.END, f"Wavelength: {round(self.antenna.wavelength(), 4)} m\n")
            self.result.insert(
                tk.END, f"Antenna Length: {round(self.antenna.length(), 4)} m\n")
            self.result.insert(
                tk.END, f"Gain: {round(self.antenna.gain_db(), 2)} dB\n")
            self.result.insert(
                tk.END, f"Directivity: {self.antenna.directivity()}\n")
            self.result.insert(
                tk.END, f"Efficiency: {round(self.antenna.efficiency()*100, 2)} %\n")
            # self.result.insert(
            #     tk.END, f"Beamwidth: {self.antenna.beamwidth()} degrees\n")
        except Exception as e:
            messagebox.showerror("Calculation Error",
                                 f"An error occurred: {e}")

    def plot_pattern(self):

        if self.antenna is None:
            messagebox.showwarning("Warning", "Calculate first!")
            return

        name = type(self.antenna).__name__
        self.plotter.plot(self.antenna)


AntennaGUI()
