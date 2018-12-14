elf_1_idx = 0
elf_2_idx = 1


recipes = [3, 7]
puzzle_input = 440231

for i in range(0, puzzle_input + 10):
    new_recipe = recipes[elf_1_idx] + recipes[elf_2_idx]
    if new_recipe >= 10:
        recipes.append(1)
    recipes.append(new_recipe % 10)

    elf_1_idx = (elf_1_idx + 1 + recipes[elf_1_idx]) % len(recipes)
    elf_2_idx = (elf_2_idx + 1 + recipes[elf_2_idx]) % len(recipes)

print(recipes[puzzle_input:puzzle_input+10])