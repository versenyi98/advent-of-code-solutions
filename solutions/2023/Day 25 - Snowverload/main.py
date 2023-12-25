import sys
import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt
import math

def show_graph(connections):
    plt.figure(figsize=(25, 18))
    G = nx.Graph()
    G.add_edges_from(list(connections))

    important_nodes = ['lrd', 'xsl', 'zlv', 'qpg', 'tpb', 'bmx']
    pos = nx.spring_layout(G, scale=5000)
    nx.draw_networkx_nodes(G, pos, node_size=300)
    if all([n in G.nodes for n in important_nodes]):
        nx.draw_networkx_labels(G, pos, labels={n:n for n in important_nodes})
    nx.draw_networkx_edges(G, pos)
    plt.show()
    plt.savefig("AoC-2023-Day-25.png", format="PNG", bbox_inches="tight")

def main():
    lines = [line.strip("\n").split(': ') for line in sys.stdin.readlines()]
    connections = defaultdict(set, {src: set(dst.split(' ')) for src, dst in lines})
    items = list(connections.items())

    all_connections = set()

    for src, dsts in items:
        for dst in dsts:
            connections[dst].add(src)
            all_connections.add(tuple(sorted([dst, src])))
    show_graph(all_connections)

    to_be_removed = [('lrd', 'qpg'), ('xsl', 'tpb'), ('zlv', 'bmx')]

    for a, b in to_be_removed:
        if a in connections and b in connections[a]:
            connections[a].remove(b)
        if b in connections and a in connections[b]:
            connections[b].remove(a)

    sizes = []
    visited = set()

    for node in connections:
        if node in visited:
            continue
        sizes.append(0)
        queue = [node]

        while len(queue):
            head = queue.pop(0)

            for dst in connections[head]:
                if dst in visited:
                    continue
                visited.add(dst)
                queue.append(dst)
                sizes[-1] += 1

    print(math.prod(sizes))

if __name__ == "__main__":
    main()