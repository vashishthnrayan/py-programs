try:
    age=int(input("Enter your age: "))
    if age < 18:
        raise ValueError
    else:
        print("the age is valid")

except ValueError:
    print("Invalid age. You must be at least 18 years old.")