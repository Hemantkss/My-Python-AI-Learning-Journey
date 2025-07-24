"""
   Exception Handling
"""
# print("hemant"

# a = 15
# if a == 12:
#     print("hello")
# else:
#     print("no")


# Exception

# print("Start")
# try:
#     print(10/5)
# except Exception as err:
#     print(f"You Can not divided by Zero, {err}")
# else:
#     print("Else")
# finally:
#     print("i will run no matter whats")

# raise
age = int(input("Enter Your Age: "))
try:
    if(age<10 or age > 18):
        raise ValueError("Your age between 10 to 18")
    else:
        print("Welcome to club") 
        
except Exception as err:
    print(f"an err Occur {err}")
    
print("hi")





