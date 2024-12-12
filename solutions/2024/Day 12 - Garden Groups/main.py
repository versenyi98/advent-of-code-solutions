import sys

vertical_directions = [(-1, 0), (+1, 0)]
horizontal_directions = [(0, -1), (0, +1)]
directions = vertical_directions + horizontal_directions

def area(patch):
  return len(patch)

def perimeter(patch):
  return sum((1 if (r + dr, c + dc) not in patch else 0
              for (r, c) in patch
              for (dr, dc) in directions))

def sides(patch):
  increased_patch = set()
  for r, c in patch:
    increased_patch.add((2 * r,     2 * c))
    increased_patch.add((2 * r + 1, 2 * c))
    increased_patch.add((2 * r,     2 * c + 1))
    increased_patch.add((2 * r + 1, 2 * c + 1))

  vertical_perimeter, horizontal_perimeter = set(), set()
  for (r, c) in increased_patch:
    for (dr, dc) in vertical_directions:
      if (new := (r + dr, c + dc)) not in increased_patch:
        vertical_perimeter.add(new)
    for (dr, dc) in horizontal_directions:
      if (new := (r + dr, c + dc)) not in increased_patch:
        horizontal_perimeter.add(new)

  sides = 0

  perimeters = [vertical_perimeter, horizontal_perimeter]
  directions = [horizontal_directions, vertical_directions]

  for perimeter, directions in zip(perimeters, directions):
    visited = set()
    for row, col in perimeter:
      if (row, col) in visited:
        continue
      sides += 1
      queue = [(row, col)]
      visited.add((row, col))

      while queue:
        row, col = queue.pop(0)
        for dr, dc in directions:
          nr = dr + row
          nc = dc + col
          if (nr, nc) in perimeter and (nr, nc) not in visited:
            visited.add((nr, nc))
            queue.append((nr, nc))
  return sides

def get_details(grid):
  rows, cols = len(grid), len(grid[0])

  def flood_fill(grid, row, col):
    original = grid[row][col]
    directions = [(-1, 0), (+1, 0), (0, +1), (0, -1)]
    queue = [(row, col)]
    grid[row][col] = -1
    patch = {(row, col)}

    while queue:
      r, c = queue.pop(0)
      for dr, dc in directions:
        nr, nc = dr + r, dc + c
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == original:
          grid[nr][nc] = -1
          patch.add((nr, nc))
          queue.append((nr, nc))
    return area(patch), perimeter(patch), sides(patch)

  return [flood_fill(grid, r, c) for r in range(rows) for c in range(cols) if grid[r][c] != -1]

def main():
  grid = list(map(list, sys.stdin.read().split('\n')))
  details = get_details(grid)

  print(f"Task 1: {sum((a * p for a, p, s in details))}")
  print(f"Task 2: {sum((a * s for a, p, s in details))}")

if __name__ == "__main__":
    main()