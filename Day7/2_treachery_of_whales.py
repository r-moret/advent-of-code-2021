import numpy as np

with open("Day7/input.txt") as file:
    text = file.read()

position = [int(number) for number in text.split(",")]

# This needs a re-think, it has to be optimizable in some way...

def fuel(hole: int):
    return sum([np.arange(1, np.abs(crab - hole) + 1).sum() for crab in position])


used_fuel = min(map(fuel, np.arange(0, max(position) + 1)))
print(f"Answer = {used_fuel}")
