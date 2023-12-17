import sys
import heapq

directions = [
    (0, +1),
    (+1, 0),
    (0, -1),
    (-1, 0)
]

def solve(grid, step_constraint, end_constraint):
    # heat loss
    # position
    # direction
    # same direction in a row
    initial_state = (0, ((0, 0), (0, +1), 0))

    visited = set()
    heap = [initial_state]

    while len(heap):
        head = heapq.heappop(heap)
        loss, state = head

        if state in visited:
            continue
        visited.add(state)

        position, direction, direction_count = state
        r, c = position

        if r == len(grid) - 1 and c == len(grid[0]) - 1 and end_constraint(direction_count):
            return loss

        direction_i = directions.index(direction)
        for new_direction_i in range(direction_i - 1, direction_i + 2):
            new_direction = directions[new_direction_i % len(directions)]
            dr, dc = new_direction

            nr = r + dr
            nc = c + dc

            if nr < 0 or nr == len(grid) or nc < 0 or nc == len(grid[0]):
                continue

            if not step_constraint(new_direction_i, direction_i, direction_count):
                continue

            heapq.heappush(heap, (loss + int(grid[nr][nc]), ((nr, nc), (dr, dc), 1 if direction_i != new_direction_i else direction_count + 1)))

def main():
    lines = [line.strip('\n') for line in sys.stdin.readlines()]

    def task1_end_constraint(_):
        return True

    def task1_step_constraint(dir_i, dir_j, count):
        return (not dir_i == dir_j or count < 3)

    def task2_end_constraint(count):
        return count >= 4

    def task2_step_constraint(dir_i, dir_j, count):
        return (not dir_i != dir_j or count >= 4) and (not dir_i == dir_j or count < 10)

    print(solve(lines, task1_step_constraint, task1_end_constraint))
    print(solve(lines, task2_step_constraint, task2_end_constraint))


if __name__ == "__main__":
    main()