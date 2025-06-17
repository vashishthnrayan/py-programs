total_bill = float(input("Enter the total bill amount: "))

amount_paid = float(input("Enter the amount paid: "))

due_amount = total_bill - amount_paid

if due_amount > 0:
    print("The due amount is: ","₹",due_amount)
elif due_amount == 0:
    print("The bill is fully paid. No due amount.")
else:
    print("The amount paid exceeds the total bill. No due amount.")
