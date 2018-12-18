import numpy as np
import scipy.signal
import os

dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    puzzle_input = f.read().splitlines()

current_area = np.zeros((len(puzzle_input), len(puzzle_input[0])), dtype=int)
fields = np.zeros((len(puzzle_input), len(puzzle_input[0])), dtype=int)
fields[:] = 1
trees = np.zeros((len(puzzle_input), len(puzzle_input[0])), dtype=int)
trees[:] = 10
yards = np.zeros((len(puzzle_input), len(puzzle_input[0])), dtype=int)
yards[:] = 100
conversion = {".": 1, "|": 10, "#": 100}

for row, line in enumerate(puzzle_input):
    for col, char in enumerate(line):
        current_area[row][col] = conversion[char]

filter = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

for n in range(0, 1000):
    sums = scipy.signal.convolve2d(current_area, filter, mode='same')
    new_area = np.where(np.logical_and(current_area == 1, sums % 100 >= 30), trees, current_area)
    new_area = np.where(np.logical_and(current_area == 10, sums % 1000 >= 300), yards, new_area)
    new_area = np.where(np.logical_and(current_area == 100, np.logical_and(sums % 100 >= 10, sums % 1000 >= 100)), yards, new_area)
    new_area = np.where(np.logical_and(current_area == 100, np.logical_not(np.logical_and(sums % 100 >= 10, sums % 1000 >= 100))), fields, new_area)
    current_area, new_area = new_area, current_area
    treesum = np.sum(current_area == 10)
    yardsum = np.sum(current_area == 100)
    print(f"{n}: {treesum*yardsum}")
