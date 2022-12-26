import sys
from collections import Counter

lines = sys.stdin.read().split()
lines = list(map(list, lines))

transposed_lines = [list(row) for row in zip(*lines[::-1])]
counters = [Counter(row) for row in transposed_lines]

gamma = ''.join([counter.most_common(1)[0][0] for counter in counters])
epsilon = ''.join([counter.most_common()[1][0] for counter in counters])

power_consumption = int(gamma, 2) * int(epsilon, 2)
print(power_consumption)

o2_generator_lists = lines
co2_scrubber_lists = lines


def get_part2_values(lines, default_value, func):
    for idx in range(len(transposed_lines)):
        counter = Counter([line[idx] for line in lines])
        new_list = []

        ones = counter.get('1', 0)
        zeros = counter.get('0', 0)

        to_be_used = default_value if ones == zeros else '1' if func(ones, zeros) == ones else '0'

        for line in lines:
            if line[idx] == to_be_used:
                new_list.append(line)
        lines = new_list
        if len(lines) == 1:
            return lines[0]
    return lines[0]


o2_val = int(''.join(get_part2_values(o2_generator_lists, '1', max)), 2)
co2_val = int(''.join(get_part2_values(co2_scrubber_lists, '0', min)), 2)

print(o2_val * co2_val)
