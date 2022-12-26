import sys


def part1(match):
    opponent_pick = ord(match[0]) - ord('A')
    my_pick = ord(match[1]) - ord('X')

    return my_pick + 1 + ((my_pick - opponent_pick + 4) % 3) * 3


def part2(match):
    opponent_pick = ord(match[0]) - ord('A')
    outcome = ord(match[1]) - ord('Y')
    my_pick = (opponent_pick + outcome + 3) % 3
    return my_pick + 1 + (outcome + 1) * 3


lines = sys.stdin.read().split("\n")
matches = [line.split() for line in lines]

for func in [part1, part2]:
    points = sum(list(map(func, matches)))
    print(points)
