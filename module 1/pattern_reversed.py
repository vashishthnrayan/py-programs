print("Right Triangle Pattern  of Stars:")
n=int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end="" ,flush=True)
    print()  # Move to the next line after each rowd