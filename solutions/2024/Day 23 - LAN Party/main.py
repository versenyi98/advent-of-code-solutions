import sys
from collections import defaultdict

graph = defaultdict(list)

def task1(graph):
    results = set()

    for node in graph:
        if node.startswith('t'):
            for neighbor1 in graph[node]:
                for neighbor2 in graph[neighbor1]:
                    if neighbor2 in graph[node]:
                        results.add(tuple(sorted([node, neighbor1, neighbor2])))
    return len(results)


def bron_kerbosch(R, P, X, graph, max_clique):
    if not P and not X:
        if len(R) > len(max_clique[0]):
            max_clique[0] = R[:]
        return

    for v in list(P):
        bron_kerbosch(R + [v], 
                      [u for u in P if u in graph[v]], 
                      [u for u in X if u in graph[v]], 
                      graph, 
                      max_clique)
        P.remove(v)
        X.append(v)

def largest_clique(graph):
    max_clique = [[]]  # To store the largest clique found
    bron_kerbosch([], list(graph.keys()), [], graph, max_clique)
    return max_clique[0]

def main():
    lines = [line.split('-') for line in sys.stdin.read().split('\n')]
    for computer1, computer2 in lines:
        graph[computer1].append(computer2)
        graph[computer2].append(computer1)

    print(task1(graph))
    print(",".join(sorted(largest_clique((graph)))))

if __name__ == "__main__":
    main()