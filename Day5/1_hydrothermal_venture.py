import re

import numpy as np
from typing import Tuple

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

    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        points = [(x1, y) for y in range(y1, y2 + 1)]
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        points = [(x, y1) for x in range(x1, x2 + 1)]
    else:
        points = []

    return points


line_points = map(vent_line, numbers)
line_points = [point for points in line_points for point in points]

for point in line_points:
    relative_point = (point[1] - lower_ylim, point[0] - lower_xlim)
    diagram[relative_point] = diagram[relative_point] + 1

print(f"Answer = {(diagram >=2).sum()}")
