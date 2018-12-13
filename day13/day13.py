import os
dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    s = f.read().splitlines()

carts = []
dirs = ["<", "^", ">", "v"]
dirs_L = ["L", "U", "R", "D"]
map = []

for row, line in enumerate(s):
    map_line = ""
    for col, ch in enumerate(line):
        if ch in dirs:
            if ch == '>':
                dir = "R"
                re = "-"
            elif ch == "<":
                dir = "L"
                re = "-"
            elif ch == "^":
                dir = "U"
                re = "|"
            elif ch == "v":
                dir = "D"
            re = "|"
            carts.append({"row": row, "col": col, "dir": dir, "xs": 0})
            map_line += re
        else:
            map_line += ch

    map.append(map_line)

carts = sorted(carts, key=lambda x: (x["row"], x["col"]))
#print(carts)

for t in range(0, 1000000):
    carts = sorted(carts, key=lambda x: (x["row"], x["col"]))
    carts_to_remove = []
    for c in carts:
        if c["dir"] == "R":
            c["col"] += 1
        elif c["dir"] == "L":
            c["col"] -= 1
        elif c["dir"] == "U":
            c["row"] -= 1
        else:
            c["row"] += 1

        if map[c["row"]][c["col"]] == "/" and c["dir"] == "U":
            c["dir"] = "R"
        elif map[c["row"]][c["col"]] == "/" and c["dir"] == "D":
            c["dir"] = "L"
        elif map[c["row"]][c["col"]] == "/" and c["dir"] == "R":
            c["dir"] = "U"
        elif map[c["row"]][c["col"]] == "/" and c["dir"] == "L":
            c["dir"] = "D"
        elif map[c["row"]][c["col"]] == "\\" and c["dir"] == "U":
            c["dir"] = "L"
        elif map[c["row"]][c["col"]] == "\\" and c["dir"] == "D":
            c["dir"] = "R"
        elif map[c["row"]][c["col"]] == "\\" and c["dir"] == "R":
            c["dir"] = "D"
        elif map[c["row"]][c["col"]] == "\\" and c["dir"] == "L":
            c["dir"] = "U"

        elif map[c["row"]][c["col"]] == "+":
            turns = c["xs"] % 3
            d = dirs_L.index(c["dir"])
            if turns == 0:  # turn left
                c["dir"] = dirs_L[d - 1]
            elif turns == 2: # turn right
                c["dir"] = dirs_L[(d + 1) % len(dirs_L)]
            c["xs"] += 1

    # check for crashes
#    carts = sorted(carts, key=lambda x: (x["row"], x["col"]))
#    print(carts)

        for i, c in enumerate(carts):
            if i == 0:
                pass
            elif carts[i]["row"] == carts[i-1]["row"] and carts[i]["col"] == carts[i-1]["col"]:
                print(f"CRASH at time {t} at {c['col']},{c['row']}")
                carts_to_remove.append(i-1)
                carts_to_remove.append(i)
#                print(carts)
    for cr in sorted(set(carts_to_remove), reverse=True):
        print(carts[cr])
        carts.pop(cr)

    if len(carts) == 1:
        print("Last car")
        print(carts[0])
        break
#for m in map:
#    print(m)