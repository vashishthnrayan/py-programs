class shape:
    def __init__(self):
        print("inside base class")
    def area(self):
        print("inside base class")
class square(shape):
    def __init__(self, side):
        self.side = side
        print("inside derived class")
    def area(self):
        print("Area of square is:", self.side * self.side)




sq=square(10)
sq.area()