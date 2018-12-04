import os
from datetime import datetime
from collections import defaultdict

dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    input_data = f.read()
lines = input_data.splitlines()

shifts = [(datetime.strptime(l[1:17], '%Y-%m-%d %H:%M'), l[19:]) for l in lines]
shifts.sort(key=lambda t: t[0])

elf_stats = defaultdict(lambda: {"minute total": [0]*60})

for s in shifts:
    day_idx = (s[0] - shifts[0][0]).days
    if '#' in s[1]:
        last_elf = int((s[1][7:]).split(' ')[0])
    elif s[1] == 'falls asleep':            
        start_sleep = s[0].minute
    else:
        for m in range(start_sleep, s[0].minute):
            elf_stats[last_elf]["minute total"][m] += 1

for elf, stats in elf_stats.items():
    stats["total minutes"] = sum(stats["minute total"])
    stats["sleepiest minute count"] = max(stats["minute total"])
    stats["sleepiest minute"] = stats["minute total"].index(stats["sleepiest minute count"])

sleepiest_elf = max(elf_stats, key=lambda x: elf_stats[x]["total minutes"])
print("Part 1: " + str(sleepiest_elf*elf_stats[sleepiest_elf]["sleepiest minute"]))

sleepiest_elf = max(elf_stats, key=lambda x: elf_stats[x]["sleepiest minute count"])
print("Part 2: " + str(sleepiest_elf*elf_stats[sleepiest_elf]["sleepiest minute"]))
