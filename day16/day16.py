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

samples = []
program = []
adding_sample = False
for line in puzzle_input:
    if line.startswith("Before"):
        adding_sample = True
        sample = {"before": list(map((lambda x: int(x.strip())), line[9:19].split(",")))}
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
for s in samples:
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

opcode_idx_options = {}
for opcode in opcode_idx_elim:
    opcode_idx_options[opcode] = [op for op in range(len(all_ops)) if op not in opcode_idx_elim[opcode]]

opcode_mapping = {} # key is opcode in program, val is index in all_ops
eliminating = True
while len(opcode_mapping) != len(all_ops):
    for idx in range(len(all_ops)):
        if len(opcode_idx_options[idx]) == 1 and idx not in opcode_mapping:
            opcode_mapping[idx] = opcode_idx_options[idx][0]
            for jdx in range(len(opcode_idx_options)):
                if jdx != idx:
                    opcode_idx_options[jdx] = [kdx for kdx in opcode_idx_options[jdx] if kdx != opcode_mapping[idx]]
            break

program_registers = [0, 0, 0, 0]

for p in program:
    all_ops[opcode_mapping[p["opcode"]]](p["args"], program_registers)

print("Part 2: " + str(program_registers[0]))