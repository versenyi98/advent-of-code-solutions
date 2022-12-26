import sys


def part1(lines):
    depth = 0
    horizontal = 0

    for line in lines:
        direction, value = line.split()

        if direction == "forward":
            horizontal += int(value)
        else:
            depth += int(value) * (1 if direction == "down" else -1)

    return depth * horizontal


def part2(lines):
    depth = 0
    horizontal = 0
    aim = 0

    for line in lines:
        direction, value = line.split()
        if direction == "forward":
            horizontal += int(value)
            depth += int(value) * aim
        else:
            aim += int(value) * (1 if direction == "down" else -1)
    return depth * horizontal


lines = sys.stdin.read().split("\n")
print(part1(lines))
print(part2(lines))
