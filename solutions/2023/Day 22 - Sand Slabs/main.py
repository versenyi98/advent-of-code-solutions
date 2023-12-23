import sys
from collections import defaultdict
import heapq

class Brick(object):
    def __init__(self, id, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2
        self.id = id

    def __repr__(self) -> str:
        return f"Brick #{self.id}({self.pos1}, {self.pos2})"

    def __lt__(self, other):
        return self.pos1[2] < other.pos1[2]


def is_overlapping(brick_a, brick_b):
    def are_ranges_intersecting(range1_start, range1_end, range2_start, range2_end):
        return not (range1_end < range2_start or range1_start > range2_end)
    return all([are_ranges_intersecting(brick_a.pos1[i], brick_a.pos2[i], brick_b.pos1[i], brick_b.pos2[i]) for i in range(3)])

def main():
    lines = [line.strip('\n').split('~') for line in sys.stdin.readlines()]
    bricks = []

    for id, line in enumerate(lines):
        bricks.append(Brick(chr(ord('A') + id), *[tuple(map(int, part.split(','))) for part in line]))

    solid = []

    heap = bricks
    heapq.heapify(heap)

    supports = defaultdict(list)
    supported = defaultdict(list)

    # TODO: simulation could be optimized (e.g. fall directly above the highest brick position, then simulate it this way)
    while len(heap):
        head = heapq.heappop(heap)
        new_brick = Brick(head.id, (head.pos1[0], head.pos1[1], head.pos1[2] - 1), (head.pos2[0], head.pos2[1], head.pos2[2] - 1))

        if new_brick.pos1[2] == 0:
            solid.append(head)
            continue

        overlaps = False
        for s in solid:
            if is_overlapping(new_brick, s):
                overlaps = True
                supports[s.id].append(head.id)
                supported[new_brick.id].append(s.id)

        if overlaps:
            solid.append(head)
            print(f"\rPart 1 {len(solid)}/{len(solid) + len(bricks)}", end="")
            continue
        heapq.heappush(heap, new_brick)
    print()

    task1 = 0
    for brick in solid:
        if all([len(supported[s]) != 1 for s in supports[brick.id]]):
            task1 += 1
    print(task1)

    task2 = 0
    for i, brick in enumerate(solid):
        print(f"\rPart 2 {i + 1}/{len(solid)}", end="")

        index = 0
        falling = [brick.id]

        while index < len(falling):
            current = falling[index]
            for s in supports.get(current, []):
                if s not in falling and all([ss in falling for ss in supported[s]]):
                    falling.append(s)
            index += 1
        task2 += len(falling) - 1
    print()
    print(task2)

if __name__ == "__main__":
    main()