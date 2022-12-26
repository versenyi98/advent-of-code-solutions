import sys


def get_number_of_increases(measurements, window):
    count = 0

    for idx, curr in enumerate(measurements):
        if idx >= window:
            count += 1 if curr > measurements[idx - window] else 0
    return count


lines = sys.stdin.read().split()
converted_lines = list(map(int, lines))

for window in [1, 3]:
    print(get_number_of_increases(converted_lines, window))
