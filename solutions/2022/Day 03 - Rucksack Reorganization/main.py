import sys


def split_into_half(line):
    half_length = len(line) // 2
    return line[:half_length], line[half_length:]


def group_list_elements(the_list, group_size):
    return list(zip(*(iter(the_list),) * group_size))


def keep_common_item(items):
    sets = [set(item) for item in items]
    return ''.join(sorted(set.intersection(*sets)))


def get_priority(item):
    if item == item.lower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


lines = sys.stdin.read().split('\n')
compartments_content = list(map(split_into_half, lines))
grouped_list = group_list_elements(lines, 3)

for lst in [compartments_content, grouped_list]:
    common_items = list(map(keep_common_item, lst))
    priorities = list(map(get_priority, common_items))
    print(sum(priorities))
