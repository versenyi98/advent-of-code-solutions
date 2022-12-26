import sys

lines = sys.stdin.read()

calories_by_elf = [list(map(int, elf.split("\n"))) for elf in lines.split("\n\n")]
calorie_sum = list(map(sum, calories_by_elf))
calorie_sum.sort()

print(calorie_sum[-1])
print(sum(calorie_sum[-3:]))