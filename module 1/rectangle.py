class shape:
    def __init__(self):
        print("inside base class")
    def area(self):
        print("inside base class")
class rectangle(shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        print("inside derived class")
    def area(self):
        print("Area of rectangle is:", self.length * self.breadth)

rect=rectangle(10, 52445)
rect.area()