import copy
import os

dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    puzzle_input = f.read().splitlines()

current_step = []
for line in puzzle_input:
    current_step.append([])
    for char in line:
        current_step[-1].append(char)

def get_next_content(area, row, col):
    adjacent = {'#': 0, "|": 0, '.': 0}
    for r in range(max(0, row-1), min(len(area), row+2)):
        for c in range(max(0, col-1), min(len(area[0]), col+2)):
            if r == row and c == col:
                continue
            adjacent[area[r][c]] += 1

    if area[row][col] == '.':
        return '|' if adjacent['|'] >= 3 else '.'
    elif area[row][col] == '|':
        return '#' if adjacent['#'] >= 3 else '|'
    else:
        if adjacent['|'] > 0 and adjacent['#'] > 0:
            return '#'
        else:
            return '.'


next_step = copy.deepcopy(current_step)

for n in range(0, 10):
    if n % 1000 == 0:
        print(n)
    for r in range(len(current_step)):
        next_step[r] = [get_next_content(current_step, r, c) for c in range(len(current_step[0]))]

    current_step, next_step = next_step, current_step

for ns in next_step:
    print(''.join(ns))

counts = {'#': 0, "|": 0, '.': 0}
for row in current_step:
    for col in row:
        counts[col] += 1

print(counts)

print(counts['|']*counts['#'])