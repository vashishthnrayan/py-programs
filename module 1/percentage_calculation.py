print ("Enter Marks Obtained in 4 Subjects: ")
math = int( input ("maths :"))
english = int( input( "english :"))
science = int( input( "science :"))
hindi = int( input( "hindi :"))

# Let's calculate the percentage of marks
sum = math+english+science+hindi
print("sun of math, english, science and hindi")
perc = (sum/400 )*100
print(end="Percentage Mark = ")
print( perc,"%")


# sq_root
print("Square Root of a number: ")
number = int(input("Enter Number: "))
Sq_root = number ** 0.5
print ("Square root of", number, "is", Sq_root)