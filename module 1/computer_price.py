class myClass:
    __privateVar=27;

    def __pricMath(self):
        print("I am inside my class")

    def hello(self):
        print("private variavle value:",myClass.__privateVar)
    __pricMath()
foo = myClass()
foo.hello()
