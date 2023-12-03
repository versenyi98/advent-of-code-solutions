import sys
import math

def collect_data(lines, strategy):
    r = 0
    while r < len(lines):
        row = lines[r]
        c = 0
        while c < len(row):
            col = row[c]

            if not col.isnumeric():
                c += 1
                continue

            number = []
            positions = []
            while c < len(row) and row[c].isnumeric():
                number.append(row[c])
                for nr in range(r - 1, r + 2):
                    for nc in range(c - 1, c + 2):
                        if nr < 0 or nc < 0 or nr == len(lines) or nc == len(row):
                            continue
                        positions.append((nr, nc))
                c += 1
            number = int("".join(number))
            strategy(positions, number)
            c += 1
        r += 1

def task1(lines):
    def strategy(positions, number):
        nonlocal result

        for nr, nc in positions:
            if lines[nr][nc] != '.' and not lines[nr][nc].isnumeric():
                result += number
                break

    result = 0

    collect_data(lines, strategy)

    return result

def task2(lines):
    def strategy(positions, number):
        nonlocal gear_ratios

        for nr, nc in positions:
            if lines[nr][nc] == '*' and not lines[nr][nc].isnumeric():
                if (nr, nc) in gear_ratios:
                    gear_ratios[(nr, nc)].append(number)
                else:
                    gear_ratios[(nr, nc)] = [number]
                break

    gear_ratios = {}

    collect_data(lines, strategy)

    result = sum([math.prod(gear) if len(gear) == 2 else 0 for gear in gear_ratios.values()])

    return result



def main():
    lines = [line.strip('\n') for line in sys.stdin.readlines()]

    print(task1(lines))
    print(task2(lines))

if __name__ == "__main__":
    main()