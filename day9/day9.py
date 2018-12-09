from collections import defaultdict

num_players = 471
last_marble_point = 7202600

player_points = defaultdict(int)
current_marble = 0

circle = {0: {"prev": 0, "next": 0}}

current_player = 1

for m in range(1, last_marble_point + 1):
    current_player = (current_player + 1) % num_players
    if m % 23 == 0:
        player_points[current_player] += m
        for i in range(0, 7):
            current_marble = circle[current_marble]["prev"]
        player_points[current_player] += current_marble
        circle[circle[current_marble]["prev"]]["next"] = circle[current_marble]["next"]
        circle[circle[current_marble]["next"]]["prev"] = circle[current_marble]["prev"]
        current_marble = circle[current_marble]["next"]

    else:
        new_marble_prev = circle[current_marble]["next"]
        new_marble_next = circle[new_marble_prev]["next"]
        circle[circle[circle[current_marble]["next"]]["next"]]["prev"] = m
        circle[circle[current_marble]["next"]]["next"] = m        
        circle[m] = {"prev": new_marble_prev, "next": new_marble_next}
        current_marble = m

max_score = max(player_points.values())

print("Part 1: " + str(max_score))