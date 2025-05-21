import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("/home/as/Downloads/DM data/Neff.csv", header=None ,names=['x','y'])
dataCCFR = pd.read_csv("/home/as/Downloads/DM data/CCFR.csv", header=None ,names=['xccfr','yccfr'])
dataWD = pd.read_csv("/home/as/Downloads/DM data/WD.csv", header=None ,names=['xwd','ywd'])
dataATLAS = pd.read_csv("/home/as/Downloads/DM data/ATLAS.csv", header=None ,names=['xatlas','yatlas'])
dataBaBar = pd.read_csv("/home/as/Downloads/DM data/BaBar.csv", header=None ,names=['xba','yba'])
dataMuC = pd.read_csv("/home/as/Downloads/DM data/MuC-Proj.csv", header=None ,names=['xmuc','ymuc'])
dataFCC = pd.read_csv("/home/as/Downloads/DM data/FCC-ee-Proj.csv", header=None ,names=['xfcc','yfcc'])
dataSHiP = pd.read_csv("/home/as/Downloads/DM data/SHiP-Proj.csv", header=None ,names=['xship','yship'])
dataLDMX = pd.read_csv("/home/as/Downloads/DM data/LDMX-Proj.csv", header=None ,names=['xldmx','yldmx'])
dataBeam = pd.read_csv("/home/as/Downloads/DM data/Beam_dump-Proj.csv", header=None ,names=['xbeam','ybeam'])
datamusic = pd.read_csv("/home/as/Downloads/DM data/MuSIC-Proj.csv", header=None ,names=['xmusic','ymusic'])
datacms = pd.read_csv("/home/as/Downloads/DM data/CMS.csv", header=None ,names=['xcms','ycms'])
dataNA = pd.read_csv("/home/as/Downloads/DM data/NA64.csv", header=None ,names=['xNA','yNA'])

x = data['x']
y = data['y']
xccfr = dataCCFR['xccfr']
yccfr = dataCCFR['yccfr']
xwd = dataWD['xwd']
ywd = dataWD['ywd']
xatlas = dataATLAS['xatlas']
yatlas = dataATLAS['yatlas']
xba = dataBaBar['xba']
yba = dataBaBar['yba']
xmuc = dataMuC['xmuc']
ymuc = dataMuC['ymuc']
xfcc = dataFCC['xfcc']
yfcc = dataFCC['yfcc']
xship = dataSHiP['xship']
yship = dataSHiP['yship']
xldmx = dataLDMX['xldmx']
yldmx = dataLDMX['yldmx']
xbeam = dataBeam['xbeam']
ybeam = dataBeam['ybeam']
xmusic = datamusic['xmusic']
ymusic = datamusic['ymusic']
xcms = datacms['xcms']
ycms = datacms['ycms']
xNA = dataNA['xNA']
yNA = dataNA['yNA']

# For Neff fill
ymax = max(y)
index = np.argmax(y == ymax)
xmax = x[index]
y1 = np.append(y, 1)
x1 = np.append(x, xmax)

plt.figure(figsize=(10, 7))

plt.plot(x, y, label="Neff", color='blue')
plt.text(1e-2, 1e-7, "Neff", fontsize=8, color='blue')
plt.fill_betweenx(y1, x1, color='lightblue', alpha=0.8)

plt.plot(xccfr, yccfr, label="CCFR", color='black')
plt.text(1e2, 1e-1, "CCFR", fontsize=8, color='black')
plt.fill_betweenx(yccfr, xccfr, color='black', alpha=0.3)

plt.plot(xNA, yNA, label="NA64$\mu$", color='indigo')  # Changed from black to indigo
plt.text(6e-2, 3e-4, "NA64$\mu$", fontsize=8, color='indigo')  # Changed text color to match
plt.fill_between(xNA, yNA, y2=1, color='indigo', alpha=0.3)  # Added y2=1 parameter to fill to the top

