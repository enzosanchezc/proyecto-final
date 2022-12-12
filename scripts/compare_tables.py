import csv
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import EngFormatter
from matplotlib.widgets import Cursor
import sys

x = [12.6,18,24.3,30.6,40,58,80.7,88.5]
y_real = [5.77,7,8.3,9.13,10.2,11.6,12.4,12.6]
y_sim = [12.49,12.7,12.84,12.98,13,13.09,13.17,13.24]

# Use latex fonts
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
#mostrar dos graficas en una
fig,ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 4))
ax.xaxis.set_major_formatter(EngFormatter(unit='Ohm'))
ax.yaxis.set_major_formatter(EngFormatter(unit='V'))
ax.set_xlabel('Resistencia de carga')#, fontsize=20)
ax.set_ylabel('Tensión')#, fontsize=20)
#enable grid
ax.grid(True)
# ax.tick_params(axis='both', which='major', labelsize=20)
# ax.tick_params(axis='both', which='minor', labelsize=20)
ax.plot(x,y_real,color='red', linewidth=1.5, label='Real')
ax.plot(x,y_sim,color='blue', linewidth=1.5, label='Simulación')
ax.legend(loc='lower right')#, fontsize=20)
plt.show()
