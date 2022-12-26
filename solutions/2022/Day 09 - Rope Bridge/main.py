import sys

moves = [line.split() for line in sys.stdin.read().split('\n')]

directions = {
    'U': (+1, 0),
    'D': (-1, 0),
    'L': (0, -1),
    'R': (0, +1)
}

for rope_length in [2, 10]:
    visited = {}
    knots = [(0, 0) for x in range(rope_length)]

    for move in moves:
        direction, amount = move
        dir_y, dir_x = directions[direction]
        for idx in range(int(amount)):
            head_y, head_x = knots[0]
            head_pos = (head_y + dir_y, head_x + dir_x)
            knots[0] = head_pos

            for knot_idx, knot in enumerate(knots[1:]):
                diff_y, diff_x = knots[knot_idx][0] - knot[0], knots[knot_idx][1] - knot[1]

                if abs(diff_y) == 2 or abs(diff_x) == 2:
                    snap_y = diff_y if abs(diff_y) != 2 else 1 if diff_y == 2 else -1
                    snap_x = diff_x if abs(diff_x) != 2 else 1 if diff_x == 2 else -1
                    knot = knot[0] + snap_y, knot[1] + snap_x

                knots[knot_idx + 1] = knot
            visited[knots[-1]] = True
    print(len(visited))