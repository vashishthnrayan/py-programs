print("pyramid pattern of stars:")
n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for k in range(0, n-i+ 1):
        print(" ", end="", flush=True)  # Print leading spaces
    for j in range(1, 2 * i ):
        print("*", end="", flush=True)  # Print stars
    print()  # Move to the next line after each row