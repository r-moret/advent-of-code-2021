import numpy as np

with open("Day6/input.txt") as file:
    text = file.read()

initial = [int(number) for number in text.split(",")]

initial_counts = np.full((9,), 0, dtype=np.int64)

for fish in initial:
    initial_counts[fish] = initial_counts[fish] + 1

# Just a re-think from the previous exercise to choose 
# the correct data structure to store the fish and 
# improve the performance! 
#
# With the previous code it was simply impossible to
# compute all the iterations...
# 
# To remember: The structure is always very important!
def simulate(iters: int, counts: np.array):
    for __ in range(iters):
        spawned = counts[0]

        counts = np.roll(counts, -1)
        counts[6] = counts[6] + spawned

    return counts


print(f"Answer = {simulate(256, initial_counts).sum()}")
