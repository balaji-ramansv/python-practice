class SllNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
    
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
    
    def has_next(self):
        if self.next is not None:
            return True
        else:
            return False

class Sll(object):
    def __init__(self, node=None):
        self.head = node
        self.length = 0

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            current += 1
            current = current.next
        return count
    
    def insert_at_beginning(self, data):
        node = SllNode()
        node.set_data(data)
        if self.length == 0:
            self.head = node
        else:
            node.set_next(self.head)
        self.length += 1