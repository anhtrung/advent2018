import os

dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, "input")) as f:
    puzzle_input = f.read()
#puzzle_input = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"
#puzzle_input = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
#puzzle_input = "^ESSWWN(E|NNENN(EESS(WNSE|)S(NNNNNN(WNNWE|SS)WWWW|S)SS|WWW(WN|E)SS(SSE(SW|NNNE)))|NN)$"
#puzzle_input = "^ENWWW(NEEE|SSE(EE|N))$"
#puzzle_input = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$)"
def get_path_length(path):
    if len(path) == 0:
        return 0
    brace_count = 0
    branch_idx = -1
    start_sub_idx =-1
    sub_paths = []
    non_enclosed_chars = 0
    for idx, char in enumerate(path):
        if char == '(':
            if brace_count == 0:
                start_sub_idx = idx
            brace_count += 1
        elif char == ')':
            brace_count -= 1
            if brace_count == 0:
                sub_paths.append(path[start_sub_idx+1:idx])
                start_sub_idx = -1
        elif char == '|' and brace_count == 0:
            # branch at this level
            branch_idx = idx
        elif brace_count == 0:
            non_enclosed_chars +=1

    if branch_idx != -1:
        branch_a_len = get_path_length(path[:branch_idx])
        branch_b_len = get_path_length(path[branch_idx+1:])
        if branch_a_len == 0 or branch_b_len == 0:
            return 0
        return max(branch_a_len, branch_b_len)

    sub_lengths = 0
    for sub in sub_paths:
        sub_lengths += get_path_length(sub)

    return non_enclosed_chars + sub_lengths


end_char = puzzle_input.find('$')
puzzle_input = puzzle_input[1:end_char]


last_coord = (0, 0)
rooms = {last_coord: 0}
branch_coords = []

for idx, char in enumerate(puzzle_input):
    last_dist = rooms[last_coord]
    x = last_coord[0]
    y = last_coord[1]
    if char in ['N', 'E', 'S', 'W']:
        if char == 'N':
            x -= 1
        elif char == 'E':
            y += 1
        elif char == 'S':
            x += 1
        elif char == 'W':
            y -= 1

        if (x, y) not in rooms:
            rooms[(x, y)] = last_dist + 1

        last_coord = (x, y)

    elif char == '(':
        branch_coords.append(last_coord)

    elif char == ')':
        last_coord = branch_coords[-1]
        branch_coords.pop()
 
    elif char == '|':
        last_coord = branch_coords[-1]


max_dist = max(rooms, key=lambda x: rooms[x])
print(rooms[max_dist])

rooms_1000 = sum([1 for key in rooms if rooms[key] >= 1000])
print(rooms_1000)