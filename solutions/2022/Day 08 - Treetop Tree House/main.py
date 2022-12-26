import sys

grid = [list(map(int, list(line))) for line in sys.stdin.read().split("\n")]

height = len(grid)
width = len(grid[0])
visible = [[False] * width for j in range(height)]
scenic = [[1 for i in range(width)] for j in range(height)]

position_lists = [[*zip(range(height), [i] * height)] for i in range(width)] +\
                 [[*zip(range(height - 1, -1, -1), [i] * height)] for i in range(width)] +\
                 [[*zip([i] * width, range(width))] for i in range(height)] +\
                 [[*zip([i] * width, range(width - 1, -1, -1))] for i in range(height)]

for position_list in position_lists:
    previous = [-1]
    for y, x in position_list:
        val = grid[y][x]
        if val > max(previous):
            visible[y][x] = True

        idx = 0
        for idx, prev_val in enumerate(previous[::-1][:-1]):
            if prev_val >= val:
                break
        scenic[y][x] *= idx + (1 if len(previous) > 1 else 0)
        previous.append(val)

print(sum([sum(row) for row in visible]))
print(max([max(row) for row in scenic]))