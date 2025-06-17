valid = False
while not valid: #using nested while loop
    try:
        n = int(input("Enter a number: "))
        while n%2==0:
            print("bye-bye")
            valid = True
    except ValueError:
        print("Please enter a valid integer.") 