import sys

def get_new_directions(direction, symbol):
    # direction we used to arrive at current position
    # symbol at current position
    # new directions after encountering symbol
    mapping = {
        # |
        ((0, +1), '|') : [(+1, 0), (-1, 0)],
        ((0, -1), '|') : [(+1, 0), (-1, 0)],
        # -
        ((+1, 0), '-') : [(0, +1), (0, -1)],
        ((-1, 0), '-') : [(0, +1), (0, -1)],
        # /
        ((+1, 0), '/') : [(0, -1)],
        ((0, -1), '/') : [(+1, 0)],
        ((-1, 0), '/') : [(0, +1)],
        ((0, +1), '/') : [(-1, 0)],
        # \
        ((+1, 0), '\\') : [(0, +1)],
        ((0, +1), '\\') : [(+1, 0)],
        ((-1, 0), '\\') : [(0, -1)],
        ((0, -1), '\\') : [(-1, 0)]
    }
    return mapping.get((direction, symbol), [direction])

def traversal(grid, start_point, start_direction):
    visited = set()
    energized = set()

    queue = [(start_point, start_direction)]

    while len(queue):
        head = queue.pop(0)

        if head in visited:
            continue

        position, direction = head
        row, col = position

        if row < 0 or row == len(grid) or col < 0 or col == len(grid):
            continue

        visited.add(head)
        energized.add(position)

        for (dr, dc) in get_new_directions(direction, grid[row][col]):
            queue.append(((row + dr, col + dc), (dr, dc)))

    return len(energized)

def main():
    lines = [line.strip('\n') for line in sys.stdin.readlines()]

    result = []

    # top, bottom
    for i in range(len(lines[0])):
        result.append(traversal(lines, (0, i), (+1, 0)))
        result.append(traversal(lines, (len(lines) - 1, i), (-1, 0)))

    # left, right
    for i in range(len(lines)):
        result.append(traversal(lines, (i, 0), (0, +1)))
        result.append(traversal(lines, (i, len(lines[0]) - 1), (0, -1)))
    print(traversal(lines, (0, 0), (0, +1)))
    print(max(result))

if __name__ == "__main__":
    main()