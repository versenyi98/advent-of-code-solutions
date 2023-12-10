import sys
import re

from collections import Counter
from pathlib import Path

symbol_to_diff = {
    '|': [(+1, 0), (-1, 0)],
    '-': [(0, +1), (0, -1)],
    'L': [(-1, 0), (0, +1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(+1, 0), (0, -1)],
    'F': [(+1, 0), (0, +1)],
}



def dfs(grid, row, col):
    if row < 0 or row >= len(grid):
        return
    if col < 0 or col >= len(grid[0]):
        return

    if grid[row][col] == '#':
        return

    grid[row][col] = '#'

    for r in range(-1, 2):
        for c in range(-1, 2):
            if abs(r) + abs(c) == 1:
                dfs(grid, row + r, col + c)

def find_cycle(grid, pos, start_pos, prev_pos, result, positions):
    row, col = pos
    if result and pos == start_pos:
        return result

    if row == len(grid) or row < 0:
        return -1

    if col == len(grid[0]) or col < 0:
        return -1

    positions += [pos]
    symbol = grid[row][col]

    if symbol not in symbol_to_diff:
        return -1

    pos1 = (row + symbol_to_diff[symbol][0][0], col + symbol_to_diff[symbol][0][1])
    pos2 = (row + symbol_to_diff[symbol][1][0], col + symbol_to_diff[symbol][1][1])

    if prev_pos == None:
        res1 = find_cycle(grid, pos1, start_pos, pos, result + 1, positions)
        res2 = find_cycle(grid, pos2, start_pos, pos, result + 1, [])
        if res1 == res2:
            return res1
        else:
            return -1
    if prev_pos == pos1:
        return find_cycle(grid, pos2, start_pos, pos, result + 1, positions)
    else:
        return find_cycle(grid, pos1, start_pos, pos, result + 1, positions)

def decrease_resolution(grid):
    return ["".join(line[::2]) for line in grid[::2]]

def increase_resolution(grid):
    result = [[] for i in range(len(grid) * 2)]

    for i, line in enumerate(grid):
        for entry in line:
            result[2 * i] += [entry, '.']
            result[2 * i + 1] += ['.'] * 2

    return result


def main():
    sys.setrecursionlimit(150000)
    with open(Path(__file__).parent / 'in') as in_:
        lines = [line.strip('\n') for line in in_.readlines()]

    for c, line in enumerate(lines):
        if 'S' in line:
            row = c
            col = line.find('S')
            break

    for possible_type in ['|', '-', 'L', 'J', '7', 'F']:
        positions = []
        lines[row] = lines[row][:col] + possible_type + lines[row][col + 1:]
        length = find_cycle(lines, (row, col), (row, col), None, 0, positions)
        if length != -1:
            print(possible_type, length // 2)
            break
    
    for row_num, row in enumerate(lines):
        for col_num, col in enumerate(row):
            if (row_num, col_num) in positions:
                continue
            lines[row_num] = lines[row_num][:col_num] + '.' + lines[row_num][col_num + 1:]

    increased = increase_resolution(lines)

    for idx in range(len(positions)):
        current = positions[idx]
        next = positions[(idx + 1) % len(positions)]

        increased[current[0] + next[0]][current[1] + next[1]] = '#'
        increased[2 * current[0]][2 * current[1]] = '#'

    for row_idx in range(len(increased)):
        dfs(increased, row_idx, 0)
        dfs(increased, row_idx, len(increased[0]) - 1)

    for col_idx in range(len(increased[0])):
        dfs(increased, 0, col_idx)
        dfs(increased, len(increased) - 1, col_idx)

    decreased = decrease_resolution(increased)
    inner = 0

    for line in decreased:
        inner += Counter(line).get('.', 0)
    print(inner)

if __name__ == "__main__":
    main()