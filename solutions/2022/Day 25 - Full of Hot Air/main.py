import sys

digit_map = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

reverse_digit_map = {value: key for key, value in digit_map.items()}


def part1(snafu):
    decimal = 0
    for idx, digit in enumerate(snafu[::-1]):
        decimal += digit_map[digit] * pow(5, idx)
    return decimal


def decimal_to_snafu(decimal):
    biggest_possible = 0

    power = 0
    while pow(5, power) < decimal:
        biggest_possible += 2 * pow(5, power)
        power += 1

    if biggest_possible > decimal:
        power -= 1
        biggest_possible -= 2 * pow(5, power)
    result = ""

    while power > -1:
        current = pow(5, power)

        for key in [2, 1, 0, -1, -2]:
            minus_biggest = key * current - biggest_possible
            plus_biggest = key * current + biggest_possible
            lower = min(minus_biggest, plus_biggest)
            upper = max(minus_biggest, plus_biggest)

            if lower <= decimal <= upper:
                result += reverse_digit_map[key]
                decimal = decimal - key * current
                break
        power -= 1
        biggest_possible -= 2 * pow(5, power)
    return result


lines = sys.stdin.read().split("\n")

sum_of_numbers = sum(map(part1, lines))
print(decimal_to_snafu(sum_of_numbers))