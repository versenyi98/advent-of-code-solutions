import sys
import numpy as np

def task1(grid, start):
    queue = [start]

    for _ in range(64):
        next_queue = set()

        while len(queue) > 0:
            r, c = queue[0]
            queue.pop(0)

            for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if grid[nr][nc] == '#':
                    continue
                next_queue.add((nr, nc))
        queue = list(next_queue)
    return len(next_queue)

def task2(grid, start):
    goal = 26501365

    queue = [start]
    points = []
    i = 1
    while len(points) != 3:
        next_queue = set()

        while len(queue) > 0:
            r, c = queue[0]
            queue.pop(0)

            for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if grid[nr % len(grid)][nc % len(grid[0])] == '#':
                    continue
                next_queue.add((nr, nc))
        queue = list(next_queue)

        if i % len(grid) == goal % len(grid):
            points.append(len(next_queue))
            print(len(points), len(next_queue))
        i += 1

    x = np.array([1, 2, 3])
    y = np.array(points)
    coefficients = list(map(int, np.polyfit(x, y, 2)))

    goal_x = 1 + goal // len(grid)
    result = coefficients[0] * goal_x * goal_x + coefficients[1] * goal_x + coefficients[2]

    return result

def main():
    grid = [line.strip() for line in sys.stdin.readlines()]

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == 'S':
                start = (r, c)

    print(task1(grid, start))
    print(task2(grid, start))


if __name__ == "__main__":
    main()