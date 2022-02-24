
import json
import networkx as nx
import numpy as np
import time


def graph():
    paths = json.loads(open('paths.json').read())

    n = [int(n) for n in set(paths.keys())]
    g = nx.Graph()
    g.add_nodes_from(n)
    for k,v in paths.items():
        g.add_edges_from([(int(k), t) for t in v])

    return g

def main():
    g = graph()
    n = list(g.nodes)
    print( nx.shortest_path(g, n[0], n[-1]) )

    s = time.time()
    path = dict(nx.all_pairs_shortest_path(g))
    e = time.time()
    print(f"All pairs in {e-s} seconds")
