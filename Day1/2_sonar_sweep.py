from itertools import pairwise

with open("Day1/input.txt", "r") as file:
    depths = file.read()

depths = [int(depth) for depth in depths.split("\n")]

tri_sums = [a + b + c for a, b, c in zip(depths, depths[1:], depths[2:])]

increased = [1 if (second - first) > 0 else 0 for first, second in pairwise(tri_sums)]
n_increased = sum(increased)

print(f"Answer = {n_increased}")