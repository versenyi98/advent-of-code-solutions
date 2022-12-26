import sys
from copy import deepcopy

def get_sequences_to_watch(board):
    sequences_to_watch = [set(row) for row in board]

    for i in range(5):
        seq = set()
        for j in range(5):
            seq.add(board[j][i])
        sequences_to_watch.append(seq)

    diag = set(board[i][i] for i in range(5))
    other_diag = set(board[4 - i][i] for i in range(5))

    sequences_to_watch += [diag, other_diag]

    return sequences_to_watch


def get_winner():
    for idx, sequences in sequences_to_watch.items():
        for sequence in sequences:
            if len(set.intersection(sequence, already_drawn)) == 5:
                return idx
    return None


def get_score(idx):
    sum_of_unmarked = 0
    for row in boards[idx]:
        for element in row:
            if element not in already_drawn:
                sum_of_unmarked += element
    return last_called * sum_of_unmarked


def draw_until_someone_wins(already_drawn):
    while get_winner() is None:
        last_called = numbers.pop(0)
        already_drawn.add(last_called)
    return last_called


def draw_until_almost_everyone_wins(already_drawn):
    while len(sequences_to_watch) != 1:
        last_called = numbers.pop(0)
        already_drawn.add(last_called)
        while get_winner() is not None:
            winner = get_winner()
            sequences_to_watch.pop(winner)


lines = sys.stdin.read()

numbers = list(map(int, lines.split("\n\n")[0].split(",")))
boards = [board.split("\n") for board in lines.split("\n\n")[1:]]

sequences_to_watch = {}

for idx, board in enumerate(boards):
    parsed_board = [list(map(int, row.split())) for row in board]
    boards[idx] = parsed_board
    sequences_to_watch[idx] = get_sequences_to_watch(parsed_board)


numbers_copy = deepcopy(numbers)

already_drawn = set()
last_called = draw_until_someone_wins(already_drawn)
print(get_score(get_winner()))

numbers = numbers_copy
already_drawn = set()
draw_until_almost_everyone_wins(already_drawn)
last_called = draw_until_someone_wins(already_drawn)
print(get_score(get_winner()))
