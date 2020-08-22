income = float(input("Enter the annual income: "))

if income <= 556.02:
    tax = 0.0
elif (income < 85_528):
    tax = (income * .18) - 556.02
else:
    tax = 14_839.02 + (income - 85_528) * .32  
    

tax = round(tax, 0)
print("The tax is:", tax, "thalers")