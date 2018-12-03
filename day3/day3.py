import os
import numpy as np


def parse_claim(claim):
    id = claim[1:claim.find(' ')]
    pos = claim[claim.find('@') + 1:claim.find(':')].split(',')
    dim = claim[claim.find(':') + 1:].split('x')
    return pos, dim, id

dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    input_data = f.read()
lines = input_data.splitlines()

fabric = np.zeros((2000, 2000), dtype=int)

for l in lines:
    p, d, _ = parse_claim(l)
    fabric[int(p[0]):int(p[0]) + int(d[0]), int(p[1]):int(p[1]) + int(d[1])] += 1

print("Part 1: " + str((fabric > 1).sum()))

for l in lines:
    p, d, id = parse_claim(l)
    if (fabric[int(p[0]):int(p[0]) + int(d[0]), int(p[1]):int(p[1]) + int(d[1])] == 1).all():
        print("Part 2: " + str(id))
