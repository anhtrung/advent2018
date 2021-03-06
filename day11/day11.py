import numpy as np

serial_number = 8199

x_coords = np.arange(1, 301).reshape(-1, 1)
y_coords = np.arange(1, 301).reshape(1, -1)

fuel_cells = np.dot(x_coords + 10, y_coords)
fuel_cells += serial_number
fuel_cells *= x_coords + 10
fuel_cells = fuel_cells//100
fuel_cells = fuel_cells % 10
fuel_cells -= 5

total_power = np.zeros((x_coords.size - 2, y_coords.size - 2))

for x in range(x_coords.size - 2):
    for y in range(y_coords.size - 2):
        total_power[x, y] = np.sum(fuel_cells[x:x+3, y:y+3])

ind = np.unravel_index(np.argmax(total_power, axis=None), total_power.shape)

print(f"Part 1: {ind[0] + 1},{ind[1] + 1}")

max_square_side = 300
total_total_power = np.zeros((x_coords.size, y_coords.size, max_square_side))

for s in range(1, max_square_side + 1):
    print(s)
    for x in range(x_coords.size - s + 1):
        for y in range(y_coords.size - s + 1):
            total_total_power[x, y, s - 1] = np.sum(fuel_cells[x:x+s, y:y+s])

ind = np.unravel_index(np.argmax(total_total_power, axis=None), total_total_power.shape)

print(f"Part 2: {ind[0] + 1},{ind[1] + 1},{ind[2] + 1}")

