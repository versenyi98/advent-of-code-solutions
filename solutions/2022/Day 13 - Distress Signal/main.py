import sys
import math
from functools import cmp_to_key


def group_elements(lst, group_size):
    return list(zip(*(iter(lst), ) * group_size))


def packet_less_than(left, right):
    if type(left) == type(right) == int:
        if left != right:
            return 1 if left < right else -1
    else:
        left = [left] if type(left) is int else left
        right = [right] if type(right) is int else right

        for lval, rval in zip(left, right):
            res = packet_less_than(lval, rval)
            if res != 0:
                return res
        if len(left) != len(right):
            return 1 if len(left) < len(right) else -1
    return 0


packets = [eval(line) for line in sys.stdin.read().split()]
grouped_packets = group_elements(packets, 2)

extra_packets = [[[2]], [[6]]]
print(sum([idx + 1 for idx, (left, right) in enumerate(grouped_packets) if packet_less_than(left, right) == 1]))
print(math.prod([idx + 1 for idx, packet in enumerate(sorted(packets + extra_packets, key=cmp_to_key(packet_less_than), reverse=True)) if packet in extra_packets]))
