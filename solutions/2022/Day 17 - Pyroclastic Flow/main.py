import sys

wind = list(sys.stdin.read())

shapes = [
    [(2, 0), (3, 0), (4, 0), (5, 0)],  # vertical shape
    [(3, 2), (2, 1), (3, 1), (4, 1), (3, 0)],  # X shape
    [(4, 2), (4, 1), (2, 0), (3, 0), (4, 0)],  # mirrored L shape
    [(2, 3), (2, 2), (2, 1), (2, 0)],  # horizontal shape
    [(2, 1), (3, 1), (2, 0), (3, 0)] # box shape
]

current_shape_idx = -1
current_wind_idx = -1
current_height = 0

walls = {-1, 7}
floor = set([(x, 0) for x in range(7)])
settled = set()

number_of_rocks = 1000000000000
cache_on_round = 2021

rock_idx = 0
while rock_idx < number_of_rocks:
    current_shape_idx = (current_shape_idx + 1) % len(shapes)
    current_shape = [(x, y + current_height + 5) for x, y in shapes[current_shape_idx]]

    wind_pushes = 0

    while True:
        # fall
        fallen_shape = [(x, y - 1) for x, y in current_shape]
        can_fall = True
        for piece in fallen_shape:
            if piece in floor or piece in settled:
                can_fall = False
                break
        if not can_fall:
            for piece in current_shape:
                current_height = max(current_height, piece[1])
                settled.add(piece)
            break
        current_shape = fallen_shape

        # push
        current_wind_idx = (current_wind_idx + 1) % len(wind)
        current_wind = wind[current_wind_idx]
        current_wind_effect = 1 if current_wind == '>' else -1
        wind_pushes += 1
        pushed_shape = [(x + current_wind_effect, y) for x, y in current_shape]
        can_be_pushed = True
        for piece in pushed_shape:
            if piece in floor or piece in settled or piece[0] in walls:
                can_be_pushed = False
                break
        if can_be_pushed:
            current_shape = pushed_shape
    if rock_idx == cache_on_round:
        print(current_height)
        cached_rock = current_shape_idx
        cached_wind = current_wind_idx
        cached_height = current_height
        cached_rock_idx = rock_idx
    if rock_idx > cache_on_round:
        if current_shape_idx == cached_rock and current_wind_idx == cached_wind:
            height_diff = current_height - cached_height
            idx_diff = rock_idx - cached_rock_idx
            remaining_loops = (number_of_rocks - rock_idx) // idx_diff
            plus_height = remaining_loops * height_diff
            rock_idx += remaining_loops * idx_diff

    rock_idx += 1

print(current_height + plus_height)