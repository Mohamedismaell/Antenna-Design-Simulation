# Antenna Design Simulation

A Python-based simulation tool for calculating antenna characteristics and visualizing radiation patterns. This project provides a Graphical User Interface (GUI) to interact with various antenna models.

## Features

- **Antenna Characteristics Calculator**: Calculate key parameters including:
  - Wavelength
  - Antenna Length
  - Gain (dB)
  - Directivity
  - Efficiency
- **Radiation Pattern Visualization**: View 2D polar plots of antenna radiation patterns.
- **Multiple Antenna Types**: Support for various antenna models:
  - Monopole
  - Dipole
  - Folded Dipole
  - Loop
  - Discone
  - Yagi
  - Helical
  - Parabolic
  - Horn
  - Cell Site
  - Microstrip

## Requirements

- Python 3.x
- `numpy`
- `matplotlib`
- `tkinter` (usually included with Python)

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies:
   ```bash
   pip install numpy matplotlib
   ```

## Usage

### Running the GUI

To launch the graphical interface:

```bash
python antenna_gui.py
```

1. Enter the **Frequency (Hz)**.
2. Enter **Radiation Resistance (Rr)** and **Loss Resistance (Rl)**.
3. Select an **Antenna Type** from the dropdown menu.
4. Click **Calculate** to view the characteristics.
5. Click **Show Pattern** to visualize the radiation pattern.

### Running the CLI Script

You can also run the basic script directly:

```bash
python main.py
```

## Project Structure

- `antenna_gui.py`: Main entry point for the GUI application.
- `antenna_plot.py`: Handles the plotting of radiation patterns using Matplotlib.
- `main.py`: Command-line script for testing antenna models.
- `models/`: Contains the implementation of different antenna classes.
