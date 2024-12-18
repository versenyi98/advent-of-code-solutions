import sys
from collections import defaultdict

rows, cols = 7, 7
fallen = 12

# rows, cols = 71, 71
# fallen = 1024

def dfs(graph, node, goals, visited, path):
  queue = [(node, path, 0)]

  while queue:
    node, path, weight = queue.pop(0)

    if node in goals:
      return (node, weight, path)

    visited.append(node)

    for neighbor, w in graph[node]:
      if neighbor in visited:
        continue
      visited.append(neighbor)
      queue.append((neighbor, path + [neighbor], weight + w))

def get_graph(grid):
  directions = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
  graph = defaultdict(list)
  for r, row in enumerate(grid):
    for c, col in enumerate(row):
      if col == '#':
        continue

      for dr, dc in directions:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr == len(grid) or nc < 0 or nc == len(grid[0]) or grid[nr][nc] == '#':
          continue
        graph[(r, c)].append(((nr, nc), 1))

  return graph

def task2(lines):
  left = fallen
  right = len(lines)

  while left + 1 != right:
    middle = (left + right) // 2
    print(f"\r{left} {right} -> {middle}       ", end="")
    grid = [['#' if (c, r) in lines[:middle] else '.' for c in range(cols)] for r in range(rows)]
    graph = get_graph(grid)
    result = dfs(graph, (0, 0), [(cols - 1, rows - 1)], [], [(0, 0)])
    if result == None:
      right = middle
    else:
      left = middle
  print()

  return lines[middle]

def main():
  lines = [tuple(map(int, line.split(','))) for line in sys.stdin.read().split('\n')]
  grid = [['#' if (c, r) in lines[:fallen] else '.' for c in range(cols)] for r in range(rows)]
  graph = get_graph(grid)

  pos, w, path = dfs(graph, (0, 0), [(cols - 1, rows - 1)], [], [(0, 0)])
  print(w)
  print(task2(lines))

if __name__ == "__main__":
    main()