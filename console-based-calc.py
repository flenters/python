import sys
#This is the main calculator class that has all the math operations
class Calc():
#Add function
    def add_numbers (x,y):
        sum = x+y
        return sum
#Subtract function
    def sub_numbers (x,y):
        sum = x-y
        return sum
#Multiply function
    def multiply_numbers (x,y):
        sum = x*y
        return sum
#Divide function    
    def divide_numbers (x,y):
        sum = x/y
        return sum          
#This is the simple interest calculator
class InterestCalc():
    def calc_interest (x,z,y):
        z = interest_rate / 100
        sum = x*z*y
        return sum
class CompInterestCalc():
    def calc_interest (amount,rate,time):
        result = amount * (pow((1 + rate / 100), time))
        return result       
#This is the currencies converter classes
class curRate():
    usd = 14.50
    gbp = 18.18
class convertZar():
    def zar(x):
        sum = x* float(0.067)
        return sum
#This is a small example of inheritnce getting currencies from curRate
class convertUsd(curRate):
    def usd(x):
        sum = x* float(curRate.usd)
        return sum
class convertGbp(curRate):
    def gbp(x):
        sum = x* float(curRate.gbp)
        return sum

#Most of the application is below in a while loop with nested if statements.
while True:
#Display the menu
    print("")
    print("######################################")
    print("##  1. Add                          ##")
    print("##  2. Subtract                     ##")
    print("##  3. Multiply                     ##")
    print("##  4. Divide                       ##")
    print("##  5. Calculate Simple Interest    ##")
    print("##  6. Calculate Compound Inerest   ##")
    print("##  7. Convert ZAR to USD           ##")
    print("##  8. Convert USD to ZAR           ##")
    print("##  9. Convert GBP to ZAR           ##")
    print("##  10. Exit                        ##")
    print("######################################")
    print("")
#User must input the choice
    choice = input("Enter 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 : ")  
    #Below is some error handling to check if the user enters a valid number 
    if choice ==  "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10":
        if choice == "1":
            num1 = int(input("Please type your 1st number "))
            num2 = int(input("Please type your 2nd number "))
            print("")
            print(num1,"+", num2, "=", Calc.add_numbers(num1,num2))
        elif choice == "2":
            num1 = int(input("Please type your 1st number "))
            num2 = int(input("Please type your 2nd number "))
            print("")
            print(num1,"-", num2, "=", Calc.sub_numbers(num1,num2))
        elif choice == "3":
            num1 = int(input("Please type your 1st number "))
            num2 = int(input("Please type your 2nd number "))
            print("")
            print(num1,"x", num2, "=", Calc.multiply_numbers(num1,num2))
        elif choice == "4":
            num1 = int(input("Please type your 1st number "))
            num2 = int(input("Please type your 2nd number "))
            print("")
            print(num1,"/", num2, "=", Calc.divide_numbers(num1,num2))
        elif choice == "5":
            principal_amount = int(input("Please enter loan amount "))
            number_years = int(input("How many years "))
            interest_rate = float(input("Enter you interest rate "))
            print("")
            print("Simple interest is:", InterestCalc.calc_interest(principal_amount,interest_rate,number_years))
        elif choice == "6":
            amount = float(input("Please enter loan amount "))
            time = float(input("How many years "))
            rate = float(input("Enter you interest rate "))
            print("")
            print("Compound interest is:", CompInterestCalc.calc_interest(amount,rate,time))
        elif choice == "7":
            zar_amount = int(input("Enter the amount in ZAR "))
            print("")
            print(zar_amount, "South African Rand equals", convertZar.zar(zar_amount), "United States Dollar")      
        elif choice == "8":
            usd_amount = int(input("Enter the amount in USD "))
            print("")
            print(usd_amount, "United States Dollar equals", convertUsd.usd(usd_amount), "South African Rand") 
        elif choice == "9":
            gbp_amount = int(input("Enter the amount in GBP "))
            print("")
            print(gbp_amount, "Pound sterling equals", convertGbp.gbp(gbp_amount), "South African Rands") 
        elif choice == "10":
            print("Good Bye")
            break
        else:
            print("You did not enter a valid number")
    else:
        print("Woops something serious has gone wrong")
