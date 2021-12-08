import re
import numpy as np

from typing import Tuple
from itertools import product

with open("Day5/input.txt") as file:
    text = file.read()

lines = text.split("\n")

numbers = [re.findall(r"[0-9]+", line) for line in lines]
numbers = [(int(x1), int(y1), int(x2), int(y2)) for x1, y1, x2, y2 in numbers]

x1, y1, x2, y2 = zip(*numbers)

upper_xlim = max(max(x1), max(x2))
lower_xlim = min(min(x1), min(x2))
upper_ylim = max(max(y1), max(y2))
lower_ylim = min(min(y1), min(y2))

diagram = np.full((upper_xlim - lower_xlim + 1, upper_ylim - lower_ylim + 1), 0)


def vent_line(vent_points: Tuple[int, int, int, int]):
    x1, y1, x2, y2 = vent_points

    step = 1
    if y1 > y2:
        step = -1
    p_y = range(y1, y2 + step, step)

    step = 1
    if x1 > x2:
        step = -1
    p_x = range(x1, x2 + step, step)

    if len(p_x) != len(p_y):
        points = [(x, y) for x,y in product(p_x, p_y)]
    else:
        points = [(x, y) for x,y in zip(p_x, p_y)]

    return points


line_points = map(vent_line, numbers)
line_points = [point for points in line_points for point in points]

for point in line_points:
    relative_point = (point[1] - lower_ylim, point[0] - lower_xlim)
    diagram[relative_point] = diagram[relative_point] + 1

print(f"Answer = {(diagram >=2).sum()}")
