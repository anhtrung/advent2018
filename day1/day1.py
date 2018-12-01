with open('input') as f:
    input_data = f.read()
lines = input_data.splitlines()

sum = 0
freqs = set()
part1 = True
check = True

while check:
    for line in lines:
        if line[0] == '+':
            sum += int(line[1:])
        else:
            sum -= int(line[1:])
        if sum in freqs:
            check = False
            break
        freqs.add(sum)
    if part1:
        print("Part 1: {0}".format(sum))
        part1 = False
print("Part 2: {0}".format(sum))
