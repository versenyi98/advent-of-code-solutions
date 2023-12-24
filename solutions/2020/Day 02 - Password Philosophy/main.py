import sys
from collections import Counter

def solve(lines):
    task1, task2 = 0, 0
    for line in lines:
        i, j = int(line[0]) - 1, int(line[1]) - 1
        ch = line[2]
        pw = line[3]

        task1 += 1 if i + 1 <= Counter(pw)[ch] <= j + 1 else 0
        task2 += 1 if (pw[i] == ch) != (pw[j] == ch) else 0
    return task1, task2


def main():
    lines = [line.replace(': ', ' ').replace('-', ' ').split(' ') for line in sys.stdin.readlines()]
    print(solve(lines))

if __name__ == "__main__":
    main()