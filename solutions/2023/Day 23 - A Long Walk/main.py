import sys
from collections import defaultdict

def dfs(graph, node, goals, visited, depth=0):
    if node in visited:
        return None

    visited.append(node)

    if depth > 0 and node in goals:
        return [(node, depth)]

    results = []
    for neighbour, w in graph[node]:
        if neighbour in visited:
            continue
        visited_copy = visited.copy()
        result = dfs(graph, neighbour, goals, visited_copy, depth + w)
        results += result

    return results

def get_graph(lines, part):
    mapping = {
        '^': (-1, 0),
        'v': (+1, 0),
        '>': (0, +1),
        '<': (0, -1)
    }

    graph = defaultdict(list)
    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            if col == '#':
                continue

            if part == 1 and c in mapping:
                dr, dc = mapping[c]
                graph[(r, c)].append(((r + dr, c + dc), 1))
                continue

            for dr, dc in mapping.values():
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr == len(lines) or nc < 0 or nc == len(lines[0]) or lines[nr][nc] == '#':
                    continue
                if part == 1 and lines[nr][nc] in mapping and mapping[lines[nr][nc]] == (-dr, -dc):
                    continue
                graph[(r, c)].append(((nr, nc), 1))

    return graph

def main():
    sys.setrecursionlimit(5000)

    lines = [line.strip('\n') for line in sys.stdin.readlines()]

    goal = (len(lines) - 1, len(lines[0]) - 2)

    graph_task1 = get_graph(lines, 1)
    results_task1 = dfs(graph_task1, (0, 1), [goal], list())
    print(max([w for _, w in results_task1]))

    intersections = [(0, 1), goal]
    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            if col == '#':
                continue
            neighbours = [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]

            count = 0
            for nr, nc in neighbours:
                if nr >= 0 and nr < len(lines) and nc >= 0 and nc < len(lines[0]) and lines[nr][nc] not in ['.', '#']:
                    count += 1
            if count >= 2:
                intersections.append((r, c))

    base_graph = get_graph(lines, 2)
    graph_task2 = {}

    for intersection in intersections:
        graph_task2[intersection] = dfs(base_graph, intersection, intersections, list())

    results_task2 = dfs(graph_task2, (0, 1), [goal], list())

    print(max([w for _, w in results_task2]))

if __name__ == "__main__":
    main()