import sys
import math


def calculate_area(cubes):
    area = 0

    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    for x, y, z in cubes:
        side_not_covered = 6
        for dx, dy, dz in directions:
            if (x + dx, y + dy, z + dz) in cubes:
                side_not_covered -= 1
        area += side_not_covered
    return area


def calculate_outer_area(cubes, air):
    area = 0

    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    for x, y, z in cubes:
        side_not_covered = 0
        for dx, dy, dz in directions:
            if (x + dx, y + dy, z + dz) in air:
                side_not_covered += 1
        area += side_not_covered
    return area


test_cases = sys.stdin.read().split("\n\n")
for idx, test_case in enumerate(test_cases):
    test_cases[idx] = set(tuple(map(int, tc.split(','))) for tc in test_case.split("\n"))


for droplets in test_cases:
    maximum_idx = -math.inf
    minimum_idx = math.inf
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    for x, y, z in droplets:
        maximum_idx = max(x, y, z, maximum_idx)
        minimum_idx = min(x, y, z, minimum_idx)

    maximum_idx += 1
    minimum_idx -= 1
    valid = range(minimum_idx, maximum_idx + 1)

    start_point = (minimum_idx, minimum_idx, minimum_idx)
    queue = [start_point]

    visited = set(start_point)
    outer_droplets = set()

    while queue:
        head = queue.pop(0)
        curr_x, curr_y, curr_z = head

        if head in droplets:
            outer_droplets.add(head)
            continue

        for dx, dy, dz in directions:
            if all(pos in valid for pos in [curr_x + dx, curr_y + dy, curr_z + dz]):
                next_pos = (curr_x + dx, curr_y + dy, curr_z + dz)
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append(next_pos)

    print(calculate_area(droplets))
    print(calculate_outer_area(outer_droplets, visited - outer_droplets))