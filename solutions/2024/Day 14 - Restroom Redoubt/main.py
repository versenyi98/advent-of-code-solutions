import os
import sys
import re
import math
from PIL import Image

cols = 101  # in case of secret input
rows = 103  # in case of secret input

def get_position_after_rounds(col, row, v_col, v_row, rounds):
  return (col + rounds * v_col) % cols, (row + rounds * v_row) % rows

def task1(lines):
  positions1 = [*(get_position_after_rounds(*line, 100) for line in lines)]
  quadrants = [0] * 4

  for col, row in positions1:
    if col < cols // 2 and row < rows // 2:
      quadrants[0] += 1
    elif col > cols // 2 and row < rows // 2:
      quadrants[1] += 1
    elif col < cols // 2 and row > rows // 2:
      quadrants[2] += 1
    elif col > cols // 2 and row > rows // 2:
      quadrants[3] += 1

  return math.prod(quadrants)

def task2(lines):
  current_round = 7623
  positions = [get_position_after_rounds(col, row, v_col, v_row, current_round)
                for col, row, v_col, v_row in lines]
  grid = [['.' if (col, row) not in positions else '#'
           for col in range(cols)] for row in range(rows)]

  for row in grid:
    print("".join(row))

def generate_images(lines, rounds):
  os.makedirs("res", exist_ok=True)
  for current_round in range(rounds):
    print(f"\rRound: {current_round + 1}/{rounds}", end="")
    positions = [get_position_after_rounds(col, row, v_col, v_row, current_round)
                  for col, row, v_col, v_row in lines]
    grid = [[0 if (col, row) not in positions else 1
             for col in range(cols)] for row in range(rows)]

    image = Image.new("1", (cols, rows))
    flat_data = [pixel for row in grid for pixel in row]
    image.putdata(flat_data)
    image.save(f"res/output_image_{current_round}.png")
  print()


def main():
  pattern = r"-?\d+"
  lines = [list(map(int, re.findall(pattern, line))) for line in sys.stdin.read().split('\n')]
  print(task1(lines))
  # generate_images(lines, 100)
  task2(lines)

if __name__ == "__main__":
  main()