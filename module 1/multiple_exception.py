try:
    num1,num2=eval(input("Enter two numbers,sperated by comma: "))
    result = num1 / num2
    print("The result is:", result)

except ZeroDivisionError :
    print("Error: Division by zero is not allowed.")
except SyntaxError:
    print("Error: Invalid input syntax. Please enter two numbers separated by a comma.")

except :
    print("wrong input")
else:
    print("no exception")
finally:
    print("this will execute no matter what")
    