class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return"({0},{1})".format(self.x, self.y )
    
    def __add__(self, other):
        x= self.x + other.x
        y= self.y + other.y
        return Point(x, y)
    
p1 = Point(1,2)
p2 = Point(2,3)

print(p1+p2)

class A:
    def __init__(self, a):
        self.a = a
    def __lt__ (self, other):
        if (self.a < other.a):
            return "ob1 is less than ob2"
        else :
            return "ob1 is greater than ob2"
    def __eq__(self,other):
        if (self.a == other.a):
            return "both objects are equal"
        else:
            return "not equal"

ob1 = A(2)
ob2 = A(3)
print("passed Value:"   , ob1.a,  ob2.a )
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print("passed Value:", ob3.a,  ob4.a)
print(ob3 == ob4)