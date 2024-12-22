import sys
from functools import cache

keypad_pos = {
    '1': (1, 0),
    '2': (1, 1),
    '3': (1, 2),
    '4': (2, 0),
    '5': (2, 1),
    '6': (2, 2),
    '7': (3, 0),
    '8': (3, 1),
    '9': (3, 2),
    '0': (0, 1),
    'A': (0, 2),
    '^': (0, 1),
    'v': (-1, 1),
    '<': (-1, 0),
    '>': (-1, 2),
}

dir_mapping = {
    (+1, 0): '^',
    (-1, 0): 'v',
    (0, +1): '>',
    (0, -1): '<'
}

@cache
def get_instruction(char_from, char_to):
    pos1, pos2 = keypad_pos[char_from], keypad_pos[char_to]
    diff = pos2[0] - pos1[0], pos2[1] - pos1[1]

    row_moves = [(1 if diff[0] > 0 else -1, 0)] * abs(diff[0])
    col_moves = [(0, 1 if diff[1] > 0 else -1)] * abs(diff[1])

    col_first = "".join(map(lambda x: dir_mapping[x], col_moves + row_moves)) + "A"
    row_first = "".join(map(lambda x: dir_mapping[x], row_moves + col_moves)) + "A"

    if char_from in ['<', '1', '4', '7'] and char_to in ['A', '^', '0']:
        return [col_first]
    if char_from in ['A', '^', '0'] and char_to in ['<', '1', '4', '7']:
        return [row_first]

    if row_first == col_first:
        return [row_first]

    return [col_first, row_first]

@cache
def process(line, rounds_left):
    result = 0
    last_char = 'A'
    for char in line:
        instructions = get_instruction(last_char, char)
        if rounds_left == 0:
            result += min(map(len, instructions))
        else:
            result += min([process(instruction, rounds_left - 1) for instruction in instructions])
        last_char = char
    return result

def main():
    lines = sys.stdin.read().splitlines()
    print(sum([process(line, 2) * int(line[:-1]) for line in lines]))
    print(sum([process(line, 25) * int(line[:-1]) for line in lines]))

if __name__ == "__main__":
    main()