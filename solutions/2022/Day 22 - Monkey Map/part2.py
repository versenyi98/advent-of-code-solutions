import sys

from enum import Enum

RIGHT = (0, +1)
DOWN = (+1, 0)
LEFT = (0, -1)
UP = (-1, 0)

directions = [
    RIGHT,
    DOWN,
    LEFT,
    UP
]

directions_sign = [">", "v", "<", "^"]


class Cell:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.neighbour = [None] * 4

    def __str__(self):
        return f"Cell({self.row},{self.col},'{self.value}')"


class Face(Enum):
    TOP = 0
    FRONT = 1
    RIGHT = 2
    BACK = 3
    LEFT = 4
    BOTTOM = 5


# for my input, shouldn't work with example
def get_face(pos, cube_size=50):
    row, col = pos
    mapping = {
        (0, 1): Face.TOP,
        (0, 2): Face.RIGHT,
        (1, 1): Face.FRONT,
        (2, 0): Face.LEFT,
        (2, 1): Face.BOTTOM,
        (3, 0): Face.BACK
    }
    return mapping[(row // cube_size, col // cube_size)]


# for my input, shouldn't work with example
def get_special(pos, direction, cube_size=50):
    row, col = pos
    face = get_face(pos, cube_size)

    specials = {
        Face.TOP: {
            LEFT: (149 - row, 0),
            UP: (col + 100, 0)
        },
        Face.RIGHT: {
            UP: (199, col - 100),
            RIGHT: (149 - row, 99),
            DOWN: (col - 50, 99)
        },
        Face.FRONT: {
            RIGHT: (49, row + 50),
            LEFT: (100, row - 50)
        },
        Face.BOTTOM: {
            RIGHT: (149 - row, 149),
            DOWN: (col + 100, 49)
        },
        Face.LEFT: {
            LEFT: (149 - row, 50),
            UP: (col + 50, 50),
        },
        Face.BACK: {
            DOWN: (0, col + 100),
            LEFT: (0, row - 100),
            RIGHT: (149, row - 100)
        }
    }
    return specials[face][direction]


# for my input, shouldn't work with example
direction_change = {
    Face.TOP: {
        RIGHT: RIGHT,
        DOWN: DOWN,
        LEFT: RIGHT,
        UP: RIGHT,
    },
    Face.RIGHT: {
        RIGHT: LEFT,
        DOWN: LEFT,
        LEFT: LEFT,
        UP: UP,
    },
    Face.FRONT: {
        RIGHT: UP,
        DOWN: DOWN,
        LEFT: DOWN,
        UP: UP,
    },
    Face.BOTTOM: {
        RIGHT: LEFT,
        DOWN: LEFT,
        LEFT: LEFT,
        UP: UP,
    },
    Face.LEFT: {
        RIGHT: RIGHT,
        DOWN: DOWN,
        LEFT: RIGHT,
        UP: RIGHT,
    },
    Face.BACK: {
        RIGHT: UP,
        DOWN: DOWN,
        LEFT: DOWN,
        UP: UP,
    }
}

grid, moves = sys.stdin.read().split("\n\n")
grid = grid.split("\n")

width = max([len(row) for row in grid])
height = len(grid)

cells = []
current_cell = None
current_direction_idx = 0
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
        face = get_face((row_idx, col_idx))
        specials = []
        # LEFT
        # for my input, shouldn't work with example
        if col_idx % 50 == 0:
            if face not in [Face.RIGHT, Face.BOTTOM]:
                specials.append(LEFT)
        # RIGHT
        # for my input, shouldn't work with example
        if col_idx % 50 == 49:
            if face not in [Face.TOP, Face.LEFT]:
                specials.append(RIGHT)
        # UP
        # for my input, shouldn't work with example
        if row_idx % 50 == 0:
            if face not in [Face.BOTTOM, Face.BACK, Face.FRONT]:
                specials.append(UP)
        # DOWN
        # for my input, shouldn't work with example
        if row_idx % 50 == 49:
            if face not in [Face.TOP, Face.FRONT, Face.LEFT]:
                specials.append(DOWN)

        if current_cell is None:
            current_cell = cell

        for direction_idx, direction in enumerate(directions):
            if cell.neighbour[direction_idx] is None and direction not in specials:
                neighbour = cells[row_idx + direction[0]][col_idx + direction[1]]
                cell.neighbour[direction_idx] = neighbour
                neighbour.neighbour[(direction_idx + 2) % 4] = cell
            if direction in specials:
                neighbour_row, neighbour_col = get_special((row_idx, col_idx), direction)
                neighbour = cells[neighbour_row][neighbour_col]
                cell.neighbour[direction_idx] = neighbour

        for direction_idx, direction in enumerate(directions):
            if direction in specials:
                continue
            if direction[0]:
                assert cell.col == cell.neighbour[direction_idx].col
            else:
                assert cell.row == cell.neighbour[direction_idx].row

move_distances = (list(map(int, moves.replace("R", "-").replace("L", "-").split("-"))))
move_turns = list(filter(lambda x: x == "L" or x == "R", moves)) + [""]

for distance, turn in zip(move_distances, move_turns):
    while distance:
        distance -= 1

        current_face = get_face((current_cell.row, current_cell.col))
        current_cell.value = directions_sign[current_direction_idx]
        next_cell = current_cell.neighbour[current_direction_idx]
        if next_cell.value == '#':
            distance = 0
            continue
        next_face = get_face((next_cell.row, next_cell.col))
        if current_face != next_face:
            new_direction = direction_change[current_face][directions[current_direction_idx]]
            current_direction_idx = directions.index(new_direction)
        current_cell = next_cell

    diff = 0
    if turn == "R":
        diff = 1
    elif turn == "L":
        diff = -1
    current_direction = directions[(current_direction_idx + diff + 4) % 4]
    current_direction_idx = directions.index(current_direction)

print(1000 * (current_cell.row + 1) + 4 * (current_cell.col + 1) + current_direction_idx)