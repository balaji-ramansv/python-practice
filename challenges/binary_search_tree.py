class Bst:
    def __init__(self, *, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.tree_height = 1
    
    def create_left(self, *, data, left=None, right=None):
        self.left = Bst(data=data, left=left, right=right)

    def create_right(self, *, data, left=None, right=None):
        self.right = Bst(data=data, left=left, right=right)

    def get_left(self):
        return self.left
    
    def set_data(self, data):
        self.data = data
    
    def get_right(self):
        return self.right
    
    def __str__(self):
        #return self.__get_tree()
        return ""

    def __get_tree(self):
        height = self.get_height()
        max_nodes = 2 ** height
        


    def has_right(self):
        if hasattr(self, 'right') and self.right is not None:
            return True
        else:
            return False
    
    def has_left(self):
        if hasattr(self, 'left') and self.left is not None:
            return True
        else:
            return False
    
    def __compute_height(self):
        # children = [self.has_left(), self.has_right()]
        # if any([self.has_left(), self.has_right()]):
        #     self.tree_height += 1
        #     if self.has_left():
        #         self.get_left().__compute_height()
        #     if self.has_right():
        #         self.get_right().get_height()
        level = 1
        child_found = True
        while child_found:
            if True in self.get_children():
                level += 1

    def get_children(self):
        children = [ method() for method in [self.get_left, self.get_right] if method() is not None ]




root = Bst(data=100)
root.create_right(data=50)
right = root.get_right()

#print(right)
root.create_left(data=25)
left = root.get_left()

left.create_left(data=21)
ll = left.get_left()

ll.create_left(data=22)
lll = ll.get_left()

lll.create_right(data=23)
lllr = lll.get_right()

#print(left)

print(root.get_height())
print(root)
