import sys
import math

def task1(games):
    result = 0

    cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    for id, game in enumerate(games, 1):
        possible = True
        for set in game:
            for amount, color in set:
                if cubes[color] < int(amount):
                    possible = False
                    break
        if possible:
            result += id
    return result

def task2(games):
    result = 0

    for game in games:
        cubes = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for set in game:
            for amount, color in set:
                cubes[color] = max(cubes[color], int(amount))

        result += math.prod(cubes.values())

    return result

def main():
    lines = [line.replace(', ', ',').split(':')[-1].strip(' \n') for line in sys.stdin.readlines()]
    games = [[[cube.split() for cube in set.split(',')] for set in line.split(';')] for line in lines]

    print(task1(games))
    print(task2(games))

if __name__ == "__main__":
    main()