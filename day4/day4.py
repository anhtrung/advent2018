import os
import numpy as np
from datetime import datetime
from collections import defaultdict


dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    input_data = f.read()
lines = input_data.splitlines()

shifts = [(datetime.strptime(l[1:17], '%Y-%m-%d %H:%M'), l[19:]) for l in lines]
shifts.sort(key=lambda t: t[0])

schedule = np.empty(((shifts[-1][0] - shifts[0][0]).days + 1, 60))
schedule[:] = np.nan

for s in shifts:
    day_idx = (s[0] - shifts[0][0]).days
    if '#' in s[1]:
        last_elf = int((s[1][7:]).split(' ')[0])
    elif s[1] == 'falls asleep':            
        start_sleep = s[0].minute
    else:
        schedule[day_idx, start_sleep:s[0].minute] = last_elf

counts = np.array(np.unique(schedule, return_counts = True))
sleepiest_elf = int(counts[0, np.argmax(counts, axis=1)[1]])

sleepy_schedule = schedule == sleepiest_elf
sleepiest_minute = np.argmax(np.sum(sleepy_schedule, axis=0))
print("Part 1: " + str(sleepiest_elf*sleepiest_minute))

