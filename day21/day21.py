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

# to help debug my_program
def execute_elfcode(initval):
    limit = 1000000000

    count = 0
    registers = [initval, 0, 0, 0, 0, 0]
    ip = 0
    while True:
        count += 1
        registers[ip_register] = ip    
        all_ops[instructions[ip]["op"]](instructions[ip]["args"], registers)

        print(f"{count:04d}: {ip:02d}: {instructions[ip]['op']} {instructions[ip]['args']} => {registers}")

        ip = registers[ip_register]
        ip += 1

        if ip >= len(instructions) or ip < 0:
            break

        if count >= limit:
            return limit

    return count


def my_program(initval):
    part_1 = True

    possibilities = []

    steps = 0
    reg0 = initval
    reg2 = 0
    reg5 = 0

    steps = 5
    while True:
        reg2 = reg5 | 0x010000
        reg5 = 10362650
        steps += 2

        while True:
            reg5 = (((reg5 + (reg2 & 0xFF)) & 0xFFFFFF) * 65899) & 0xFFFFFF
 
            steps += 7
            if 256 > reg2:  # ip14
                steps += 1

                # Program halts if we get here and reg5 == reg0
                # so all values of reg5 here will resuls in halt condition

                if part_1:
                    # assumes that there is a solution where only one iteration is needed
                    print("Part 1: " + str(reg5))
                    part_1 = False

                if reg5 not in possibilities:
                    possibilities.append(reg5)
                else:
                    # assumes there is a repeating pattern
                    print("Part 2: " + str(possibilities[-1]))
                    return
                
                break
            else:
                x = (reg2 // 256)   # number of iterations
                steps += 7*x + 9
                reg2 = x

        steps += 2
        if reg5 == reg0:
            return steps
        steps += 1

my_program(0)
