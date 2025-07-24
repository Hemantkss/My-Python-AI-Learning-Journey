"""
    Loops
"""

# 1 For loop

# for i in range(1, 21, 1):
#     print(i)

# for i in range(20, 51):
#     print(i)

# for i in range(16, 0, -1):
#     print(i)

# for i in range(-5, -16, -1):
#     print(i)

# Print a table 
# table = int(input("Enter Table Number: "))
# for i in range(table, (table*10)+1, table):
#     print(i)


# Loops for Strings

# a = "HEMANT SABALE"
# for i in range(len(a)):
#     print(a[i])

# a = "HEMANT"
# for i in a:
#     print(i)


# Break continue else
# for i in range(1, 11):
#     if(i == 6):
#         print("Break")
#         break
#     print(i)
# else:
#     print("Else")
        
# Quiz
# Q1. Accept an integer and Print hello world n times.
# n = int(input("Enter Number: "))
# for i in range(n):
#     print("Hello World")

# Q2. Print natural number up to n 
# n = int(input("Enter Number: "))
# for i in range(1, n+1):
#     print(i)

# Q3.  Reverse for loop. Print n to 1 
# n = int(input("Enter Number: "))
# for i in range(n, 0, -1):
#     print(i)

# Q4. Take a number as input and print its table 
# table = int(input("Enter Table Number: "))
# for i in range(table, (table*10)+1, table):
#     print(i)

# Q5. Sum up to n terms
# n = int(input("Enter Number: "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
#     print(f"Sum of {n} is {sum}")

# Q6.  Factorial of a number
# n = int(input("Enter Number: ")) 
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(i, factorial)
    
# Q7. Print the sum of all even & odd numbers in a range separately 
# n = int(input("Enter Number: ")) 
# even = 0
# odd = 0
# for i in range(1, n+1):
#     if(i % 2 == 0):
#         even += i
#     else:
#         odd += i
#     print(i, even, odd)


# Q8. Print all the factors of a number 
# n = int(input("Enter Number: ")) 
# for i in range(1, n+1):
#     if(n % i == 0):
#         print(i)

# Q9. Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself 
# n = int(input("Enter Number: ")) 
# sum = 0
# for i in range(1, n):
#     if(n % i == 0):
#         sum += i
# if(sum == n):
#     print(f"{n} is a perfect number")
# else:
#     print(f"{n} is not a perfect number")

# Q10. Check wether the number is prime or not 
# n = int(input("Enter Number: ")) 
# count = 0
# for i in range(1, n+1):
#     if(n % i == 0):
#         count += 1
# if(count == 2):
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")

# Q11. Reverse a string without using in build functions.
# a = "HEMANT"
# b = ""
# for i in range(len(a)-1, -1, -1):
#     b += a[i]
# print(b)

# Q12. Check string is Pallindrome or not 
# a = input("Enter String: ")
# b = ""
# for i in range(len(a)-1, -1, -1):
#     b += a[i]
# if(a == b):
#     print("Pallindrome")
# else:
#     print("Not Pallindrome")

# Q13. Count all letters, digits, and special symbols from a given string
# str = "P@#yn26at^&i5veHemant1580@#"
# count1 = 0
# count2 = 0
# count3 = 0
# for i in str:
#     if(i.isalpha()):
#         count1 += 1
#     elif(i.isdigit()):
#         count2 += 1
#     else:
#         count3 += 1
# print(f"Letters: {count1}")
# print(f"Digits: {count2}")
# print(f"Special Symbols: {count3}")




# 2  While loop
# a = 1
# while(a <= 10):
#     print(a)
#     a += 1

# Quiz
# Q1. Separate each digit of a number and print it on the new line
# n = int(input("Enter Number: "))
# while(n > 0):
#     print(n % 10)
#     n //= 10

# Q2. Accept a number and print its reverse
# n = int(input("Enter Number: "))
# reverse = 0
# while(n > 0):
#     reverse = (reverse * 10) + (n % 10)
#     n //= 10
# print(reverse)


# Q3. Accept a number and check if it is a pallindromic number (If number and its reverse are equal)
# n = int(input("Enter Number: "))
# copy = n
# reverse = 0
# while(n > 0):
#     reverse = (reverse * 10) + (n % 10)
#     n //= 10
# if(copy == reverse):
#     print(f"{copy} is a pallindromic number")
# else:
#     print(f"{copy} is not a pallindromic number")

# Q4. Create a random number guessing game with python.
import random
num = random.randint(1, 5)
tries = 0

while(True):
    guess = int(input("Enter your guess: "))
    if(num == guess):
        tries += 1
        print(f"You won in {tries} tries")
        break
    elif(num < guess):
        print("Too high")
        tries += 1
    elif(num > guess):
        print("Too low")
        tries += 1
    else:
        tries += 1
        print("You lost")


