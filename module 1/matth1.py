import math
print("welcome to math toolkit\n")

num_1= float(input("Enter first number: "))
print(f"the square root of {num_1} is {math.sqrt(num_1)}")

# power
base =2
exp=5
print(f"{base} raised to the power of {exp} is {math.pow(base, exp)}")

# trigonometry
angle_deg = float(input("Enter an angle in degrees: "))
angle_rad = math.radians(angle_deg)
print(f"Sine of {angle_deg} degrees is {math.sin(angle_rad)}")

# rounding functions
num_2 = float(input("Enter a number to round: "))
print(f"floor of {num_2} is {math.floor(num_2)}")
print   (f"ceil of {num_2} is {math.ceil(num_2)}")

# constant
print(f"The value of pi is {math.pi}")

# pie and e constants
print(f"constant")
print(f"pi (π) = {math.pi}")
print(f"e (Euler's number) = {math.e}")

# logratamic functions
print(f"logarithm ")
print(f"log base 10 of  is {math.log(10)}")
print   (f"log base e of  is {math.log10(1000)}")
print(f"log base 2 of  is {math.log2(8)}")

# factorial
num_3 = int(input("Enter a number to calculate its factorial: "))
print(f"Factorial of {num_3} is {math.factorial(num_3)}")

# GCD
num_a = int(input("Enter first number for GCD: "))
num_b = int(input("Enter second number for GCD: "))

print(f"GCD of {num_a} and {num_b} is {math.gcd(num_a, num_b)}")