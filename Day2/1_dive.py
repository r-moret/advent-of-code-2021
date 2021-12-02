import time

start = time.time()

with open("Day2/input.txt") as file:
    course = file.read()

course = course.split("\n")

forward, up, down = zip(
    *[
        (int(args[1]), 0, 0)
        if (args := command.split(" "))[0] == "forward"
        else (0, int(args[1]), 0)
        if args[0] == "up"
        else (0, 0, int(args[1]))
        for command in course
    ]
)

print(f"Answer = {sum(forward) * (sum(down) - sum(up))}")