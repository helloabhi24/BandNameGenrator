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

