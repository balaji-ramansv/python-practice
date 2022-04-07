from copy import deepcopy

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.curr_node = None
        self.next_node = None

    def insert_data_at_beginning(self, data):
        self.__create_node(data)
        if self.head is None:
            self.head = self.curr_node
        else:
            self.curr_node.next = self.head
            self.head = self.curr_node

    def insert_data_at_random_pos(self, data, pos):
        self.__create_node(data)
        curr_pos = 0
        curr = self.head
        if self.head is None:
            self.head = self.curr_node
        end_reached = False
        while curr_pos < pos:
            curr_pos += 1
            if self.head.next is None:
                break
            else:
                curr = self.head.next
        curr.next = self.curr_node
        if not end_reached:
            self.curr_node.next = self.head.next
        self.head = self.curr_node

    def __create_node(self, data):
        self.curr_node = SinglyLinkedListNode()
        self.curr_node.insert_data(data)
        


    def length(self):
        length = 0
        while self.head.next is not None:
            length += 1
        return length

class SinglyLinkedListNode:
    def __init__(self):
        self.data = None
        self.next = SinglyLinkedListNode
    
    def insert_data(self, data):
        self.data = data

    def insert_next(self, nxt):
        self.next = nxt

def print_linked_list(node: SinglyLinkedListNode):
    while hasattr(node, 'next'):
        print(node.data)
        node = node.next

if __name__ == '__main__':
    llist = SinglyLinkedList()
    for i in range(5):
        llist_item = int(input())
        #llist.insert_data_at_beginning(llist_item)
        llist.insert_data_at_random_pos(llist_item, i+1)

    print_linked_list(llist.head)