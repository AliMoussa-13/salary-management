import os
import time
userName=input("Hello Enter your name :")
print("------------------------")
os.system('cls' if os.name == 'nt' else 'clear')
print(f"Welcome {userName} to the salary mangement program: ")
print("----------------------------------------------------")
monthName=input("Enter the name of the month you are storing the salary for:")
salaryOfMonth=int(input(f"Enter your salary for {monthName} :"))
print("Enter the following perctanges(%) for :")
saving=float(input("1)Savings :"))
rent=float(input("2)Rents:"))
electricity=float(input("3)Electricity:"))
   