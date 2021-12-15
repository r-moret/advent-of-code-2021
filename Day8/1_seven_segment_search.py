import re

with open("Day8/input.txt") as file:
    text = file.read()

text = [entry.split("|")[1] for entry in text.split("\n")]

n_segments = {1: 2, 4: 4, 7: 3, 8: 7}

ocurrences = [
    {
        number: len(re.findall(r"\b[a-z]{" + str(segments) + r"}\b", output))
        for number, segments in n_segments.items()
    }
    for output in text
]
total = sum([sum(instance.values()) for instance in ocurrences])

print(f"Answer = {total}")