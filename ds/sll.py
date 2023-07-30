class Node:
    def __init__(self, data):
         self.data = data
         self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_linked_list(self):
        node = self.head
        print(f"data = {node.data}")
        next_node = node.next    
        while next_node is not None:
            print(f"data = {next_node.data}")
            next_node = next_node.next

ll = LinkedList()
ll.head = Node(2)
second = Node(4)
third = Node(6)

ll.head.next = second
second.next = third

ll.print_linked_list()
