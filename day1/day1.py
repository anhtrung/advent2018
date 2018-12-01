import itertools

with open('input') as f:
    input_data = f.read()
lines = input_data.splitlines()
print("Part 1: {0}".format(sum(map(int, lines))))

sum = 0
freqs = set([0])

for num in itertools.cycle(lines):
    sum += int(num)
    if sum in freqs:
        break
    freqs.add(sum)
print("Part 2: {0}".format(sum))
