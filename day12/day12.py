import os

dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    s = f.read().splitlines()

initial_state = s[0][15:]

rules = {}
for rule in s[2:]:
    before = rule[0:5]
    after = rule[9]
    rules[before] = after

gen_state = '.'*len(initial_state) + initial_state + '.'*len(initial_state)

for gen in range(20):
    g = '..'
    for i in range(2, len(gen_state) - 2):
        xx = gen_state[i-2:i+3]
        if xx not in rules:
            g += '.'
        else:
            g += rules[xx]
    g += '..'
    gen_state = g
    print(g)

c = gen_state.count('#')

sum = 0
for idx, pot in enumerate(gen_state):
    if pot == '#':
        sum += idx - len(initial_state)

print(sum)