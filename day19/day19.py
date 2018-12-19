import os

def addr(args, regs):
    regs[args["C"]] = regs[args["A"]] + regs[args["B"]]

def addi(args, regs):
    regs[args["C"]] = regs[args["A"]] + args["B"]

def mulr(args, regs):
    regs[args["C"]] = regs[args["A"]] * regs[args["B"]]

def muli(args, regs):
    regs[args["C"]] = regs[args["A"]] * args["B"]

def banr(args, regs):
    regs[args["C"]] = regs[args["A"]] & regs[args["B"]]

def bani(args, regs):
    regs[args["C"]] = regs[args["A"]] & args["B"]

def borr(args, regs):
    regs[args["C"]] = regs[args["A"]] | regs[args["B"]]

def bori(args, regs):
    regs[args["C"]] = regs[args["A"]] | args["B"]

def setr(args, regs):
    regs[args["C"]] = regs[args["A"]]

def seti(args, regs):
    regs[args["C"]] = args["A"]

def gtir(args, regs):
    regs[args["C"]] = 1 if args["A"] > regs[args["B"]] else 0

def gtri(args, regs):
    regs[args["C"]] = 1 if regs[args["A"]] > args["B"] else 0

def gtrr(args, regs):
    regs[args["C"]] = 1 if regs[args["A"]] > regs[args["B"]] else 0

def eqir(args, regs):
    regs[args["C"]] = 1 if args["A"] == regs[args["B"]] else 0

def eqri(args, regs):
    regs[args["C"]] = 1 if regs[args["A"]] == args["B"] else 0

def eqrr(args, regs):
    regs[args["C"]] = 1 if regs[args["A"]] == regs[args["B"]] else 0

all_ops = {
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr,
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtir": gtir,
    "gtri": gtri,
    "gtrr": gtrr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr}


dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, "input")) as f:
    puzzle_input = f.read().splitlines()

ip_register = int(puzzle_input[0][4:])
parsed_input = list(map(lambda x: x.split(" "), puzzle_input[1:]))
instructions = [{"op": i[0], "args": {"A": int(i[1]), "B": int(i[2]), "C": int(i[3])}} for i in parsed_input]

def part_1():
    registers = [1, 0, 0, 0, 0, 0]
    ip = 0
    while True:
        registers[ip_register] = ip    
        all_ops[instructions[ip]["op"]](instructions[ip]["args"], registers)
        print(f"{ip}, {registers}")
        ip = registers[ip_register]
        ip += 1

        if ip >= len(instructions) or ip < 0:
            break

    print(registers)

#part_1()


ip = 3
initial = (0, 1, 0, 558, 2, 10551264)
reg0, reg1, reg2, reg3, reg4, reg5 = initial


x = 0
for n in range (1, reg5+1):
    if reg5 % n == 0:
        x += n

print(x)

# for reg1 in range(1, reg5+1):
#     for reg3 in range(1, reg5+1):
#         regg2 = reg1*reg3
#         if reg2 == reg5:
#             reg0 += reg1


# while True:
#     while True:
#         reg2 = reg1 * reg3
#         if reg2 == reg5:
#             reg0 += reg1
#         # this loop 10551264 times
#         reg3 += 1
#         if reg3 > reg5:
#             reg3 = 1
#             break
#     reg1 += 1
#     if reg1 > reg5:
#         break

# 2 seti 1 7 3 , reg 3 = 1
# 3 mulr 1 3 2 , reg 2 = reg 1 x reg 3
# 4 eqrr 2 5 2 , -
# *5 addr 2 4 4 , SKIP next, when reg 2 == reg 5
# 6 addi 4 1 4 , SKIP next
# 7 addr 1 0 0 , reg 0 incr by reg 1 ???? how many times??
# 8 addi 3 1 3 , reg 3 incr by 1
# 9 gtrr 3 5 2 , -
# *10 addr 4 2 4 , SKIP next when reg 3 > reg 5
# 11 seti 2 3 4 , JUMP to 3
# 12 addi 1 1 1 , reg 1 incr 1
# 13 gtrr 1 5 2 , -
# 14 addr 2 4 4, SKIP next when reg 1 > reg 5
# 15 seti 1 6 4, JUMP to 2
# 16 mulr 4 4 4, ip = ip^2 == > ends