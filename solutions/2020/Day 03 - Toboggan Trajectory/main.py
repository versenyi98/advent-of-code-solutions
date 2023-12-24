import sys
import math

def solve(lines, slopes):
    results = []
    for slope in slopes:
        r, c = 0, 0
        dr, dc = slope
        results.append(0)

        while r < len(lines):
            if lines[r][c] == '#':
                results[-1] += 1
            r += dr
            c = (c + dc) % len(lines[0])
    return math.prod(results)


def main():
    lines = [line.strip("\n") for line in sys.stdin.readlines()]

    print(solve(lines, [(1, 3)]))
    print(solve(lines, [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]))

if __name__ == "__main__":
    main()