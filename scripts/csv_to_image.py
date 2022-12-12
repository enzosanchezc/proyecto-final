# import csv file with pairs of x,y coordinates and plot them with latex fonts
# Usage: python csv_to_image.py <file.csv> <xstart> <xend>
import csv
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import EngFormatter
from matplotlib.widgets import Cursor
import sys

x = []
y = []

with open(sys.argv[1], 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    # skip first two lines
    # next(plots)
    # next(plots)
    # next(plots)
    # next(plots)
    # next(plots)
    # next(plots)
    # next(plots)
    # next(plots)
    next(plots)
    next(plots)
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

# Use latex fonts
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig,ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 4))
ax.xaxis.set_major_formatter(EngFormatter(unit='s'))
ax.yaxis.set_major_formatter(EngFormatter(unit='V'))
ax.set_xlabel('Tiempo')#, fontsize=20)
ax.set_ylabel('Tensión')#, fontsize=20)
#enable grid
ax.grid(True)
#ax.set_title(sys.argv[3])
# if limits are given, use them
if len(sys.argv) == 4:
    ax.set_xlim(float(sys.argv[2])-260e-9, float(sys.argv[3])-260e-9)
# Divide y values by 10.8
#y = [i /10000 for i in y]
# Inverti y values
#y = [-i for i in y]
# increase plot font size
ax.tick_params(axis='both', which='major')#, labelsize=20)
ax.tick_params(axis='both', which='minor')#, labelsize=20)
ax.plot(x,y,color='red', linewidth=0.7)
cursor = Cursor(ax, useblit=True, color='red', linewidth=2)
plt.show()
#plt.savefig(sys.argv[2])