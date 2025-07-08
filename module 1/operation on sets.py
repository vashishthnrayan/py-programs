# my_set={1,2,2,3,3,4,5,5,5}
# print(my_set)  # Output: {1, 2, 3, 4, 5}

# my_set.add(6)
# print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
my_set = {1, 2, 3}
print(my_set)  # Output: {1, 2, 3}

my_set= {1.0,"hello", (1,2,3)}
print(my_set)  # Output: {1.0, 'hello', (1, 2, 3)}

my_set={1, 2, 3, 4, 3, 2}
print(my_set)  # Output: {1, 2, 3, 4}

my_set=set([1, 2, 3, 4, 5])
print(my_set,"\n")  # Output: {1, 2, 3, 4, 5}

num_set = set({0, 1, 2, 3, 4, 5})
print("Origanal  ginal set:", num_set)  # Output: {0, 1, 2, 3, 4, 5}
num_set.pop()
print("after removing the first element from the said set:")
print(num_set)  # Output: {1, 2, 3, 4, 5}   