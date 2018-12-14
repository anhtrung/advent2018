elf_1_idx = 0
elf_2_idx = 1

recipes = [3, 7]
puzzle_input = 440231
puzzle_input_list = [4, 4, 0, 2, 3, 1]


for i in range(552860567+20):
    new_recipe = recipes[elf_1_idx] + recipes[elf_2_idx]
    if new_recipe >= 10:
        recipes.append(1)
    recipes.append(new_recipe % 10)

    elf_1_idx = (elf_1_idx + 1 + recipes[elf_1_idx]) % len(recipes)
    elf_2_idx = (elf_2_idx + 1 + recipes[elf_2_idx]) % len(recipes)

    if recipes[-len(puzzle_input_list)-1:-1] == puzzle_input_list:
        print("Part 2: " + str(len(recipes) - len(puzzle_input_list) - 1))
        break

    if recipes[-len(puzzle_input_list):] == puzzle_input_list:
        print("Part 2: " + str(len(recipes) - len(puzzle_input_list)))
        break

part1_answer = ''.join(str(x) for x in recipes[puzzle_input:puzzle_input+10])

print("Part 1: " + part1_answer)
