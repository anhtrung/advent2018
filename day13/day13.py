import os

dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    input_map = f.read().splitlines()

dirs = ["<", "^", ">", "v"]
map = []
carts = []

def turn_left(dir):
    d = dirs.index(dir)
    return dirs[d - 1]

def turn_right(dir):
    d = dirs.index(dir)
    return dirs[(d + 1) % len(dirs)]

for row, line in enumerate(input_map):
    map_line = ""
    for col, ch in enumerate(line):
        if ch in dirs:
            if ch == '>' or '<':
                re = '-'
            elif ch == '^' or 'v':
                re = "|"
            carts.append({"row": row, "col": col, "dir": ch, "xs": 0})
            map_line += re
        else:
            map_line += ch
    map.append(map_line)

for t in range(0, 1000000):
    carts = sorted(carts, key=lambda x: (x["row"], x["col"]))
    crashed_carts_idx = []

    for c in carts:
        if c["dir"] == ">":
            c["col"] += 1
        elif c["dir"] == "<":
            c["col"] -= 1
        elif c["dir"] == "^":
            c["row"] -= 1
        elif c["dir"] == "v":
            c["row"] += 1

        if ((map[c["row"]][c["col"]] == "/" and c["dir"] == "^") or 
        (map[c["row"]][c["col"]] == "/" and c["dir"] == "v") or
        (map[c["row"]][c["col"]] == "\\" and c["dir"] == ">") or 
        (map[c["row"]][c["col"]] == "\\" and c["dir"] == "<")):
            c["dir"] = turn_right(c["dir"])
        elif ((map[c["row"]][c["col"]] == "/" and c["dir"] == ">") or
        (map[c["row"]][c["col"]] == "/" and c["dir"] == "<") or  
        (map[c["row"]][c["col"]] == "\\" and c["dir"] == "^") or
        (map[c["row"]][c["col"]] == "\\" and c["dir"] == "v")):
            c["dir"] = turn_left(c["dir"])
        elif map[c["row"]][c["col"]] == "+":
            turns = c["xs"] % 3
            if turns == 0:  # turn left
                c["dir"] = turn_left(c["dir"])
            elif turns == 2: # turn right
                c["dir"] = turn_right(c["dir"])
            c["xs"] += 1

        # check for crashes
        for i in range(1, len(carts)):
            if carts[i]["row"] == carts[i-1]["row"] and carts[i]["col"] == carts[i-1]["col"]:
                print(f"Crash at tick {t} at {c['col']},{c['row']}")
                crashed_carts_idx.append(i)
                crashed_carts_idx.append(i-1)

    # remove crashed carts
    for cr in sorted(set(crashed_carts_idx), reverse=True):
        carts.pop(cr)

    if len(carts) == 1:
        print(f"Last car: {carts[0]['col']},{carts[0]['row']}")
        break
