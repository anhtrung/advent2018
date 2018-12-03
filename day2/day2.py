from functools import reduce
import os


def box_count(box_id):
    has_2 = 1 if len([c for c in box_id if box_id.count(c) == 2]) > 0 else 0
    has_3 = 1 if len([c for c in box_id if box_id.count(c) == 3]) > 0 else 0
    return has_2, has_3

dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    input_data = f.read()
lines = input_data.splitlines()

results = reduce((lambda x, y: (x[0] + y[0], x[1] + y[1])),  map(box_count, lines))

print("Part 1: " + str(results[0]*results[1]))

for i, id_a in enumerate(lines):
    for id_b in lines[i + 1:]:
        common_letters = [c for j, c in enumerate(id_a) if id_b[j] == c]
        if len(common_letters) == len(id_a) - 1:
            print("Part 2: " + ''.join(common_letters))

