# even
num=[1,2,3,4,5,6,7,8,9,10]

even=[x for x in num if x%2==0]
print("list of even numbers:",even,"\n")
# odd

num2=[1,2,3,4,5,6,7,8,9,10]
odd=[x for x in num2 if x%2!=0]
print("list of odd numbers:",odd,"\n")



mydict = {str(x):x**2 for x in [1,2,3,4,5]}
print(mydict)