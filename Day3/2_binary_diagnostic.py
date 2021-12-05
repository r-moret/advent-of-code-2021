from collections import Counter
from typing import List

with open("Day3/input.txt") as file:
    diagnostic = file.read()

diagnostic = [[int(bit) for bit in code] for code in diagnostic.split("\n")]
oxygen = co2 = diagnostic

for pos in range(len(diagnostic[0])):
    most_common_oxygen = (
        1 if sum(list(zip(*oxygen))[pos]) >= len(list(zip(*oxygen))[pos]) / 2 else 0
    )
    least_common_co2 = (
        0 if sum(list(zip(*co2))[pos]) >= len(list(zip(*co2))[pos]) / 2 else 1
    )

    oxygen = [
        code for code in oxygen if code[pos] == (most_common_oxygen) or len(oxygen) == 1
    ]
    co2 = [code for code in co2 if code[pos] == (least_common_co2) or len(co2) == 1]

oxygen = int("0b" + "".join([str(bit) for bit in oxygen[0]]), 2)
co2 = int("0b" + "".join([str(bit) for bit in co2[0]]), 2)

print(f"Answer = {oxygen * co2}")