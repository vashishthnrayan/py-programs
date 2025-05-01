name="penguin"
age=15
is_student=True
weight=38.5

# printing different types of variables and their types
print("Name:", name)
print, ("Data type of name is", type(name))

print("Age:", age)
print("Data type of age is", type(age))

print("Is student:", is_student)
print("Data type of is_student is", type(is_student))

print("Weight:", weight)
print("Data type of weight is", type(weight))

# type casting to convert the data types of  variables
print("\n After Type casting")

age=str(age)
print("Age:", age)
print("Data type of age is", type(age))
weight=int(weight)
print("Weight:", weight)
print("Data type of weight is", type(weight))