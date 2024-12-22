import sys

def mix(num1, num2):
    return num1 ^ num2

def prune(num):
    return num % 16777216

def calculate_next_secret(secret):
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret

def get_changes(s5, s4, s3, s2, s1):
    p5, p4, p3, p2, p1 = s5 % 10, s4 % 10, s3 % 10, s2 % 10, s1 % 10
    return (p4 - p5, p3 - p4, p2 - p3, p1 - p2)

def main():
    lines = [int(line) for line in sys.stdin.read().splitlines()]

    task1 = 0
    overall_changes = {}

    for line, number in enumerate(lines):
        print(f"\rProcessing {line + 1}/{len(lines)}", end="")
        seen = {}
        s5 = number
        s4 = calculate_next_secret(s5)
        s3 = calculate_next_secret(s4)
        s2 = calculate_next_secret(s3)

        for i in range(1997):
            s1 = calculate_next_secret(s2)
            changes = get_changes(s5, s4, s3, s2, s1)
            price = s1 % 10

            if changes not in seen:
                seen[changes] = price

            s5, s4, s3, s2 = s4, s3, s2, s1
        task1 += s1
        for change in seen:
            overall_changes[change] = overall_changes.get(change, 0) + seen[change]

    print()
    print(task1)
    print(max(overall_changes.values()))

if __name__ == "__main__":
    main()