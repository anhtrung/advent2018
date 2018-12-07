import os
from collections import defaultdict
import string


def completed_presteps(pre_steps, completed):
    for letter in pre_steps:
        if letter not in completed:
            return False
    return True

dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    input_data = f.read()

rules = defaultdict(list)

alphabet = []
for line in input_data.splitlines():
    rules[line[36]].append(line[5])
    alphabet.extend([line[5], line[36]])

alphabet = sorted(set(alphabet))

order = []
while len(order) < len(alphabet):
    for letter in alphabet:
        if letter not in rules and letter not in order:
            order.append(letter)
            break
        elif completed_presteps(rules[letter], order) and letter not in order:
            order.append(letter)
            break
    
print('Part 1: ' + ''.join(order))
