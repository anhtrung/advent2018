import os
import string

def react(poly):
    reacted = []
    for c in poly:
        if reacted and reacted[-1].lower() == c.lower() and reacted[-1].islower() != c.islower():
            reacted.pop()
        else:
            reacted.append(c)
    return reacted

            
dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    input_data = f.read()

poly = input_data.strip()

part1 = react(poly)

print("Part 1: " + str(len(part1)))

alpha = string.ascii_lowercase[:]

results = map((lambda x: len(react(''.join(part1).replace(x.lower(), '').replace(x.upper(), '')))), alpha)

print("Part 2: " + str(min(results)))