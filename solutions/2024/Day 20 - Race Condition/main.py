import sys
from collections import defaultdict
import heapq

def dijkstra(start, end, edges):
  pq = [(0, start)]
  distances = defaultdict(lambda: float('inf'))
  distances[start] = 0

  while pq:
    cost, node = heapq.heappop(pq)

    if cost > distances[node]:
      continue

    for neighbor, weight in edges[node]:
      new_cost = cost + weight

      if new_cost < distances[neighbor]:
        distances[neighbor] = new_cost
        heapq.heappush(pq, (new_cost, neighbor))

  return distances

def get_graph(grid):
  def get_cheats(row, col, max_dist):
    cheats = []

    for nr in range(row - max_dist, row + max_dist + 1):
      for nc in range(col - max_dist, col + max_dist + 1):
        cost = abs(row - nr) + abs(col - nc)
        if cost > max_dist or cost <= 1:
          continue
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#':
          cheats.append(((r, c), (nr, nc), cost))
    return cheats

  directions = [(-1, 0), (+1, 0), (0, +1), (0, -1)]
  cheats_task1 = []
  cheats_task2 = []
  graph = defaultdict(list)

  for r, row in enumerate(grid):
    for c, col in enumerate(row):
      if col != '#':
        for dr, dc in directions:
          nr, nc = r + dr, c + dc
          if 0 <= nr < len(grid) and 0 <= nc < len(row) and grid[nr][nc] != '#':
            graph[(r, c)].append(((nr, nc), 1))
        cheats_task1 += get_cheats(r, c, 2)
        cheats_task2 += get_cheats(r, c, 20)

  return graph, cheats_task1, cheats_task2

def apply_cheat(distances, cheat):
  pos1, pos2, cost = cheat
  return 1 if distances[pos2] - distances[pos1] - cost >= 100 else 0

def main():
  lines = sys.stdin.read().split('\n')

  graph, cheats_task1, cheats_task2 = get_graph(lines)

  for r, row in enumerate(lines):
    for c, col in enumerate(row):
      if col == 'E':
        end = (r, c)
      elif col == 'S':
        start = (r, c)

  distances = dijkstra(start, end, graph)
  print(sum(apply_cheat(distances, cheat) for cheat in cheats_task1))
  print(sum(apply_cheat(distances, cheat) for cheat in cheats_task2))

if __name__ == "__main__":
    main()