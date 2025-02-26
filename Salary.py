import os
import time
monthNames=[]
salaryOfMonths=[]
savings=[]
renting=[]
electricity=[]
remainings=[]
def StringInputChecker(text):
    number=[0,1,2,3,4,5,6,7,8,9]
    check =False
    for i in range(len(text)):
        for j in range (len(number)):
            if(str(number[j])==text[i]):
             check=True
    return check
def calculateValue(percentage,salary):
    return salary*(percentage/100)

    
 
again=True
userName=input("Hello Enter your name :")
print("------------------------")
os.system('cls' if os.name == 'nt' else 'clear')
print(f"Welcome {userName} to the salary mangement program: ")
print("----------------------------------------------------")
main=True
while main:
    main=False
    while again:
        again=False
        monthName=input("Enter the name of the month you are storing the salary for:")
        if StringInputChecker(monthName):
            again=True
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You entered wrong monthName :(  ")
            print("Enter just the name of the month with any  numbers") 
        monthNames.append(monthName)
        if StringInputChecker(monthName):
            monthNames.pop()
    
    salaryOfMonth=int(input(f"Enter your salary for {monthName} :"))      

    check=True
    while check:
        check=False
    
        print("Enter the following perctanges (%) :")
        savingPer=float(input("1)Savings:"))
        rentPer=float(input("2)Rents:"))
        electricityPer=float(input("3)Electricity:"))
        if(savingPer+rentPer+electricityPer>100):
            check=True
            #os.system('cls' if os.name == 'nt' else 'clear')
            print("The sum of the inputs is greater than 100(%) :( ")
            print("please enter the percentages in correct way in which the sum of the three inputs must be less than 100(%) ")
        salaryOfMonths.append(salaryOfMonth)
        saving=calculateValue(savingPer,salaryOfMonth)
        savings.append(saving)
        rent=calculateValue(rentPer,salaryOfMonth)
        renting.append(rent)
        elec=calculateValue(electricityPer,salaryOfMonth)
        electricity.append(elec)
        remaining=salaryOfMonth-(saving+rent+elec)
        remainings.append(remaining)
        if(savingPer+rentPer+electricityPer>100):# this is step is done since at the end I noticed that even 
                                                # the numbers are wrong they are added to the list
             savings.pop()
             renting.pop()
             electricity.pop()
             remainings.pop()

    print("Do you need to eneter a new month? (yes/no):")
    answer=input()
    if answer=="yes"or answer=="Yes":
        main=True
        again=True
        check=True
    
perctnages={
    "savings":savings,
    "renting":renting,
    "electricity":electricity,
    "remaining":remainings
    }
user= {
    "userName":userName,
    "monthName":monthNames,
    "salary":salaryOfMonths,
    "bills":perctnages,
}
print(f"hello {user["userName"]} :")
print("================")
for i in range (len(monthNames)):
    print(
    f"The month:{user.get('monthName')[i]},salary:{user.get('salary')[i]},and it was divide for: "
    f"(saving):{user.get('bills').get('savings')[i]},"
    f"(renting):{user.get('bills').get('renting')[i]},"
    f"(electricity):{user.get('bills').get('electricity')[i]}"
    f"(remaining):{user.get('bills').get('remaining')[i]}"
)
yearlySaving=0.0
yearlyRenting=0.0
yearlyElectricity=0.0
print("Do you want to see the yearly values (yes/no) :")
choice=input()
if choice=="yes"or choice=="Yes":
    if len(monthNames)==12 :
        print("The yearly  values :")
        print("=====================")
        for i in range(len(monthNames)):
            yearlyRenting+=savings[i]
            yearlyRenting+=renting[i]
            yearlyElectricity+=electricity[i]
        print(
            f"The yearly saving value is :{yearlySaving}"
            f"The yearly renting value is {yearlyRenting}"
            f"The yearly Electricity value is {yearlyElectricity}"
          )
    else:
        print("The number of months is less than 12,so you can not calculate yearly values :( ")





