# only works for my secret input :(

import sys

lines = sys.stdin.read().split("\n")

start_point = None
end_point = None

walls = set()
width = len(lines[0]) - 2
height = len(lines) - 2

direction = {
    ">": (0, +1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (+1, 0)
}

winds = set()

for row_idx, row in enumerate(lines):
    for col_idx, col in enumerate(row):
        if col == ".":
            if start_point is None:
                start_point = (row_idx - 1, col_idx - 1)
            end_point = (row_idx - 1, col_idx - 1)
        elif col != "#":
            winds.add(((row_idx - 1, col_idx - 1), direction[col]))
wind_cache = [winds]


def traverse(start_point, end_point, start_round):
    queue = [(start_point, start_round)]
    visited = set(queue)

    while queue:
        pos, round_idx = queue.pop(0)
        pos_row, pos_col = pos
        if pos == end_point:
            return round_idx
        round_idx += 1
        mod_round_idx = round_idx % (height * width)

        if mod_round_idx >= len(wind_cache):
            wind_cache.append(set())
            for ((wind_row, wind_col), (wind_dir_row, wind_dir_col)) in winds:
                new_wind_row = (wind_row + wind_dir_row * round_idx) % height
                new_wind_col = (wind_col + wind_dir_col * round_idx) % width
                wind_cache[mod_round_idx].add((new_wind_row, new_wind_col))

        for dir_row, dir_col in direction.values():
            new_pos = (dir_row + pos_row, dir_col + pos_col)

            if new_pos != start_point and new_pos != end_point and (new_pos[0] < 0 or new_pos[0] >= height or new_pos[1] < 0 or new_pos[1] >= width):
                continue
            if (new_pos, mod_round_idx) in visited:
                continue
            if new_pos in wind_cache[mod_round_idx]:
                continue
            visited.add((new_pos, mod_round_idx))
            queue.append((new_pos, round_idx))
        if pos in wind_cache[mod_round_idx] or (pos, mod_round_idx) in visited:
            continue

        visited.add((pos, mod_round_idx))
        queue.append((pos, round_idx))


res1 = traverse(start_point, end_point, 0)
res2 = traverse(end_point, start_point, res1)
res3 = traverse(start_point, end_point, res2)
print(res1, res2, res3)