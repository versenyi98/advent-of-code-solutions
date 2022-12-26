import sys
import math
from operator import itemgetter


class Monkey:
    @staticmethod
    def create_monkey_from_input(lines):
        def convert_to_int(x):
            return int(x) if x.isnumeric() else x

        items = list(map(int, lines[1][18:].split(", ")))
        operands = list(map(convert_to_int, itemgetter(0, 2)(lines[2][19:].split())))
        operator = lines[2][19:].split()[1]
        divisor = int(lines[3].split()[-1])
        passed_target = int(lines[4].split()[-1])
        failed_target = int(lines[5].split()[-1])

        return Monkey(items, operator, operands, divisor, passed_target, failed_target)

    def __init__(self, items, operator, operands, divisor, passed_target, failed_target):
        self.items = items
        self.operator = operator
        self.operands = operands
        self.divisor = divisor
        self.passed_target = passed_target
        self.failed_target = failed_target
        self.inspect_counter = 0

    def inspect_objects(self, relief):
        for item in self.items:
            self.inspect_counter += 1
            new_worry_level = (self.apply_operation(item) // relief) % LCM

            target = self.passed_target if new_worry_level % self.divisor == 0 else self.failed_target
            yield new_worry_level, target
        self.items = []

    def apply_operation(self, old):
        def get_value(value):
            return old if value == 'old' else value

        if self.operator == '+':
            return get_value(self.operands[0]) + get_value(self.operands[1])
        elif self.operator == '*':
            return get_value(self.operands[0]) * get_value(self.operands[1])
        else:
            raise AttributeError(f"Unknown operation {self.operator}")


monkey_lines = [lines.split("\n") for lines in sys.stdin.read().split("\n\n")]

for rounds, relief in zip([20, 10000], [3, 1]):
    monkeys = [Monkey.create_monkey_from_input(lines) for lines in monkey_lines]
    LCM = math.prod([monkey.divisor for monkey in monkeys])
    for i in range(rounds):
        for monkey in monkeys:
            for new_worry_level, target_idx in monkey.inspect_objects(relief):

                monkeys[target_idx].items.append(new_worry_level)

    print(math.prod(sorted([monkey.inspect_counter for monkey in monkeys])[-2:]))
