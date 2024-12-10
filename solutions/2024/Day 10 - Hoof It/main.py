import sys
from collections import defaultdict

def dfs(graph, node, goals, visited):
  if node in goals:
    return [node]

  results = []
  for neighbor in graph[node]:
    if neighbor not in visited:
      results += dfs(graph, neighbor, goals, visited + [neighbor])

  return results

def get_graph(grid):
  directions = [(-1, 0), (+1, 0), (0, +1), (0, -1)]

  graph = defaultdict(list)
  for r, row in enumerate(grid):
    for c, col in enumerate(row):
      if col != '.':
        for dr, dc in directions:
          nr, nc = r + dr, c + dc
          if 0 <= nr < len(grid) and 0 <= nc < len(row) and \
            grid[nr][nc] != '.' and int(grid[nr][nc]) == int(col) + 1:
            graph[(r, c)].append((nr, nc))

  return graph

def main():
  grid = sys.stdin.read().split('\n')
  goals = [(r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if col == '9']
  graph = get_graph(grid)

  result = [dfs(graph, (r, c), goals, [])
            for r, row in enumerate(grid)
            for c, col in enumerate(row)
            if col == '0']

  print(f"Task 1: {sum(map(len, map(set, result)))}")
  print(f"Task 2: {sum(map(len, result))}")

if __name__ == "__main__":
    main()