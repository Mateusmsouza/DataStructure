from node import Node

def recursive_print(node: Node) -> None:
    """recursive print has time complexity of O(n) where n is linked list height

    Args:
        node (Node): [description]
    """    
    if node:
       print(f'{node.content}')
       recursive_print(node.next)
