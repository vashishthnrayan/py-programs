class myClass:
    __privateVar=27

    def __privMath(self):
        print("I am inside my class")

    def hello(self):
        print("private variavle value:",myClass.__privateVar)
        self.__privMath()
foo = myClass()
foo.hello()
