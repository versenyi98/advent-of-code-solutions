import sys

def shoelace_formula(vertices):
    n = len(vertices)
    if n < 3:
        return 0

    sum1 = 0
    sum2 = 0

    for i in range(n):
        sum1 += vertices[i][0] * vertices[(i + 1) % n][1]
        sum2 += vertices[i][1] * vertices[(i + 1) % n][0]

    return abs(sum1 - sum2) // 2

def solve(lines, mapping, get_amount, get_direction):
    pos = (0, 0)

    points = []
    length = 1

    for entry in lines:
        amount = get_amount(entry)
        dir = get_direction(entry)

        length += amount

        dir = mapping[dir]
        next_pos = (pos[0] + dir[0] * amount, pos[1] + dir[1] * amount)

        pos = next_pos
        points.append(pos)
    return shoelace_formula(points) + length // 2 + 1

def main():
    lines = [line.strip('\n').split() for line in sys.stdin.readlines()]

    mapping_task1 = { 'D': (-1, 0), 'U': (+1, 0), 'L': (0, -1), 'R': (0, +1) }
    mapping_task2 = { 3: (-1, 0), 1: (+1, 0), 2: (0, -1), 0: (0, +1) }

    def get_amount_task1(entry):
        return int(entry[1])

    def get_direction_task1(entry):
        return entry[0]

    def get_amount_task2(entry):
        return int("0x" + entry[2][2:-2], 16)

    def get_direction_task2(entry):
        return int("0x" + entry[2][-2], 16)


    print(solve(lines, mapping_task1, get_amount_task1, get_direction_task1))
    print(solve(lines, mapping_task2, get_amount_task2, get_direction_task2))

if __name__ == "__main__":
    main()