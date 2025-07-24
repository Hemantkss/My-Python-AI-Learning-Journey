"""
  Functions
"""
# def fullName():
#     a = input("Enter First Name: ")
#     b = input("Enter Last Name: ")
#     print(f"{a} {b}")
# fullName()

# # Parameters and Arguments
# def sum(a, b):
#     print(f"The sum of {a} and {b} is {a+b}")
    
# sum(2, 5)
# sum(12, 12)


# Types of Arguments

# 1 positional argument
# def sum(a, b):
#     print(f"The sum of {a} and {b} is {a+b}")
    
# sum(2, 5)
# sum(12, 12)

# 2 default argument
# def student(name= "Hemant"):
#     print(f"Hi, {name}")
# student()
# student("Rahul")

# 3 keyword argument
# def info(name, age):
#     print(f"Hi, {name} You are {age} years old")
    
# info("Hemant", 24)
# info(age = 25, name = "Rahul")


# Return statement
# def hello():
#     return "Hello World"
# print(hello())


# Quiz
# Q1. Check the string is palindrome or not
def isPalindrome(string):
    if(string == string[::-1]):
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")
        
isPalindrome("malayalam")
isPalindrome("hello")
isPalindrome("world")
isPalindrome("naman")