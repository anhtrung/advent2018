import os

dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    puzzle_input = f.read().splitlines()

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

all_ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def missing_number(limit, check_set):
    for i in range(limit):
        if i not in check_set:
            return i
    assert False


samples = []
program = []
adding_sample = False
for line in puzzle_input:
    if line.startswith("Before"):
        adding_sample = True
        sample = {}
        sample["before"] = list(map((lambda x: int(x.strip())), line[9:19].split(",")))
    elif line.startswith("After"):
        sample["after"] = list(map((lambda x: int(x.strip())), line[9:19].split(",")))
        samples.append(sample)
        adding_sample = False
    elif len(line) > 0:
        instruction = list(map((lambda x: int(x)), line.split(' ')))
        if adding_sample:
            sample["opcode"] = instruction[0]
            sample["args"] = {"A": instruction[1], "B": instruction[2], "C": instruction[3]}
        else:
            program.append({
                "opcode": instruction[0],
                "args": {"A": instruction[1], "B": instruction[2], "C": instruction[3]}
            })
            

total = 0
opcode_idx_elim = {}
for x, s in enumerate(samples):
    correct_result = 0
    for idx, op in enumerate(all_ops):
        regs = list(s["before"])
        op(s["args"], regs)
        if regs == s["after"]:
            correct_result += 1
        else:
            if s["opcode"] not in opcode_idx_elim:
                opcode_idx_elim[s["opcode"]] = []
            opcode_idx_elim[s["opcode"]].append(idx)
    if correct_result >= 3:
        total += 1

print("Part 1: " + str(total))

for opcode in opcode_idx_elim:
    opcode_idx_elim[opcode] = set(opcode_idx_elim[opcode])

opcode_mapping = {} # key is opcode in program, val is index in all_ops
eliminating = True
while eliminating:
    for idx in range(len(all_ops)):
        if len(opcode_mapping) == len(all_ops):
            eliminating = False
            break
        if idx in opcode_mapping:
            continue
        if len(opcode_idx_elim[idx]) == len(all_ops) - 1:
            opcode_mapping[idx] = missing_number(len(all_ops), opcode_idx_elim[idx])
            for jdx in range(len(opcode_idx_elim)):
                if jdx != idx:
                    opcode_idx_elim[jdx].add(opcode_mapping[idx])
            break

program_registers = [0, 0, 0, 0]

for p in program:
    all_ops[opcode_mapping[p["opcode"]]](p["args"], program_registers)

print(program_registers)