import numpy as np

from functools import partial
from io import StringIO
from typing import Tuple

with open("Day4/input.txt") as file:
    text = file.readlines()

    first_line = text[0].rstrip("\n")
    sequence = [int(number) for number in first_line.split(",")]

    block_lines = range(2, len(text), 6)
    blocks = ["".join(text[line : line + 5]) for line in block_lines]

    matrices = np.array([np.loadtxt(StringIO(block)) for block in blocks], dtype=int)
    drawn = np.full(matrices.shape, False)


def draw_number(number: int, block: Tuple):
    matrix, drawn = block

    drawn[np.where(matrix == number)] = True

    full_column = drawn.all(axis=0).any()
    full_row = drawn.all(axis=1).any()

    exists_winner = full_column or full_row

    return exists_winner


for n in sequence:
    draw_n = partial(draw_number, n)
    is_winner = list(map(draw_n, zip(matrices, drawn)))

    if any(is_winner):
        winner = is_winner.index(True)
        winner_matrix = matrices[winner]
        winner_drawn = drawn[winner]
        winner_n = n

    is_loser = [not win for win in is_winner]

    matrices = matrices[is_loser]
    drawn = drawn[is_loser]

unmarked_sum = winner_matrix[np.where(winner_drawn == False)].sum()
print(f"Answer = {winner_n * unmarked_sum}")