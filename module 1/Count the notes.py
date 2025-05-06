amount=int(input("Enter the amount for withdraw: "))


note1=amount//500
amount%=500
note2=amount//200
amount%=200
note3=amount//100
amount%=100
note4=amount//50
amount%=50
note5=amount//20
amount%=20
note6=amount//10
amount%=10
note7=amount//5
amount%=5

print("Number of 500 notes:", note1)
print("Number of 200 notes:", note2)
print("Number of 100 notes:", note3)
print("Number of 50 notes:", note4)
print("Number of 20 notes:", note5)
print("Number of 10 notes:", note6)
print("Number of 5 notes:", note7)
# print("Number of 1 notes:", amount)
print("remaning amount:(if any): ₹", amount)