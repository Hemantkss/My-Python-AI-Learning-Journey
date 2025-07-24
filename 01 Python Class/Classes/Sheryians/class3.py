"""
    Conditional statements 
"""
# 1 if 
# a = 20
# if(a > 10):
#     print("Greater than 10")

# 2 if else
# color = "red"
# if(color == "red"):
#     print("Color is red")
# else:
#     print("Color is not red")

# 3 if elif else
# latter = "B"
# if(latter == "A"):
#     print("Latter will be A")
# elif(latter == "B"):
#     print("Latter will be B")
# else:
#     print("not a Latter")
    
# Quiz
# Q1. Accept two numbers and print the greatest between them.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if(num1 > num2):
#     print(f"{num1} is greater than {num2}")
# else:
#     print(f"{num2} is greater than {num1}")
    
    
# Q2. Accept To gender from the user as char and print the respective greeting message Ex - Good Morning Sir (on the basis of gender)
# gender = (input("Enter Your Gender as Char(M-F)"))
# if(gender == "M" or gender == "m"):
#     print("Good Morning Sir, Hemant")
# elif(gender == "F" or gender == "f"):
#     print("Good Morning Madam, Neha")
# else:
#     print("Input invalid!")


# Q3. Accept an integer and check whether it is an even number or odd.
# num = int(input("Enter Your Number"))
# if(num % 2 == 0):
#     print("You Enter Even Number")
# else:
#    print("You Enter Odd Number")

# Q4. Accept name and age from the user. Check if the user is a valid voter 
# name = input("Enter Your Name")
# age = int(input("Enter Your Age"))
# if(age >= 18):
#     print(f"Hi, {name} You are Valid Voter age is {age}")
# else:
#     print(f"Hi, {name} You are not Valid Voter age is {age}")
    
# Q5. Accept a year and check if it a leap year or not 
# year = int(input("Enter The Year"))
# if(year % 100 == 0 or year % 400 == 0):
#     print(f"This is leap Year, {year}")
# elif(year % 100 != 0 and year % 4 == 0):
#     print(f"This is leap Year, {year}")
# else:
#     print("This is normal year")


# If- elif ladder
temp = int(input("Enter Your City Temprature"))
if(temp < 0):
    print("Freezing Cold")
elif(temp >= 0 and temp < 10):
    print("Very Cold")
elif(temp >= 10 and temp < 20):
    print("Cold")
elif(temp >= 20 and temp < 30):
    print("Pleasant")
elif(temp >= 30 and temp < 40):
    print("Hot")
else:
    print("Boiling Hot")