from typing import List

with open("Day6/input.txt") as file:
    text = file.read()

fish = [int(number) for number in text.split(",")]


def simulate(iters: int, initial: List[int]):
    state = initial

    for __ in range(iters):
        creators = list(filter(lambda fish: fish == 0, state))

        state = [(fish - 1) if fish != 0 else 6 for fish in state]
        state = state + [8] * len(creators)

    return state


print(f"Answer = {len(simulate(80, fish))}")
