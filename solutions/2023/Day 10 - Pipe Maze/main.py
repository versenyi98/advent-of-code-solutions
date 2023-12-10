from collections import Counter
import sys

symbol_to_diff = {
    '|': [(+1, 0), (-1, 0)],
    '-': [(0, +1), (0, -1)],
    'L': [(-1, 0), (0, +1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(+1, 0), (0, -1)],
    'F': [(+1, 0), (0, +1)],
}

def dfs(grid, row, col):
    queue = [(row, col)]

    while len(queue):
        row, col = queue[0]
        queue = queue[1:]

        if row < 0 or row >= len(grid):
            continue
        if col < 0 or col >= len(grid[0]):
            continue

        if grid[row][col] == '#':
            continue

        grid[row][col] = '#'

        for r in range(-1, 2):
            for c in range(-1, 2):
                if abs(r) + abs(c) == 1:
                    queue.append((row + r, col + c))

def find_cycle(grid, pos):
    start_pos = pos
    states = [(pos, None, 0, [])]

    saved_states = []

    while len(states):
        state = states[0]
        position, prev_pos, result, positions = state
        states = states[1:]
        row, col = position

        if result and position == start_pos:
            saved_states.append(state)
            continue

        if row == len(grid) or row < 0:
            continue

        if col == len(grid[0]) or col < 0:
            continue

        symbol = grid[row][col]

        if symbol not in symbol_to_diff:
            continue

        pos1 = (row + symbol_to_diff[symbol][0][0], col + symbol_to_diff[symbol][0][1])
        pos2 = (row + symbol_to_diff[symbol][1][0], col + symbol_to_diff[symbol][1][1])

        if prev_pos != pos1:
            states.append((pos1, position, result + 1, positions + [position]))
        if prev_pos != pos2:
            states.append((pos2, position, result + 1, positions + [position]))

    if len(saved_states) == 2 and saved_states[0][2] == saved_states[1][2]:
        return (saved_states[0][2], saved_states[0][3])
    return None

def decrease_resolution(grid):
    return ["".join(line[::2]) for line in grid[::2]]

def increase_resolution(grid):
    result = [[] for _ in range(len(grid) * 2)]

    for i, line in enumerate(grid):
        for entry in line:
            result[2 * i] += [entry, '.']
            result[2 * i + 1] += ['.'] * 2

    return result


def main():
    lines = [line.strip('\n') for line in sys.stdin.readlines()]

    for c, line in enumerate(lines):
        if 'S' in line:
            row = c
            col = line.find('S')
            break

    for possible_type in ['|', '-', 'L', 'J', '7', 'F']:
        lines[row] = lines[row][:col] + possible_type + lines[row][col + 1:]
        result = find_cycle(lines, (row, col))

        if result:
            break

    cycle_length, positions = result
    print(possible_type, cycle_length // 2)

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

    inner = len([dot for dot in "".join(decreased) if dot == "."])
    print(inner)

if __name__ == "__main__":
    main()