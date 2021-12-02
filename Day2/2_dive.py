from itertools import accumulate

with open("Day2/input.txt") as file:
    course = file.read()

course = course.split("\n")

# (delta horizontal, delta aim)
d_horiz, d_aims = zip(
    *[
        (int(args[1]), 0)
        if ((args := command.split(" "))[0] == "forward")
        else (0, -int(args[1]))
        if (args[0] == "up")
        else (0, int(args[1]))
        for command in course
    ]
)

d_horiz, d_depth = zip(
    *[(hor, hor * aim) for hor, aim in zip(d_horiz, accumulate(d_aims))]
)

print(f"Answer = {sum(d_horiz) * sum(d_depth)}")