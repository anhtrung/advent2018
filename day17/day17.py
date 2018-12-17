import os
import re


def print_world(world):
    print('\n\n\n')
    x_min = min(world, key=lambda coord: coord[0])[0]
    x_max = max(world, key=lambda coord: coord[0])[0]
    y_min = min(world, key=lambda coord: coord[1])[1]
    y_max = max(world, key=lambda coord: coord[1])[1]
    world_array = []
    
    for _ in range(y_min, y_max + 1):
        world_array.append([])
        for _ in range(x_min, x_max + 1):
            world_array[-1].append('.')

    for xy in world:
        world_array[xy[1]-y_min][xy[0]-x_min] = world[xy]

    for i, row in enumerate(world_array):
        print(f"{i+y_min:04d} " + ''.join(row) + '' + str(x_max))


def fill(world, spring, y_max, completed_springs):
    count = 0
    for tile in world:
        if tile[1] >= y_min and tile[1] <= y_max:
            if world[tile] in ['~', '|']:
                count += 1

    print(count)

    while True:
    #    print_world(world)
        new_springs = []
        x, y = spring
        while True:
            tile_below = world.get((x, y+1), '.')
            if tile_below in ['#', '~']:
                if world.get((x, y), '.') in ['~']:
                    completed_springs.append(spring)
                    return
                break
            y += 1
            if y > y_max or tile_below == '|':
                for yy in range(spring[1], y):
                    world[(spring[0], yy)] = '|'
                completed_springs.append(spring)
                return

        left = x
        right = x

        while world.get((left-1, y), '.') != '#' and world.get((left, y+1), '.') in ['#', '~']:            
            left -= 1
            if world.get((left, y+1), '.') == '.':
                if (left, y) not in completed_springs:
                    new_springs.append((left, y))
                break

        while world.get((right+1, y), '.') != '#' and world.get((right, y+1), '.') in ['#', '~']:      
            right += 1
            if world.get((right, y+1), '.') == '.':
                if (right, y) not in completed_springs:
                    new_springs.append((right, y))
                break

        if len(new_springs) == 0:
            for x in range(left, right+1):
                world[(x, y)] = '~'
        else:
            for x in range(left, right+1):
                world[(x, y)] = '|'

            for ns in new_springs:
                fill(world, ns, y_max, completed_springs)

    return


def old_fill(world, spring, completed_springs):
    count = 0

    for tile in world:
        if world[tile] in ['~', '|']:
            count += 1

    print(count)

 #   if count == 24191:
 #       print_world(world)

    while True:
        new_springs = []
        x, y = spring
        # find y-level to fill
        while world.get((x, y+1), '.') not in ['#', '~']:
            y += 1
            if y > y_max:
                for y_coord in range(spring[1]+1, y):
                    world[spring[0], y_coord] = '|'
                completed_springs.append(spring)
                return
        
        if world[x, y+1] == '|':
            completed_springs.append(spring)
            return

        if (x, y) == spring:
            completed_springs.append(spring)
            return
        
        left = x
        right = x
        while world.get((left-1, y), '.') != '#':
            if world.get((left-1, y+1), '.') in ['#', '~']:
                left -= 1
            elif world.get((left-1, y+1), '.') == '.':
                if (left-1, y) not in completed_springs:
                    new_springs.append((left-1, y))
                break
            else:
                completed_springs.append(spring)
                return
        while world.get((right+1, y), '.') != '#':
            if world.get((right+1, y+1), '.') in ['#', '~']:
                right += 1
            elif world.get((right+1, y+1), '.') == '.':
                if (right+1, y) not in completed_springs:
                    new_springs.append((right+1, y))
                break
            else:
                completed_springs.append(spring)
                return

        for x_coord in range(left, right+1):
            fill_char = '|' if len(new_springs) > 0 else '~'
            world[x_coord, y] = fill_char

#        print_world(world)

        for ns in new_springs:
            world[ns] = '|'

#        print_world(world)


        if len(new_springs) > 0:
            for y_coord in range(spring[1]+1, y):
                world[spring[0], y_coord] = '|'
            
#            print_world(world)

            for ns in new_springs:
#                print_world(world)
                old_fill(world, ns, completed_springs)
#                print_world(world)

    return


#############


dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    puzzle_input = f.read().splitlines()

world = {}

for line in puzzle_input:
    m = re.match(r"([xy])=(\d+), ([xy])=(\d+)..(\d+)", line)
    if m:
        a = m.group(1)
        aval = int(m.group(2))
        b = m.group(3)
        bval = (int(m.group(4)), int(m.group(5)) + 1)
        if a == 'x':
#            if bval[0] > 500:
#                continue
            for y in range(*bval):
                world[(aval, y)] = '#'
        else:
#            if aval > 500:
#                continue
            for x in range(*bval):
                world[(x, aval)] = '#'

y_min = min(world, key=lambda coord: coord[1])[1]
y_max = max(world, key=lambda coord: coord[1])[1]
water_spring = (500, 0)


print_world(world)
completed_springs = []
fill(world, water_spring, y_max, completed_springs)

print_world(world)

count = 0
for tile in world:
    if tile[1] >= y_min and tile[1] <= y_max:
        if world[tile] in ['~', '|']:
            count += 1

print(count)