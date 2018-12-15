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

    reachable_squares = []
    for sq in in_range_squares:
        d, step = get_distance_and_step(unit_to_move["coord"], sq, occupied_squares)
        if d is not None:
            reachable_squares.append({"coord": sq, "dist": d, "step": step})

    if len(reachable_squares) == 0:
        return None

    reachable_squares = sorted(reachable_squares, key=lambda sq: (sq["dist"], sq["coord"]))
    return reachable_squares[0]["step"]

def get_adjacent(square, occupied_squares=[]):
    adjacent = [
        (square[0], square[1]-1),
        (square[0], square[1]+1),
        (square[0]-1, square[1]),
        (square[0]+1, square[1])]
    return [sq for sq in adjacent if sq not in occupied_squares]

def get_distance_and_step(square_1, square_2, occupied_squares):
    step_squares = [[square_2]]
    all_squares = [square_2]
    while True:
        next_squares = []
        for sq in step_squares[-1]:
            next_adj = get_adjacent(sq, occupied_squares)
            if square_1 in next_adj:
                return len(step_squares), sq
            next_squares.extend(next_adj)

        next_squares = sorted(list(set([sq for sq in next_squares if sq not in all_squares])))
        if len(next_squares) == 0:
            return None, None

        step_squares.append(next_squares)
        all_squares.extend(next_squares)

# main
dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    puzzle_input = f.read().splitlines()

cave = []
units = []
for row, line in enumerate(puzzle_input):
    for col, ch in enumerate(line):
        if ch == "E" or ch == "G":
            units.append({"type": ch, "coord": (row, col), "hp": 200, "attack": 3})
        elif ch == "#":
            cave.append((row, col))

combat = True
for round in range(0, 500):
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
                print("Death!")
                active_units.remove(targets_in_range[0])

    units = active_units
    if not combat:
        break


#print(round)
units = (sorted(units, key=lambda u: u["coord"]))
for u in units:
    print(u)

hp_sum = sum([u["hp"] for u in units])
print(f"Part 1: {round*hp_sum}")
