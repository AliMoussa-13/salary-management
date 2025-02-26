import os
import time
monthNames=[]
salaryOfMonths=[]

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
    #    continue  
    monthNames.append(monthName)
    
salaryOfMonth=int(input(f"Enter your salary for {monthName} :"))      

check=True
while check:
    check=False
    
    print("Enter the following perctanges (%) :")
    savingPer=float(input("1)Savings :"))
    rentPer=float(input("2)Rents:"))
    electricityPer=float(input("3)Electricity:"))
    if(savingPer+rentPer+electricityPer>100):
        check=True
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("The sum of the inputs is greater than 100(%) :( ")
        print("please enter the percentages in correct way in which the sum of the three inputs must be less than 100(%) ")
    salaryOfMonths.append(salaryOfMonth)

answer=input("More?")

    
user ={
    "Name":userName,
    "MonthName":monthNames,
    "Salary":salaryOfMonths
}
     
#i must split the chechking conditions  and loop over the month name and salary to get more than once or put the input 
# savind and ect above at before the loop and put for it a specific loop
#check the dictionary methods


