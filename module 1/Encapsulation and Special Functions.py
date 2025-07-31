class Student:
    __schoolName = "ABC High School"

    def __init__(self, name, age):
        self.name = name

    print(__schoolName)
    
    def __display(self):
        print("this is a private method")

std = Student("John", 16)
