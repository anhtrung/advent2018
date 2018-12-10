import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    input_data = f.read()

lines = input_data.splitlines()
max_time = 50000

points = np.zeros((max_time, len(lines), 2), dtype=int)
times = np.arange(0, max_time, 1)

for i, line in enumerate(lines):
    x0 = int(line[10:16])
    y0 = int(line[17:24])
    vx = int(line[36:38])
    vy = int(line[39:42])
    points[:, i, 0] = x0 + times*vx
    points[:, i, 1] = y0 + times*vy

points_range = np.abs(np.max(points[:, :, :], axis=1) - np.min(points[:, :, :], axis=1))
min_spread = np.argmin(points_range, axis=0)

for t in min_spread:
    print(t)
    plt.plot(points[t, :, 0], - points[t, :, 1], 'r.')
    plt.axis('equal')
    plt.show()

    


