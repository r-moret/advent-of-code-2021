with open("Day3/input.txt") as file:
    diagnostic = file.read()

diagnostic = diagnostic.split("\n")

gamma = [
    "1" if sum([int(bit) for bit in bits]) > (len(bits) / 2) else "0"
    for bits in list(zip(*diagnostic))
]
gamma = int("0b" + "".join(gamma), 2)

epsilon = (2 ** 12 - 1) - gamma

print(f"Answer = {gamma * epsilon}")