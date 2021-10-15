from re import T
from cycle_helper import cyclic
import time
from igraph import *

EDGES = [
    ('AB', 12),
    ('BC', 9),
    ('CD', 13),
    ('DB', 13),
    ('DE', 15),
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
#    plot_graph(tree_copy)
    
    return is_cyclicy



def kruskal(edges: list) -> list:
    forest = []
    tree = []
    edges_sorted = sorted(edges, key=lambda x: x[1])
    for index_edge in range(len(edges_sorted)):
        
        edge = edges_sorted[index_edge]
        next_edge = None

        # check if is there a next edge
        if index_edge < len(edges_sorted) - 1:
            next_edge = edges_sorted[1+index_edge]

        # check is current edge has same weight as the next one
        if next_edge and edge[1] == next_edge[1]:
            print(f'duplicated weight edges: {edge} {next_edge}')
            tree_copy = list(tree)
            tree_copy.append(next_edge)

            forest = forest + kruskal(tree_copy)
        if not creates_cycle(tree, edge):
            tree.append(edge)

    forest.append(tree)

    return forest


def plot_graph(tree):
    formated_tree = []
    for node in tree:
        formated_tree.append((node[0][0], node[0][1], node[1]))

    graph = Graph.TupleList(formated_tree, weights=True)

    for edge in graph.es:
        edge['label'] = edge['weight']
    plot(graph)

if __name__ == '__main__':
    plot_graph(EDGES)
    forest = kruskal(EDGES)
    print(forest)
    for mst in forest:
        print('algoritmo finished, ploting mst')
        plot_graph(mst)
    