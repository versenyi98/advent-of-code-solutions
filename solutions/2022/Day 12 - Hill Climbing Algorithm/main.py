import sys


def get_height(char):
    if char.isupper():
        char = {'S' : 'a', 'E' : 'z'}[char]
    return ord(char) - ord('a')


lines = sys.stdin.read().split("\n")

part1, end_pos = None, None
part2 = []
for row_idx, row in enumerate(lines):
    if "S" in row:
        part1 = (row_idx, row.find("S"))
    if "E" in row:
        end_pos = (row_idx, row.find("E"))

    for idx, char in enumerate(row):
        if char == 'a' or char == 'S':
            part2.append((row_idx, idx))

grid = [list(row) for row in lines]
height_map = [list(map(get_height, row)) for row in grid]

height = len(lines)
width = len(lines[0])
directions = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

for start_positions in [[part1], part2]:
    visited = set()
    queue = [(start_pos, 0) for start_pos in start_positions]

    while queue:
        pos, steps = queue.pop(0)
        y, x = pos

        if pos in visited:
            continue
        visited.add(pos)

        if grid[y][x] == 'E':
            print(steps)
            break

        current_height = height_map[y][x]
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            npos = (ny, nx)
            if height > ny >= 0 and 0 <= nx < width and npos not in visited:
                nheight = height_map[ny][nx]
                if nheight - current_height <= 1:
                    queue.append((npos, steps + 1))