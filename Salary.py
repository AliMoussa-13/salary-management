import os
import time
def StringInputChecker(text):
    number=[0,1,2,3,4,5,6,7,8,9]
    check =False
    for i in range(len(text)):
        for j in range (len(number)):
            if(str(number[j])==text[i]):
             check=True
    return check
 
again=True
userName=input("Hello Enter your name :")
print("------------------------")
os.system('cls' if os.name == 'nt' else 'clear')
while again:
    again=False
    print(f"Welcome {userName} to the salary mangement program: ")
    print("----------------------------------------------------")
    monthName=input("Enter the name of the month you are storing the salary for:")
    if StringInputChecker(monthName):
        again=True
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You entered wrong monthName :(  ")
        print("Enter just the name of the month with any  numbers")
        continue
        
    salaryOfMonth=int(input(f"Enter your salary for {monthName} :"))
    print("Enter the following perctanges (%) :")
    saving=float(input("1)Savings :"))
    rent=float(input("2)Rents:"))
    electricity=float(input("3)Electricity:"))
    if(saving+rent+electricity>100):
        again=True
        os.system('cls' if os.name == 'nt' else 'clear')
        print("The sum of the inputs is greater than 100(%) :( ")
        print("please enter the percentages in correct way in which the sum of the three inputs must be less than 100(%) ")