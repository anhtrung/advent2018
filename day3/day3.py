import os
import numpy as np
import re


dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    input_data = f.read()
lines = input_data.splitlines()

claims = list(map((lambda x: [int(d) for d in re.findall(r'\d+', x)]), lines))

fabric = np.zeros((1500, 1500), dtype=int)

for id, x, y, w, h in claims:    
    fabric[x:x+w, y:y+h] += 1

print("Part 1: " + str((fabric > 1).sum()))

for id, x, y, w, h in claims:
    if (fabric[x:x+w, y:y+h] == 1).all():
        print("Part 2: " + str(id))
