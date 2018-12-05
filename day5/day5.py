import os
import string

def react(poly):
    i = 0
    while True:
        if i == len(poly) - 1:
            return len(poly)
        if poly[i].lower() == poly[i+1].lower() and poly[i].islower() != poly[i+1].islower():
            poly = poly[:i] + poly[i+2:]
            i = max(0, i - 1)
        else:
            i += 1
            
dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    input_data = f.read()

poly = input_data.strip()

part1 = react(poly)
print("Part 1: " + str(part1))

alpha = string.ascii_lowercase[:]

counts = {}
for letter in alpha:
    poly = input_data.strip().replace(letter, '').replace(letter.upper(), '')
    counts[letter] = react(poly)

print("Part 2: " + str(min(counts.values())))