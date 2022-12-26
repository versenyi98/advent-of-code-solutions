import sys


def parse_line(line):
    first, second = line.split(",")
    parsed_line = [*first.split("-"), *second.split("-")]
    return list(map(int, parsed_line))


def fully_overlapping(line):
    fb, fe, sb, se = line
    first_set = {*range(fb, fe + 1)}
    second_set = {*range(sb, se + 1)}

    return first_set.issubset(second_set) or second_set.issubset(first_set)


def overlapping(line):
    fb, fe, sb, se = line
    first_set = {*range(fb, fe + 1)}
    second_set = {*range(sb, se + 1)}

    return len(set.intersection(first_set, second_set)) > 0


lines = sys.stdin.read().split('\n')
parsed_lines = list(map(parse_line, lines))

for func in (fully_overlapping, overlapping):
    res = list(map(func, parsed_lines))
    print(sum(res))
