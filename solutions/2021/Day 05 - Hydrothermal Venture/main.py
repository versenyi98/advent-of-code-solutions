import sys


def is_line(candidate):
    begin, end = candidate
    x1, y1 = begin
    x2, y2 = end

    return x1 == x2 or y1 == y2


def is_diagonal(candidate):
    begin, end = candidate
    x1, y1 = begin
    x2, y2 = end

    return abs(x1 - x2) == abs(y1 - y2)


lines = [line.split(" -> ") for line in sys.stdin.read().split("\n")]

for idx, value in enumerate(lines):
    lines[idx] = [list(map(int, entry.split(','))) for entry in value]

true_lines = list(filter(is_line, lines))
diagonals = list(filter(is_diagonal, lines))

covers = {}

for true_line in true_lines:
    begin, end = true_line
    x1, y1 = begin
    x2, y2 = end

    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if (x, y) not in covers:
                covers[(x, y)] = 0
            covers[(x, y)] += 1

print(len(list(filter(lambda x: x > 1, covers.values()))))

for diagonal_line in diagonals:
    begin, end = diagonal_line
    x1, y1 = begin
    x2, y2 = end

    step_x = 1 if x1 < x2 else -1
    step_y = 1 if y1 < y2 else -1

    for x, y in zip(range(x1, x2 + step_x, step_x), range(y1, y2 + step_y, step_y)):
        if (x, y) not in covers:
            covers[(x, y)] = 0
        covers[(x, y)] += 1

print(len(list(filter(lambda x: x > 1, covers.values()))))