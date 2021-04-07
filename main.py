#Band Name Genrator
print("Welcome to Band Name Genrator.")
city = input("Name of City where you grow.. \n")
pet_name = input("What's your first pet name? \n")
print("Congratulation ! You have a Band Name ",'"',city +" ",  pet_name,'"')

#BMI Calculator
w = int(input("Enter your w in kg"))
h = float(input("Enter your h in m"))
cal = int(w / (h**2))
print("Bmi is ",cal)

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
