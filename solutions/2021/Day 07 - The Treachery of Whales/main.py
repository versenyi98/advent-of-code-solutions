import math
import sys

values = list(map(int, sys.stdin.read().split(",")))

sorted_values = sorted(values)
print(sum(abs(sorted_values[len(sorted_values) // 2] - value) for value in values))

avg_floor = sum(values) // len(values)
avg_ceil = math.ceil(sum(values) / len(values))

minimum = math.inf
for current in [avg_ceil, avg_floor]:
    minimum = min(minimum, sum((1 + abs(current - value)) * abs(current - value) // 2 for value in values))
print(minimum)
