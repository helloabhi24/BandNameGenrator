#Band Name Genrator
print("Welcome to Band Name Genrator.")
city = input("Name of City where you grow.. \n")
pet_name = input("What's your first pet name? \n")
print("Congratulation ! You have a Band Name ",'"',city +" ",  pet_name,'"')

#BMI Calculator
w = int(input("Enter your w in kg "))
h = float(input("Enter your h in m "))
cal = int(w / (h**2))

if cal<18.5:
    print(f"Your BMI is {cal},You are underweight.")
elif cal<25:
    print(f"Your BMI is {cal},You are normal weight.")
elif cal<30:
    print(f"Your BMI is {cal},You are over weight.")
elif cal<35:
    print(f"Your BMI is {cal},You are obese.")
else:
    print(f"Your BMI is {cal},You are cliniclly obese.")

#Age Calculator
age = int(input("Enter your age"))
remain_age = 90-age
months = 12*remain_age
weeks = 52*remain_age
days = 365*remain_age

print(f"You have {months} months, {weeks} weeks,{days} days remain to age of 90")

#Tip Calculator
print("Welcome to Tip Calculator!")
bill = float(input("Enter amount of Bill" ))
tip = int(input("Enter the amount of tip "))
people = int(input("Enter the amount of people who share the bill "))
tip_in_per = (100+tip)/100
cal= round((bill/people)*tip_in_per,2)
print(f"Each one give {cal} money")

#Even/Odd
print("Welcome to number checker!")
no = int(input("Give a number  "))

if no%2==0:
    print(f"{no} is a even no.")
else:
    print(f"{no} is a odd no.")
    
#Leap Year
print("Leap Year Calculator!")
year = int(input("Enter a year. "))

if year%4 ==0:
    if year%100!=0:
        print(f"{year} is a leap year")
    elif year%400==0:
            print(f"{year} is a Leap Year")
else:
    print("Not a leap year")

# Roller Costar Ride
print("Welcome to RollerCosterRide!")
height = int(input("Tell your height in cm "))
amount = 0
if height>120:
    print("Your welcome")
    age = int(input("What is your age? "))
    if age<12:
        amount = 5
        print("your ticket is 5 rupee")
    elif age<18:
        amount = 7
        print("your ticket is 7 rupee")
    elif age>=45 or age<=55:
        amount = 0
        print("you are Free Rider")
    else:
        amount = 12
        print("your ticket is 12 rupee")
    take_pic = input("You want to click a pic say Y or N ")
    if take_pic == 'Y' or take_pic == 'y':
        amount+=3
    print(f"your total bill is {amount}")
else:
    print("You are not invited!")


    
