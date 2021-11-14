from node import Node

from print import recursive_print
from add import add

def main():
    linked_list = Node(content=0, next=None)
    
    for i in range(1, 5):
        add(node=linked_list, value=i)
    
    recursive_print(linked_list)

if __name__ == '__main__':
    main()