plt.plot(xwd, ywd, label="WD", color='gold')
plt.text(1e-1, 2e-3, "WD", fontsize=10, color='gold')
plt.fill_between(xwd, ywd, y2=1, color='gold', alpha=0.5)

plt.plot(xatlas, yatlas, label="ATLAS", color='red')
plt.text(1e1, 1e-3, "ATLAS", fontsize=8, color='red')
plt.fill_between(xatlas, yatlas, y2=1, color='red', alpha=0.5)

plt.plot(xba, yba, label="BaBar", color='orange')
plt.text(3e-1, 5e-4, "BaBar 4 $\mu$", fontsize=10, color='orange')
plt.fill_between(xba, yba, y2=1, color='orange', alpha=0.5)

plt.plot(xcms, ycms, label="CMS", color='darkviolet')
plt.text(3e0, 2e-3, "CMS", fontsize=10, color='darkviolet')
plt.fill_between(xcms, ycms, y2=1, color='darkviolet', alpha=0.5)

plt.scatter(xmuc, ymuc, label="MuC", color='purple', marker='o', s=4)
plt.text(1e3, 1e-2, "MuC", fontsize=8, color='purple')

plt.scatter(xfcc, yfcc, label="FCC-ee", color='green', marker='x', s=4)
plt.text(1e2, 1e-3, "FCC-ee", fontsize=8, color='green')

plt.scatter(xship, yship, label="SHiP", color='brown', marker='o', s=3)
plt.text(1e-2, 2e-6, "SHiP", fontsize=8, color='brown')

plt.scatter(xldmx, yldmx, label="LDMX", color='magenta', marker='o', s=3)
plt.text(5e-2, 5e-5, "LDMX", fontsize=8, color='magenta')

plt.scatter(xbeam, ybeam, label="Beam dump", color='teal', marker='s', s=4)
plt.text(2e0, 8e-8, "Beam_dump", fontsize=8, color='teal')


plt.scatter(xmusic, ymusic, label="MuSIC", color='gray', marker='^', s=4)
plt.text(1e1, 9e-6, "MuSIC", fontsize=8, color='gray')

mchi = 1e-22

x_line = np.logspace(-3, 4, 200)  # from 1e-3 to 1e4 (same as your xlim)
constant = 2.86e1*mchi**0.5
y_line = constant * x_line

plt.plot(x_line, y_line, color='orchid', linestyle='--', label=r"$\nu$ Oscillation")
plt.fill_between(x_line, y_line, y2=1, color='orchid', alpha=0.1)
plt.text(1e2, 6e-8, "E = 1 PeV", fontsize=8, color='orchid', rotation=30)

#Different Energies E = 1 TeV
constant2 = 9.04e2*mchi**0.5
y_line2 = constant2 * x_line
plt.plot(x_line, y_line2, color='orchid', linestyle='--')
plt.text(2e2, 4e-6, "E = 1 TeV", fontsize=8, color='orchid', rotation=30)

#Different Energies E = 1 GeV
constant2 = 2.86e4*mchi**0.5
y_line2 = constant2 * x_line
plt.plot(x_line, y_line2, color='orchid', linestyle='--')
plt.text(2e2, 8e-5, "E = 1 GeV", fontsize=8, color='orchid', rotation=30)

#Different Energies E = 100 PeV
constant2 = 2.86e0*mchi**0.5
y_line2 = constant2 * x_line
plt.plot(x_line, y_line2, color='orchid', linestyle='--')
plt.text(2e2, 1e-8, "E = 100 PeV", fontsize=8, color='orchid', rotation=30)

plt.xscale('log')
plt.yscale('log')
plt.ylim(1e-8, 1)
plt.xlim(1e-3, 1e4)
plt.xlabel("$m_{Z'}$ (GeV)")
plt.ylabel("g'")
plt.legend(loc='lower right')
# plt.grid(False, which="both", ls="--", alpha=0.5)
plt.tight_layout()
plt.show()
