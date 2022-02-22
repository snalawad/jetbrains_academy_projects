initial_atoms = int(input())
final_atoms = int(input())

half_life_cycles = 0
period = 12

while initial_atoms >= final_atoms:
    initial_atoms /= 2
    half_life_cycles += 1
print(period * half_life_cycles)
