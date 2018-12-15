import os

def get_target_type(unit):
    return "G" if unit["type"] == "E" else "E"

def get_targets_in_range(unit, targets):
    tir = [t for t in targets if t["coord"] in get_adjacent(unit["coord"])]
    return sorted(tir, key=lambda t: (t["hp"], t["coord"]))

def get_chosen_move(unit_to_move, units, cave):
    occupied_squares = [u["coord"] for u in units]
    occupied_squares.extend(cave)
    occupied_squares.remove(unit_to_move["coord"])

    target_list = [u for u in units if u["type"] == get_target_type(unit_to_move)]

    in_range_squares = []
    for t in target_list:
        in_range_squares.extend(get_adjacent(t["coord"], occupied_squares))

    return get_move_in_range(unit_to_move["coord"], in_range_squares, occupied_squares)

def get_adjacent(square, occupied_squares=[]):
    adjacent = [
        (square[0]-1, square[1]),
        (square[0], square[1]-1),
        (square[0], square[1]+1),
        (square[0]+1, square[1])]
    return [sq for sq in adjacent if sq not in occupied_squares]

def get_move_in_range(start_square, target_squares, occupied_squares):
    max_row = max(occupied_squares, key=lambda x: x[0])[0]
    max_col = max(occupied_squares, key=lambda x: x[1])[1]

    paths = []
    for r in range(max_row):
        paths.append([])
        for c in range(max_col):
            paths[r].append([])
        
    paths[start_square[0]][start_square[1]] = [start_square]

    step_squares = [[start_square]]

    while True:
        added_squares = []

        for sq in step_squares[-1]:
            next_squares = get_adjacent(sq, occupied_squares)
            for next_sq in next_squares:
                if len(paths[next_sq[0]][next_sq[1]]) == 0:
                    paths[next_sq[0]][next_sq[1]] = paths[sq[0]][sq[1]] + [next_sq]
                    added_squares.append(next_sq)

        if len(added_squares) == 0:
            break

        reached_targets = True
        for target in target_squares:
            if len(paths[target[0]][target[1]]) == 0:
                reached_targets = False
                break

        if reached_targets:
            break
        
        step_squares.append(added_squares)
    
    target_paths = [paths[target[0]][target[1]] for target in target_squares if len(paths[target[0]][target[1]]) != 0]

    if len(target_paths) == 0:
        return None # no targets are reachable
    
    target_paths = sorted(target_paths, key=lambda t: (len(t), t[1][0], t[1][1]))

    return target_paths[0][1]


def play_game(cave, units):

    combat = True
    elf_deaths = 0
    goblin_deaths = 0
    for round in range(0, 100):
        # sort units into reading order
        units = sorted(units, key=lambda u: (u["coord"]))
        active_units = list(units)

        for u in units:
            if u["hp"] <= 0:
                continue

            target_type = get_target_type(u)
            targets = list(filter(lambda u: u["type"]== target_type, active_units))

            if len(targets) == 0:
                print("Combat ends!")
                combat = False
                break

            targets_in_range = get_targets_in_range(u, targets)

            if len(targets_in_range) == 0:
                # move
                move = get_chosen_move(u, active_units, cave)

                if move is None:
                    continue

                u["coord"] = move
                targets_in_range = get_targets_in_range(u, targets)

            if len(targets_in_range) > 0:
                targets_in_range[0]["hp"] -= u["attack"]
                if targets_in_range[0]["hp"] <= 0:
                    if targets_in_range[0]["type"] == "E":
#                        print("Elf death!")
                        elf_deaths += 1
                    else:
#                        print("Goblin death!")
                        goblin_deaths += 1

                    active_units.remove(targets_in_range[0])

        units = active_units
        if not combat:
            break

    hp_sum = sum([u["hp"] for u in units])
    print(f"Part 1: {round*hp_sum}")

    return elf_deaths

# main
dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    puzzle_input = f.read().splitlines()

for a in range(4, 100):

    attack_vals = {"E": a, "G": 3}

    cave = []
    units = []
    for row, line in enumerate(puzzle_input):
        for col, ch in enumerate(line):
            if ch == "E" or ch == "G":
                units.append({"type": ch, "coord": (row, col), "hp": 200, "attack": attack_vals[ch]})
            elif ch == "#":
                cave.append((row, col))

    elf_deaths = play_game(cave, units)
    print(f"Elf deaths with attack {a}: {elf_deaths}")
    if elf_deaths == 0:
        break
