units=int(input("Enter the number of units you used: "))

if(units>=0 and units <= 50):
    amount = units * 0.50
elif(units <= 150):
    amount = units * 0.75
elif(units <= 250):
    amount = units * 1.25
else:
    amount = units * 1.50

surcharge = amount * 17/100
ebill = amount + surcharge

print("Electricity Bill = Rs.",ebill)
