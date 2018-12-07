import os
from collections import defaultdict
import string


def completed_presteps(pre_steps, completed):
    for letter in pre_steps:
        if letter not in completed:
            return False
    return True

def next_todo(rules, completed, available):
    for letter in sorted(available):
        if letter not in rules and letter in available:
            return letter
        elif completed_presteps(rules[letter], completed) and letter in available:
            return letter
    return None


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

schedule = [
    {"step": None, "endtime":-1},
    {"step": None, "endtime":-1},
    {"step": None, "endtime":-1},
    {"step": None, "endtime":-1},
    {"step": None, "endtime":-1}
    ]
in_progress = []
completed_steps = []
time = None

while len(completed_steps) < len(alphabet):
    time = 0 if time == None else min([val["endtime"] for val in schedule if val["endtime"] >= 0])
    
    for worker_job in schedule:
        if worker_job["endtime"] == time:   # just finished, add to completed
            completed_steps.append(worker_job["step"])
            in_progress.remove(worker_job["step"])
            worker_job["step"] = None
            worker_job["endtime"] = -1

    for worker_job in schedule:
        if worker_job["endtime"] <= time:
            available_steps = [a for a in alphabet if a not in completed_steps and a not in in_progress]  
            next_step = next_todo(rules, completed_steps, available_steps)
            if next_step is not None:
                worker_job["step"] = next_step
                worker_job["endtime"] = time + 60 + ord(next_step) - ord('A') + 1
                in_progress.append(next_step)
            else:   # nothing can be started now
                break

print('Part 2: ' + str(time))