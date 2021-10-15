from cycle_helper import cyclic
import time
from igraph import *

EDGES = [
    ('AB', 12),
    ('BC', 9),
    ('CA', 13),
    ('CD', 12)
]

def creates_cycle(tree: list, edge_candidate: tuple):

    graph = dict()

    if not tree:
        return False

    tree_copy = list(tree)

    tree_copy.append(edge_candidate)

    for edge in tree_copy:
        vertex_source = edge[0][0]
        vertex_target = edge[0][1]

        if not graph.get(vertex_source):
            graph[vertex_source] = (vertex_target,)
        else:
            graph[vertex_source] = graph[vertex_source] + (vertex_target,)
    
    is_cyclicy = cyclic(graph)
    print(f'this graph {graph} is cyclic: {is_cyclicy}')
    plot_graph(tree_copy)
    
    time.sleep(1)
    return is_cyclicy



def kruskal(edges: list) -> list:
    tree = []
    edges_sorted = sorted(edges, key=lambda x: x[1])
    for edges in edges_sorted:
        if not creates_cycle(tree, edges):
            tree.append(edges)

    return tree


def plot_graph(tree):
    formated_tree = []
    for node in tree:
        formated_tree.append((node[0][0], node[0][1], node[1]))

    graph = Graph.TupleList(formated_tree, weights=True)
    plot(graph)

if __name__ == '__main__':
    mst = kruskal(EDGES)
    print('algoritmo finished, ploting mst')
    plot_graph(mst)