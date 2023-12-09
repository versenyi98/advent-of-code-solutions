import sys

def solve(sequences):
    next_values = []
    prev_values = []

    for current_sequence in sequences:
        diffs = [current_sequence]

        while any(last := diffs[-1]):
            diffs.append([last[i + 1] - last[i] for i in range(len(last) - 1)])

        prev = 0
        next = 0

        for current_diffs in reversed(diffs):
            prev = current_diffs[0] - prev
            next = current_diffs[-1] + next
        next_values.append(next)
        prev_values.append(prev)

    return sum(next_values), sum(prev_values)

def main():
    numbers = [list(map(int, line.strip('\n').split())) for line in sys.stdin.readlines()]
    print(solve(numbers))

if __name__ == "__main__":
    main()