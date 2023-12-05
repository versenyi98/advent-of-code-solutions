import sys

def task1(cards):
    result = 0
    for winning, own in cards:
        matching = len(list(set(winning) & set(own)))
        result += pow(2, matching - 1) if matching > 0 else 0
    return result

def task2(cards):
    amount = [1] * len(cards)

    for card, (winning, own) in enumerate(cards):
        matching = len(list(set(winning) & set(own)))

        for card_won in range(card + 1, card + matching + 1):
            if card_won < len(amount):
                amount[card_won] += amount[card]

    return sum(amount)

def main():
    lines = [line.strip('\n').split(': ')[-1].split(' | ') for line in sys.stdin.readlines()]
    cards = [[list(map(int, groups.split())) for groups in line] for line in lines]

    print(task1(cards))
    print(task2(cards))

if __name__ == "__main__":
    main()