class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def print_x(self):
        print(self.x)

obj = B(1)
obj.print_x()
