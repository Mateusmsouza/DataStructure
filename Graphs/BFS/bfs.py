'''
BFS algorithm in Python
Autor: Mateus Souza
'''


from typing import Tuple
from igraph import *

predecessor = {}
time = {}
level = {}

def bfs(graph: Graph, root_index: int) -> Tuple:
    
    # get tree root by index
    root = graph.vs[root_index]
    i = 1
    ans = 0
    queue = []

    # push root to queu and set its time and level functions
    queue.append(root)
    root['visited'] = True
    time[root['name']] = i
    level[root['name']] = 0

    # run while queue is not empty
    while queue:
        ans += 1
        
        # dequeue a node from queue
        vertex = queue.pop(0)

        print(f'visiting {vertex["name"]}')

        # iteraing over all node's neighbors 
        for neighbor_index in graph.neighbors(vertex):

            neighbor = graph.vs[neighbor_index]

            # if its not visited, check its neighbors too 
            if not neighbor['visited']:
                print(f'setting {neighbor["name"]} as visited')

                # setting each neighbor as visited, predecessor, level and time functions
                # and add it to queue
                neighbor['visited'] = True
                i+=1

                predecessor[neighbor['name']] = vertex['name']
                level[neighbor['name']] = level[vertex['name']] + 1
                time[neighbor['name']] = i
                
                queue.append(neighbor)
    print(f'depht: {ans}')
    return (predecessor, level, time)

if __name__ == '__main__':
    graph = Graph(
        n=2,
        edges=[
            [0,1]
        ]
    )

    for i in range(graph.vcount()):
        graph.vs[i]['name'] = i
        graph.vs[i]['visited'] = False

    predecessor, level, time = bfs(graph, 0)

    print('--------------------------------------')
    print(f'predecessors function: {predecessor}')
    print(f'level function: {level}')
    print(f'time function: {time}')
