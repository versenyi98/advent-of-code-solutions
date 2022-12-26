import sys
from collections import Counter

values = list(map(int, sys.stdin.read().split(",")))
counter = dict(Counter(values))

for i in range(256):
    new_counter = {}
    for value in range(1, 9):
        if value in counter:
            new_counter[value - 1] = counter[value]
    if 0 in counter:
        if 6 not in new_counter:
            new_counter[6] = 0
        if 8 not in new_counter:
            new_counter[8] = 0
        new_counter[6] += counter[0]
        new_counter[8] += counter[0]
    counter = new_counter
    if i == 79:
        print(sum(counter.values()))
print(sum(counter.values()))
