import numpy as np

with open("Day7/input.txt") as file:
    text = file.read()

position = np.array([int(number) for number in text.split(",")])

# A bit of statistics!: 
# The fuel that we want to minimize is
# the Sum of Absolute Error between every
# crab and the position of the hole.
#
# As SAE and MAE (Mean of Absolute Error) minimize 
# in the same value, and we know that the value that
# minimizes MAE is the median of the distribution...
#
# We got it!

minimum = np.floor(np.median(position))
fuel = int(np.abs(position - minimum).sum())

print(f"Answer = {fuel}")