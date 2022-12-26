import sys


def is_valid_stack(line):
    return line[0].isalnum()


def split_move(move):
    move = move.split()
    return int(move[1]), move[3], move[5]


def part1(move):
    amount_, from_, to_ = move

    from_stack = stacks[from_]
    being_moved = from_stack[len(from_stack) - amount_:]
    stacks[from_] = from_stack[:len(from_stack) - amount_]
    stacks[to_] += being_moved[::-1]


def part2(move):
    amount_, from_, to_ = move

    from_stack = stacks[from_]
    being_moved = from_stack[len(from_stack) - amount_:]
    stacks[from_] = from_stack[:len(from_stack) - amount_]
    stacks[to_] += being_moved


lines = sys.stdin.read()
stack_lines, move_lines = lines.split("\n\n")

stack_lines = stack_lines.split("\n")
stack_lines = [list(stack) for stack in stack_lines]
stack_lines = [list(row) for row in zip(*stack_lines[::-1])]

stack_lines = list(filter(is_valid_stack, stack_lines))
moves = move_lines.split("\n")
moves = list(map(split_move, moves))

for func in [part1, part2]:
    stacks = {line[0]: ''.join(line[1:]).strip() for line in stack_lines}
    for move in moves:
        func(move)

    for key, value in stacks.items():
        print(value[-1], end="")
    print()
