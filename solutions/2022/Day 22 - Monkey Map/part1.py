import sys

from enum import Enum


class Direction(Enum):
    UP = 3
    RIGHT = 0
    DOWN = 1
    LEFT = 2


class Cell:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def __str__(self):
        return f"Cell({self.row},{self.col},'{self.value}')"


def search_for_next_valid_cell(pos, direction):
    dir_row, dir_col = direction
    curr_row, curr_col = pos

    while True:
        curr_col = (curr_col + dir_col + width) % width
        curr_row = (curr_row + dir_row + height) % height
        if cells[curr_row][curr_col].value != ' ':
            return cells[curr_row][curr_col]


grid, moves = sys.stdin.read().split("\n\n")
grid = grid.split("\n")

width = max([len(row) for row in grid])
height = len(grid)

cells = []
current_cell = None
current_direction = Direction.RIGHT

for idx in range(height):
    grid[idx] = grid[idx] + " " * (width - len(grid[idx]))

for row_idx, row_val in enumerate(grid):
    cells.append([])
    for col_idx, col_val in enumerate(row_val):
        cells[-1].append(Cell(col_val, row_idx, col_idx))

for row_idx, row_val in enumerate(cells):
    for col_idx, cell in enumerate(row_val):
        if cell.value == ' ':
            continue

        if current_cell is None:
            current_cell = cell

        if cell.up is None:
            up = search_for_next_valid_cell((row_idx, col_idx), (-1, 0))
            cell.up = up

        if cell.down is None:
            down = search_for_next_valid_cell((row_idx, col_idx), (+1, 0))
            cell.down = down

        if cell.right is None:
            right = search_for_next_valid_cell((row_idx, col_idx), (0, +1))
            cell.right = right

        if cell.left is None:
            left = search_for_next_valid_cell((row_idx, col_idx), (0, -1))
            cell.left = left

        assert cell.row == cell.left.row, f"{cell} {cell.left}"
        assert cell.row == cell.right.row, f"{cell} {cell.right}"
        assert cell.col == cell.up.col, f"{cell} {cell.up}"
        assert cell.col == cell.down.col, f"{cell} {cell.down}"

move_distances = (list(map(int, moves.replace("R", "-").replace("L", "-").split("-"))))
move_turns = list(filter(lambda x: x == "L" or x == "R", moves)) + [""]

for distance, turn in zip(move_distances, move_turns):
    while distance:
        distance -= 1
        next_cell = None

        if current_direction == Direction.RIGHT:
            next_cell = current_cell.right
        if current_direction == Direction.LEFT:
            next_cell = current_cell.left
        if current_direction == Direction.UP:
            next_cell = current_cell.up
        if current_direction == Direction.DOWN:
            next_cell = current_cell.down

        if next_cell.value == '#':
            distance = 0
            continue

        current_cell = next_cell

    diff = 0
    if turn == "R":
        diff = 1
    elif turn == "L":
        diff = -1
    current_direction = Direction((current_direction.value + diff + 4) % 4)

print(1000 * (current_cell.row + 1) + 4 * (current_cell.col + 1) + current_direction.value)