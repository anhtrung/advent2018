import os
import numpy as np
from collections import defaultdict

dir = os.path.dirname(os.path.realpath(__file__))
data = np.loadtxt(os.path.join(dir, 'input'), dtype=int,delimiter=',')

mins = np.min(data, axis=0)
maxs = np.max(data, axis=0)

xs = np.arange(mins[0]-40, maxs[0]+40)
ys = np.arange(mins[1]-40, maxs[1]+40)

land = np.zeros((len(xs), len(ys), len(data)), dtype=int)
counts = defaultdict(int)
excluded = []

for y_idx, y in enumerate(ys):
    for x_idx, x in enumerate(xs):
        land[x_idx, y_idx, :] = abs(x - data[:, 0]) + abs(y - data[:, 1])
        min_val = np.min(land[x_idx, y_idx, :])
        min_idx = np.argwhere(land[x_idx, y_idx, :] == min_val)
        if len(min_idx) == 1:
            counts[min_idx[0][0]] += 1

        if x < (xs[10]) or x > (xs[-10]) or y < (ys[10]) or y > (ys[-10]):
            excluded.extend(min_idx[0])

excluded = set(excluded)
filtered_counts = {k:v for (k,v) in counts.items() if k not in excluded}
min_coord = max(filtered_counts, key=lambda x: filtered_counts[x])

print("Part 1: " + str(filtered_counts[min_coord]))

totals = np.sum(land, axis=2)
acceptable = totals < 10000

print("Part 2: " + str(acceptable.sum()))

