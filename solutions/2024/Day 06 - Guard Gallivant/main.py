import sys

rows, cols = 0, 0
directions = [(-1, 0), (0, +1), (+1, 0), (0, -1)]

def task1(obstacles, guard):
    positions = set()
    curr_dir = 0
    
    positions.add(guard)
    
    while True:
        row, col = guard
        dir_row, dir_col = directions[curr_dir]
        new_row, new_col = row + dir_row, col + dir_col
        new_guard = (new_row, new_col)
        if new_guard in obstacles:
            curr_dir = (curr_dir + 1) % 4
        elif (new_row < 0 or new_row == rows or new_col < 0 or new_col == cols):
            return positions
        else:
            positions.add(new_guard)
            guard = new_guard

def task2(obstacles, guard):
    obstacles_hit = set()
    curr_dir = 0
        
    while True:
        row, col = guard
        dir_row, dir_col = directions[curr_dir]
        new_row, new_col = row + dir_row, col + dir_col
        new_guard = (new_row, new_col)
        if new_guard in obstacles:
            if (new_guard, curr_dir) in obstacles_hit:
                return True
            obstacles_hit.add((new_guard, curr_dir))
            curr_dir = (curr_dir + 1) % 4
        elif (new_row < 0 or new_row == rows or new_col < 0 or new_col == cols):
            return False
        else:
            guard = new_guard

def main():
    lines = sys.stdin.read().split('\n')

    global rows, cols
    rows = len(lines)
    cols = len(lines[0])

    obstacles = set((r, c)
                    for r, row in enumerate(lines)
                    for c, col in enumerate(row)
                    if col == '#')
    guard = [(r, c)
             for r, row in enumerate(lines)
             for c, col in enumerate(row)
             if col == '^'
            ][0]

    positions = task1(obstacles, guard)
    print(f"Task 1: {len(positions)}")
    print(f"Task 2: {sum(task2(obstacles | set([pos]), guard) for pos in positions)}")

if __name__ == "__main__":
    main()