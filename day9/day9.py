from collections import defaultdict

num_players = 471
last_marble_point = 72026

player_points = defaultdict(int)
current_marble_pos = 1
marble_circle = [0, 1]
current_player = 1

for m in range(2, last_marble_point + 1):
    current_player = (current_player + 1) % num_players
    if m % 23 == 0:
        player_points[current_player] += m
        remove_idx = current_marble_pos - 7
        if remove_idx < 0:
            remove_idx = len(marble_circle) + remove_idx
        player_points[current_player] += marble_circle[remove_idx]
        marble_circle.pop(remove_idx)
        current_marble_pos = remove_idx
    else:
        insert_pos = current_marble_pos + 2
        if insert_pos > len(marble_circle):
            insert_pos = insert_pos % len(marble_circle)
        marble_circle.insert(insert_pos, m)
        current_marble_pos = insert_pos

max_score = max(player_points.values())

print("Part 1: " + str(max_score))