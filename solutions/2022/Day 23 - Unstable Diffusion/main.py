import math
import sys
from collections import Counter


grid = sys.stdin.read().split("\n")

elves = set()

surrounding = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]

moves = [
    [(-1, -1), (-1, 0), (-1, 1)],   # NORTH
    [(+1, -1), (+1, 0), (+1, 1)],   # SOUTH
    [(-1, -1), (0, -1), (1, -1)],   # WEST
    [(-1, +1), (0, +1), (1, +1)],   # EAST
]

for row_idx, row in enumerate(grid):
    for col_idx, col in enumerate(row):
        if col == "#":
            elves.add((row_idx, col_idx))

round_number = 0
while True:
    round_number += 1
    new_elves = set()

    didnt_move = 0

    proposed = {}
    proposed_counter = Counter()

    for elf in elves:
        should_move = False
        ex, ey = elf
        for sx, sy in surrounding:
            if ((ex + sx), (ey + sy)) in elves:
                should_move = True
                break

        if should_move:
            could_move = False
            for move in moves:
                good = True
                for mx, my in move:
                    if ((ex + mx), (ey + my)) in elves:
                        good = False
                        break
                if not good:
                    continue
                could_move = True
                nx, ny = ex + move[1][0], ey + move[1][1]
                proposed[elf] = (nx, ny)
                proposed_counter.update([(nx, ny)])
                break
            if not could_move:
                proposed[elf] = elf
                proposed_counter.update([elf])
                didnt_move += 1
        else:
            proposed[elf] = elf
            proposed_counter.update([elf])
            didnt_move += 1
    for elf in elves:
        if proposed_counter[proposed[elf]] == 1:
            new_elves.add(proposed[elf])
        else:
            new_elves.add(elf)

    elves = new_elves
    moves = moves[1:] + [moves[0]]
    min_row, max_row, min_col, max_col = math.inf, -math.inf, math.inf, -math.inf

    for elf in elves:
        row, col = elf
        min_row = min(min_row, row)
        max_row = max(max_row, row)
        min_col = min(min_col, col)
        max_col = max(max_col, col)

    if round_number == 10:
        print((max_row - min_row + 1) * (max_col - min_col + 1) - len(elves))
    if didnt_move == len(elves):
        print(round_number)
        break