import sys
from collections import Counter
from functools import cmp_to_key

rank_of_cards = {}
joker = False

def n_of_a_kind(hand, n):
    counter = Counter(hand)

    if not joker:
        return n in counter.values()
    else:
        jokers = counter['J']
        return len([v for k, v in counter.items() if v == n or (k != 'J' and v + jokers == n)]) > 0

def full_house(hand):
    if not joker:
        counter = Counter(hand)
        return 2 in counter.values() and 3 in counter.values()
    else:
        without_joker = {card for card in hand if card != 'J'}
        counter = Counter(without_joker)
        return len(without_joker) <= 2 and len([value for value in counter.values() if value >= 4]) == 0

def two_pair(hand):
    if not joker:
        counter = Counter(hand)
        counter = Counter(counter.values())
        return counter.get(2, 0) == 2
    else:
        without_joker = {card for card in hand if card != 'J'}
        counter = Counter(without_joker)

        if len(without_joker) <= 3:
            return True
        elif len(without_joker) == 5:
            counter = Counter(hand)
            counter = Counter(counter.values())
            return counter.get(2, 0) == 2
        else:
            return len([value for key, value in counter.items() if value == 2]) > 0

def rank(hand):
    if n_of_a_kind(hand, 5):
        return 6
    elif n_of_a_kind(hand, 4):
        return 5
    elif full_house(hand):
        return 4
    elif n_of_a_kind(hand, 3):
        return 3
    elif two_pair(hand):
        return 2
    elif n_of_a_kind(hand, 2):
        return 1
    return 0

def compare(a, b):
    hand_a = a[0]
    hand_b = b[0]

    if rank(hand_a) == rank(hand_b):
        for card_a, card_b in zip(list(hand_a), list(hand_b)):
            if rank_of_cards.get(card_a) != rank_of_cards.get(card_b):
                if rank_of_cards.get(card_a) > rank_of_cards.get(card_b):
                    return 1
                else:
                    return -1
    elif rank(hand_a) > rank(hand_b):
        return 1
    return -1

def task1(lines):
    sorted_lines = sorted(lines, key=cmp_to_key(compare))
    return sum([int(bet) * multiplier for multiplier, [_, bet] in enumerate(sorted_lines, 1)])

def task2(lines):
    global rank_of_cards
    rank_of_cards['J']  = 1

    global joker
    joker = True

    sorted_lines = sorted(lines, key=cmp_to_key(compare))
    return sum([int(bet) * multiplier for multiplier, [_, bet] in enumerate(sorted_lines, 1)])

def main():
    global rank_of_cards
    rank_of_cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    rank_of_cards.update({str(num): num for num in range(2, 10)})

    lines = [line.strip('\n').split(' ') for line in sys.stdin.readlines()]
    print(task1(lines))
    print(task2(lines))

if __name__ == "__main__":
    main()