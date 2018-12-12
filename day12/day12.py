with open("input.txt", "r") as f:
    s = f.read().splitlines()

initial_state = s[0][15:]

rules = {}
for rule in s[2:]:
    before = rule[0:5]
    after = rule[9]
    rules[before] = after

gen_state = initial_state
pot0_idx = 0

for gen in range(500):
#    if gen % 1000 == 0:
#        print(gen)
    spacing = ' '*(20 - pot0_idx)
#    print(spacing + gen_state)
    while gen_state.startswith('.........'):
        gen_state = gen_state[5:]
        pot0_idx -= 5
    while gen_state.endswith('.........'):
        gen_state = gen_state[:-5]

    if not gen_state.startswith('....'):
        gen_state = '....' + gen_state
        pot0_idx += 4
    if not gen_state.endswith('....'):
        gen_state += '....'

    pot0_idx -= 2
    g = ''
    for i in range(2, len(gen_state) - 2):
        xx = gen_state[i-2:i+3]
        if xx not in rules:
            g += '.'
        else:
            g += rules[xx]
    gen_state = g

    sum = 0
    for idx, pot in enumerate(gen_state):
        if pot == '#':
            sum += idx - pot0_idx

    print(sum)


spacing = ' ' * (20 - pot0_idx)
print(spacing + gen_state)

c = gen_state.count('#')
print(c)

sum = 0
for idx, pot in enumerate(gen_state):
    if pot == '#':
        sum += idx - pot0_idx
print(sum)


total = (50000000000 - 500)*c + sum
print(total)