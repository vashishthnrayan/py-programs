my_dict={'name':'John', 'age':30, 'city':'New York'}

my_dict['age'] = 31  # Update age

my_dict['gender']= "Male"

print("Dictionary -",my_dict)  

square = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print(square.pop(4))

print("Dictionary after pop -", square)

print(square.popitem())

print("Dictionary after popitem -", square)



square.clear()


print("Dictionary after clear -", square)

del square

print("Dictionary after del -", square)