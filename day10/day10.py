import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    input_data = f.read()

lines = input_data.splitlines()

points = np.zeros((len(lines), 4))

for i, line in enumerate(lines):
    x0 = int(line[10:16])
    y0 = int(line[17:24])
    vx = int(line[36:38])
    vy = int(line[39:42])
    points[i] = [x0, y0, vx, vy]

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r.', animated=True)
plt.axis('equal')

def init():
    ax.set_xlim(100, 200)
    ax.set_ylim(-250, -50)
    return ln,

def update(frame):
    xdata = points[:, 0] + frame*points[:, 2]
    ydata = - (points[:, 1] + frame*points[:, 3])
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(10005, 10025, 20, endpoint=False), 
                    init_func=init, blit=True, interval=1000)
plt.show()

    


