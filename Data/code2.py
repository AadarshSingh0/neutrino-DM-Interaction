import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("/home/as/Downloads/DM data/Data_large/Neff_003.csv", header=None ,names=['x','y'])
dataCCFR = pd.read_csv("/home/as/Downloads/DM data/Data_large/CCFR.csv", header=None ,names=['xccfr','yccfr'])
databorexino = pd.read_csv("/home/as/Downloads/DM data/Data_large/Borexino.csv", header=None ,names=['xBorexino','yBorexino'])
dataSN1987A = pd.read_csv("/home/as/Downloads/DM data/Data_large/SN1987A.csv", header=None ,names=['xSN1987A','ySN1987A'])
datastellar = pd.read_csv("/home/as/Downloads/DM data/Data_large/stellar.csv", header=None ,names=['xstellar','ystellar'])

x = data['x']
y = data['y']
xccfr = dataCCFR['xccfr']
yccfr = dataCCFR['yccfr']
xBorexino = databorexino['xBorexino']
yBorexino = databorexino['yBorexino']
xSN1987A = dataSN1987A['xSN1987A']
ySN1987A = dataSN1987A['ySN1987A']
xstellar = datastellar['xstellar']
ystellar = datastellar['ystellar']


# For Neff fill
ymax = max(y)
index = np.argmax(y == ymax)
xmax = x[index]
y1 = np.append(y, 1)
x1 = np.append(x, xmax)

xlim = max(xccfr)

plt.figure(figsize=(10, 7))

# plt.plot(x, y, label="Neff", color='blue')
plt.scatter(x, y, label="Neff", color='blue', marker='o', s=3)
plt.text(1e-2, 1e-12, "Neff", fontsize=10, color='blue')
plot_xmin = 1e-7 # Left boundary for log scale
sort_indices = np.argsort(y)
x_sorted = x[sort_indices]
y_sorted = y[sort_indices]
plt.fill_betweenx(y_sorted, plot_xmin, x_sorted, color='lightblue', alpha=0.5, step='pre', zorder=1)

plt.plot(xccfr, yccfr, label="CCFR", color='black')
plt.text(1e2, 5e-4, "CCFR", fontsize=10, color='black')
plt.fill_between(xccfr, yccfr, ymax, color='black', alpha=0.3)

plt.plot(xBorexino, yBorexino, label="Borexino", color='gold')
plt.text(1e0, 2e-4, "Borexino", fontsize=14, color='goldenrod')
plt.fill_between(xBorexino, yBorexino, y2=1, color='gold', alpha=0.3)

plt.scatter(xSN1987A, ySN1987A, label="SN1987A", color='red', marker='o', s=4)
plt.text(1e1, 1e-9, "SN1987A", fontsize=8, color='red')

sort_indices = np.argsort(xstellar)  
x_sorted = xstellar[sort_indices]
y_sorted = ystellar[sort_indices]
plt.plot(x_sorted, y_sorted, color='orange', label="Stellar Cooling", alpha=0.6, linewidth=4)
plt.fill_between(x_sorted, y_sorted, y2=1, color='orange', alpha=0.8)
plt.text(3e-1, 1e-9, "Stellar Cooling", fontsize=12, color='orange')

mchi = 1e-22

x_line = np.logspace(-6, 4, 200)  
constant = 2.86e-2 *mchi**0.5
y_line = constant * x_line

plt.plot(x_line, y_line, color='orchid', linestyle='--', label=r"$\nu$ Oscillation")
plt.fill_between(x_line, y_line, y2=1, color='orchid', alpha=0.1)
plt.text(2e1, 3e-12, "E = 1 PeV", fontsize=8, color='orchid', rotation=30)

#Different Energies E = 1 TeV
constant2 = 9.04e-1*mchi**0.5
y_line2 = constant2 * x_line
plt.plot(x_line, y_line2, color='orchid', linestyle='--')
plt.text(4e1, 5e-10, "E = 1 TeV", fontsize=8, color='orchid', rotation=30)

#Different Energies E = 1 GeV
constant2 = 2.86e1*mchi**0.5
y_line2 = constant2 * x_line
plt.plot(x_line, y_line2, color='orchid', linestyle='--')
plt.text(5e1, 3e-8, "E = 1 GeV", fontsize=8, color='orchid', rotation=30)

#Different Energies E = 100 PeV
constant2 = 2.86e-3*mchi**0.5
y_line2 = constant2 * x_line
plt.plot(x_line, y_line2, color='orchid', linestyle='--')
plt.text(2e1, 3e-13, "E = 100 PeV", fontsize=8, color='orchid', rotation=30)

plt.xscale('log')
plt.yscale('log')
plt.ylim(1e-13, ymax)
plt.xlim(1e-6, xlim)
plt.xlabel("$m_{Z'}$ (MeV)")
plt.ylabel("g'")
plt.legend()
# plt.grid(False, which="both", ls="--", alpha=0.5)
plt.tight_layout()
plt.show()
