from node import Node

def add(node: Node, value: int) -> None:
    """
    recursive function to add a value to a linked list.
    time complexity: O(n) where n is the height of the tree

    Args:
        node (Node): [description]
        value (int): [description]
    """    
    if node.next:
        add(node.next, value=value)
        return

    node.next = Node(content=value, next=None)