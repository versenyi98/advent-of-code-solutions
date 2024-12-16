import sys
from collections import defaultdict
import heapq

def task1(graph, start, targets):
  def bfs(graph, start, targets):
    pq = []
    heapq.heappush(pq, (0, start, [(start, 0)]))

    visited = set()
    while pq:
      priority, node, path = heapq.heappop(pq)

      if node in targets:
        return (priority, node, path)

      if node in visited:
        continue

      visited.add(node)

      for nr, nc, nd, w in graph[node]:
        if (nr, nc, nd) not in visited:
          heapq.heappush(pq, (priority + w, (nr, nc, nd), path + [((nr, nc, nd), priority + w)]))
  return bfs(graph, start, targets)

def task2(graph, start, targets):
  def bfs(graph, start, targets):
    pq = []
    heapq.heappush(pq, (0, start, [(start, 0)]))
    visited = set()
    results = set()

    while pq:
      priority, node, path = heapq.heappop(pq)

      if (node, priority) in targets:
        for (path_node, path_priority) in path:
          targets.add((path_node, path_priority))

      if node in visited:
        continue

      visited.add(node)

      for nr, nc, nd, w in graph[node]:
        heapq.heappush(pq, (priority + w, (nr, nc, nd), path + [((nr, nc, nd), priority + w)]))
    return targets
  return bfs(graph, start, targets)

def get_graph(grid):
  directions = [(-1, 0), (0, -1), (+1, 0), (0, +1)]
  graph = defaultdict(list)
  for r, row in enumerate(grid):
    for c, col in enumerate(row):
      if col == '#':
        continue

      for di, (dr, dc) in enumerate(directions):
        graph[(r, c, di)].append((r, c, (di + 1) % 4, 1000))
        graph[(r, c, di)].append((r, c, (di - 1) % 4, 1000))
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr == len(grid) or nc < 0 or nc == len(grid[0]) or grid[nr][nc] == '#':
          continue
        graph[(r, c, di)].append((nr, nc, di, 1))

  return graph

def get_unique_positions(path):
  return set([(r, c) for (r, c, _), _ in path])

def main():
  lines = sys.stdin.read().split('\n')
  graph = get_graph(lines)

  for r, row in enumerate(lines):
    for c, col in enumerate(row):
      if col == 'S':
        start_pos = (r, c, 3)
      if col == 'E':
        end_pos = (r, c)

  task1_result = task1(graph, start_pos, [(end_pos[0], end_pos[1], direction) for direction in range(4)])
  print(task1_result[0])

  targets = set(task1_result[2])
  last_result = len(get_unique_positions(targets))
  while True:
    targets = task2(graph, start_pos, targets)
    result = len(get_unique_positions(targets))

    if last_result != result:
      last_result = result
    else:
      break
  print(result)

if __name__ == "__main__":
    main()