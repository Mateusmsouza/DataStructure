from dataclasses import dataclass

@dataclass
class Node:
    '''Class for representing a Node.'''

    value: int
    right: object = None
    left: object = None