class car :
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def display(self):
        print("Car Name:", self.name, "Color:", self.color)

car1= car("Toyota", "Red")
car1.display()
car2=car("BMW", "Blue")
car2.display()