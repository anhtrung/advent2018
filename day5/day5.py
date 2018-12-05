import os

dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    input_data = f.read()

poly = input_data.strip()

last_len = len(poly)
while True:
    for i in range(len(poly) - 1):
        if poly[i].lower() == poly[i+1].lower() and poly[i].islower() != poly[i+1].islower():
            poly = poly[:i] + poly[i+2:]
            break
    if len(poly) == last_len:
        break
    last_len = len(poly)

print("Part 1: " + str(len(poly)))