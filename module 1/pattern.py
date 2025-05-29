print("Right Triangle Pattern  of Stars:")
n=int(input("Enter the number of rows: "))
for i in range(0,n+1):
    for j in range(0,i+1):
        print("*",end="" ,flush=True)
    print()  # Move to the next line after each row