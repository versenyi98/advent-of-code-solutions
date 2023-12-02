import sys

def task1(lines):
    result = 0
    for line in lines:
        numbers = [int(ch) for ch in line if ch.isnumeric()]
        result += 10 * numbers[0] + numbers[-1]
    return result

def task2(lines):
    numbers = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 }

    def decode_numbers(line):
        for key, value in numbers.items():
            while (index := line.find(key)) != -1:
                line = line[:index + 1] + str(value) + line[index + 1:]
        return line

    decoded_lines = [decode_numbers(line) for line in lines]
    return task1(decoded_lines)

def main():
    lines = [line.strip('\n') for line in sys.stdin.readlines()]

    print(task1(lines))
    print(task2(lines))

if __name__ == "__main__":
    main()