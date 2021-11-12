from dataclasses import dataclass
from collections import deque

from node import Node


@dataclass
class BinarySearchTree:
    '''
        Binary Search Tree has the following properties:
            - The left subtree of a node contains only nodes with value lesser than the node’s value.
            - The right subtree of a node contains only nodes with value greater than the node’s value.
            - The left and right subtree each must also be a binary search tree.
            - There must be no duplicate nodes.
    '''

    root: Node

    def printInOrderRecursive(self, node: Node) -> Node:
        if not node:
            return

        self.printInOrderRecursive(node.left)
        print(node.value)
        self.printInOrderRecursive(node.right)
    
    def printInOrderIterative(self) -> None:
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            
            print(node.value)
        
            if node.right:
                queue.append(node.right)
    
    def insertValue(self, value: int, node: Node) -> None:
        if node.value == value:
            return

        elif node.value > value:
            
            if node.left:
                self.insertValue(value=value, node=node.left)
            else:
                node.left = Node(value=value)
                return
        else:
            
            if node.right:
                self.insertValue(value=value, node=node.right)
            else:
                node.right = Node(value=value)
                return


def main():
    # create binary tree
    root = Node(value=0, left=None, right=None)

    binary_tree = BinarySearchTree(root=root)

    ### choose your function ###
    binary_tree.insertValue(1, node=binary_tree.root)
    binary_tree.insertValue(3, node=binary_tree.root)
    binary_tree.insertValue(5, node=binary_tree.root)
    binary_tree.insertValue(7, node=binary_tree.root)
    binary_tree.printInOrderRecursive(node=binary_tree.root)
    # binary_tree.printInOrderIterative()

if __name__ == '__main__':
    main()
