import sys
from functools import cache

def remove_trailing_zeroes(val):
    while len(val) and val[-1] == 0:
        val = val[:-1]

    return val

@cache
def dp(line, position, current_groups, target_groups):
    current_groups_trunc = remove_trailing_zeroes(current_groups)

    if position == len(line):
        return 1 if remove_trailing_zeroes(current_groups) == target_groups else 0

    if current_groups_trunc == target_groups and line[position:].find('#') == -1:
        return 1

    if len(current_groups_trunc) > len(target_groups):
        return 0

    if len(current_groups) and current_groups_trunc[-1] > target_groups[len(current_groups_trunc) - 1]:
        return 0

    if len(current_groups) and current_groups_trunc[:-1] != target_groups[:len(current_groups_trunc) - 1]:
        return 0

    if line[position] == '#':
        if current_groups:
            return dp(line, position + 1, current_groups[:-1] + (current_groups[-1] + 1,), target_groups)
        else:
            return dp(line, position + 1, (1,), target_groups)

    elif line[position] == '.':
        if len(current_groups) == 0 or current_groups[-1] == 0:
            return dp(line, position + 1, current_groups, target_groups)
        else:
            return dp(line, position + 1, current_groups + (0,), target_groups)
    else:
        if len(current_groups) == 0:
            swap = dp(line, position + 1, current_groups + (1,), target_groups)
        else:
            swap = dp(line, position + 1, current_groups[:-1] + (current_groups[-1] + 1,), target_groups)

        if len(current_groups) == 0 or current_groups[-1] == 0:
            no_swap = dp(line, position + 1, current_groups, target_groups)
        else:
            no_swap = dp(line, position + 1, current_groups + (0,), target_groups)

        return no_swap + swap

def main():
    lines = [line.strip('\n').split(' ') for line in sys.stdin.readlines()]
    task1 = []
    task2 = []

    for [line, numbers] in lines:
        numbers = tuple(map(int, numbers.split(',')))

        task1.append(dp(line, 0, (), numbers))
        task2.append(dp("?".join([line] * 5), 0, (), numbers * 5))

    print(sum(task1), sum(task2))

if __name__ == "__main__":
    main()