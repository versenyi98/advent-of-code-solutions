import sys
import math
from itertools import combinations

def solve(numbers, n):
    for group in combinations(numbers, n):
        if sum(group) == 2020:
            return math.prod(group)

def main():
    numbers = list(map(int, sys.stdin.readlines()))
    print(solve(numbers, 2))
    print(solve(numbers, 3))

if __name__ == "__main__":
    main()