class Node:
    def __init__(self, data):
         self.data = data
         self.next = None

    def __str__(self):
        return f"DATA: {self.data}; NEXT: {self.next};;  "

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def get_length(self, print_len=False):
        if print_len:
            print(f"Length of the linked list is {self.__length}")
        return self.__length

    def insert_at_head(self, node):
        print("Inserting at head...")
        if self.get_length() == 0:
            self.__head = node
            self.__tail = self.__head
        else:
            node.next = self.__head
            self.__head = node
        self.__length += 1

    def insert_at_tail(self, node):
        print("Inserting at tail...")
        if self.get_length() == 0:
            self.insert_at_head(node)
        else:
            self.__tail.next = node
            self.__tail = self.__tail.next
        self.__length += 1

    def does_data_exist(self, data):
        print(f"Checking if {data} exists...")
        traversal_node = self.__head
        while traversal_node is not None:
            if traversal_node.data == data:
                return True
            traversal_node = traversal_node.next
        return False

    def delete_at_pos(self, pos):
        print(f"Attempting to delete at pos {pos}")
        traversal_node = self.__head
        ll_len = self.get_length(print_len=True)
        if pos > ll_len:
            raise Exception("Can't delete node at position > len")
        if pos < 0:
            raise Exception("Invalid pos. pos must be +ve")
        if pos == 0:
            self.__head = self.__head.next
        else:
            counter = 0
            prev = None
            while counter < pos and traversal_node is not None:
                prev = traversal_node
                traversal_node = traversal_node.next
                counter += 1
            if counter == pos:
                prev.next = prev.next.next
        self.__length -= 1

    def get_data_at_pos(self, pos):
        print(f"Attempting to get data at pos {pos}")
        curr_pos = 0
        traversal_node = self.__head
        while curr_pos <= pos and traversal_node is not None:
            if curr_pos == pos:
                return traversal_node.data
            curr_pos += 1
            traversal_node = traversal_node.next
        return None

    def __str__(self):
        ll_str = f"[{self.__head.data}|"
        node = self.__head
        while node.next is not None:
            ll_str += "-]----->"
            node = node.next
            ll_str += f"[{node.data}|"
        ll_str += f"-]----->{node.next}"
        return ll_str

ll = LinkedList()
ll.insert_at_head(Node(11))
print(ll)
ll.insert_at_head(Node(22))
print(ll)
ll.insert_at_head(Node(33))
print(ll)
ll.insert_at_head(Node(44))
print(ll)
ll.insert_at_head(Node(55))
print(ll)
ll.insert_at_tail(Node(66))
print(ll)
ll.delete_at_pos(ll.get_length() - 1)
print(ll)
ll.delete_at_pos(0)
print(ll)
print(ll.does_data_exist(22))
print(ll)
print(ll.get_data_at_pos(100))
print(ll)
