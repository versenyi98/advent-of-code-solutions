import sys

directions = {
  '^': (-1, 0),
  'v': (+1, 0),
  '>': (0, +1),
  '<': (0, -1)
}

def get_robot_position(grid):
  for r, row in enumerate(grid):
    for c, col in enumerate(row):
      if col == '@':
        return r, c

def task1(grid, moves):
  rr, rc = get_robot_position(grid)

  for move in moves:
    dr, dc = directions[move]
    num_of_boxes = 1
    while True:
      nr = rr + num_of_boxes * dr
      nc = rc + num_of_boxes * dc

      if grid[nr][nc] == '#':
        break
      elif grid[nr][nc] == 'O':
        num_of_boxes += 1
      else:
        for n in range(num_of_boxes, 0, -1):
          grid[rr + n * dr][rc + n * dc] = grid[rr + (n - 1) * dr][rc + (n - 1) * dc]
        grid[rr][rc] = '.'
        rr, rc = rr + dr, rc + dc
        break

  return sum(100 * r + c for r, row in enumerate(grid) for c, col in enumerate(row) if col == 'O')

def task2(grid, moves):
  rr, rc = get_robot_position(grid)

  for move in moves:
    dr, dc = directions[move]

    # List of lists, to keep track of all the boxes to be moved.
    # The last list always contains the newly found boxes.
    boxes_moved = [list()]
    boxes_moved[-1].append((rr, rc))

    pushed_to_wall = False
    while True:
      new_boxes_moved = list()

      # Consider only the boxes found in the last round
      for moved_cell in boxes_moved[-1]:
        moved_r, moved_c = moved_cell
        nr = moved_r + dr
        nc = moved_c + dc

        if grid[nr][nc] == '#':
          pushed_to_wall = True
          break
        # we found a new box, and it is not pushed by the other side of the box
        elif grid[nr][nc].isdigit() and grid[nr][nc] != grid[moved_r][moved_c] and (nr, nc) not in new_boxes_moved:
          if dc == 0:
            # we don't care about the order of the box pieces in the list, when
            # the movement is vertical aka dc is 0
            new_boxes_moved.append((nr, nc))
            if grid[nr][nc + 1] == grid[nr][nc] and (nr, nc + 1) not in new_boxes_moved:
              new_boxes_moved.append((nr, nc + 1))
            if grid[nr][nc - 1] == grid[nr][nc] and (nr, nc - 1) not in new_boxes_moved:
              new_boxes_moved.append((nr, nc - 1))
          else:
            # the order of box pieces is important, so the box pieces won't overlap while moving
            # -> ...[]... ; ...[.].. ; ....[]..   Correct
            # -> ...[]... ; ....[...              Incorrect, the other side should've moved first
            if grid[nr][nc + dc] == grid[nr][nc] and (nr, nc + dc) not in new_boxes_moved:
              new_boxes_moved.append((nr, nc + dc))
              new_boxes_moved.append((nr, nc))
            if grid[nr][nc - dc] == grid[nr][nc] and (nr, nc - dc) not in new_boxes_moved:
              new_boxes_moved.append((nr, nc))
              new_boxes_moved.append((nr, nc - dc))
      if pushed_to_wall:
        break
      if len(new_boxes_moved) > 0:
        boxes_moved.append(new_boxes_moved)
      else:
        break
    if pushed_to_wall:
      continue

    # move boxes and robot
    for boxes in boxes_moved[::-1]:
      for box in boxes:
        grid[box[0] + dr][box[1] + dc] = grid[box[0]][box[1]]
        grid[box[0]][box[1]] = '.'

    rr, rc = rr + dr, rc + dc
  return sum(100 * r + c for r, row in enumerate(grid) for c, col in enumerate(row) if col.isdigit() and col == row[c + 1])

def main():
  grid, moves = sys.stdin.read().split('\n\n')
  grid = list(map(list, grid.split('\n')))
  modified_grid = [list("".join(line).replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')) for line in grid]

  box_counter = 0
  for r, row in enumerate(modified_grid):
    for c, col in enumerate(row):
      if col == '[':
        modified_grid[r][c] = str(box_counter)
        modified_grid[r][c + 1] = str(box_counter)
        box_counter += 1

  moves = "".join(moves.split('\n'))

  print(task1(grid, moves))
  print(task2(modified_grid, moves))

if __name__ == "__main__":
    main()