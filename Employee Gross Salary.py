Basic_Salary = float(input("Enter Basic Salary :"))

DA = (Basic_Salary * 75)/ 100
HRA = (Basic_Salary * 20)/ 100
#Gross_Salary = Basic_Salary + DA + HRA

if Basic_Salary<10000:
    Gross_Salary=DA+Basic_Salary
    print ("Gross Salary :" , Gross_Salary)
elif Basic_Salary>=10000 and Basic_Salary<20000:
    Gross_Salary=DA+Basic_Salary+(HRA/2)
    print ("Gross Salary :" , Gross_Salary)
elif Basic_Salary>=20000:
    Gross_Salary=Basic_Salary+DA+HRA
    print ("Gross Salary :" , Gross_Salary)
else:
    print("Invalid Entry")
