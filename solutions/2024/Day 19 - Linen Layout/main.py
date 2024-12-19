import sys
from collections import defaultdict

def find_all_indices_of_substring(string, substring):
  indices = []
  start = 0
  while True:
    start = string.find(substring, start)
    if start == -1:
      break
    indices.append(start)
    start += 1
  return indices

def dfs(graph, node, goals, visited, path):
  queue = [(node, path)]
  results = []

  while queue:
    node, path = queue.pop(0)

    if node in goals:
      return [(node, path)]

    visited.append(node)

    for neighbor in graph[node]:
      if neighbor in visited:
        continue
      visited.append(neighbor)
      queue.append((neighbor, path + [neighbor]))
  return []

def get_number_of_all_paths(graph, index, pattern, visited):
  if index in visited:
    return visited[index]
  if index == len(pattern):
    return 1
  if index > len(pattern):
    return 0
  visited[index] = sum(get_number_of_all_paths(graph, neighbor, pattern, visited) for neighbor in graph[index])
  return visited[index]

def get_graph(pattern, towels):
  graph = defaultdict(list)
  for towel in towels:
    indices = find_all_indices_of_substring(pattern, towel)
    for index in indices:
      graph[index].append(index + len(towel))
  return graph

def solution(towels, patterns):
  task1 = 0
  task2 = 0
  for pattern in patterns:
    graph = get_graph(pattern, towels)
    task1 += len(dfs(graph, 0, [len(pattern)], [], [0]))
    task2 += get_number_of_all_paths(graph, 0, pattern, {})
  return task1, task2

def main():
  towels, patterns = sys.stdin.read().split('\n\n')
  towels = towels.split(', ')
  patterns = patterns.split('\n')

  print(solution(towels, patterns))

if __name__ == "__main__":
    main()