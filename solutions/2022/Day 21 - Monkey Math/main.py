import copy
import sys

lines = sys.stdin.read().split("\n")


def parse(lines):
    numbers = {}
    operations = []

    for line in lines:
        split = line.split()
        name = split[0][:-1]

        if len(split) == 2:
            number = int(split[1])
            numbers[name] = number
        else:
            if name == "root":
                root1 = split[1]
                root2 = split[3]
            operations.append((name, split[1], split[2], split[3]))
    return numbers, operations, root1, root2


def part1(numbers, operations):
    copy_numbers = copy.deepcopy(numbers)
    copy_operation = copy.deepcopy(operations)

    while copy_operation:
        new_operations = []
        while copy_operation:
            head = copy_operation.pop()
            name, operand1, operator, operand2 = head
            if operand1 in copy_numbers and operand2 in copy_numbers:
                copy_numbers[name] = eval(f"{copy_numbers[operand1]} {operator} {copy_numbers[operand2]}")
            else:
                new_operations.append(head)
        copy_operation = new_operations
    return int(copy_numbers["root"])


def part2(numbers, operations):
    for order in range(2):
        humn_values_range = (-pow(10, 15), pow(10, 15))
        previous_humn_value = None
        while True:
            humn_value = (humn_values_range[0] + humn_values_range[1]) // 2
            if previous_humn_value:
                if humn_value == previous_humn_value:
                    break
            previous_humn_value = humn_value
            copy_numbers = copy.deepcopy(numbers)
            copy_operation = copy.deepcopy(operations)

            copy_numbers["humn"] = humn_value

            while copy_operation:
                new_operations = []
                while copy_operation:
                    head = copy_operation.pop()
                    name, operand1, operator, operand2 = head
                    if name == "root":
                        continue

                    if operand1 in copy_numbers and operand2 in copy_numbers:
                        copy_numbers[name] = eval(f"{copy_numbers[operand1]} {operator} {copy_numbers[operand2]}")
                    else:
                        new_operations.append(head)
                copy_operation = new_operations

            diff = copy_numbers[root2] - copy_numbers[root1]

            if diff < 0 if order else diff > 0:
                humn_values_range = (humn_value + 1, humn_values_range[1])
            elif diff > 0 if order else diff < 0:
                humn_values_range = (humn_values_range[0], humn_value - 1)
            else:
                return humn_value


numbers, operations, root1, root2 = parse(lines)
print(part1(numbers, operations))
print(part2(numbers, operations))
