import sys


def get_range(start, end):
    step = 1 if start <= end else -1
    return range(start, end + step, step)


wall_pos = set()

# Lord forgive me for I've sinned
wall_corners = [list(map(lambda x: list(map(int, x.split(","))), line.split(" -> "))) for line in sys.stdin.read().split("\n")]
wall_pos.update([(xx, yy) for wall_corner in wall_corners for idx, (x, y) in enumerate(wall_corner) if idx + 1 < len(wall_corner) for xx in get_range(x, wall_corner[idx + 1][0]) for yy in get_range(y, wall_corner[idx + 1][1])])

fall_directions = [(0, +1), (-1, +1), (+1, +1)]


def get_result(part):
    sand_pos = set()
    falling_sand = [(500, 0)]

    lowest_wall = max([y for _, y in wall_pos])

    if part == 2:
        lowest_wall += 2

    while len(falling_sand) and falling_sand[-1][1] != lowest_wall:
        falling = False
        for direction in fall_directions:
            new_pos = tuple(sum(x) for x in zip(direction, falling_sand[-1]))
            if new_pos not in sand_pos and new_pos not in wall_pos and (part == 1 or new_pos[1] != lowest_wall):
                falling = True
                falling_sand += [new_pos]
                break
        if not falling:
            settled = falling_sand.pop(-1)
            sand_pos.add(settled)
    return len(sand_pos)


for part in [1, 2]:
    print(get_result(part))