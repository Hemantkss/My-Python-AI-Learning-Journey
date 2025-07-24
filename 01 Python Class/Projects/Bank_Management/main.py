import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []
    
    # Open database
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("Database not found")
    except Exception as err:
        print(f"Error occured in opening the database: {err}")
        
    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            fs.write(json.dumps(Bank.data))
            
    @classmethod
    def __accountGenerator(cls):
        alphabets = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        specialChar = random.choices("!@#$%&*^", k=1)
        id = alphabets + num + specialChar
        random.shuffle(id)
        return "".join(id)
            
        
    # Create a new account
    def CreateAccount(self):
        Info = {
            "Name": input("Enter your name: "),
            "Age": int(input("Enter your age: ")),
            "Email": input("Enter your email: "),
            "Pin": int(input("Enter your pin: ")),
            "AccountNumber": Bank.__accountGenerator(),
            "Balance": 0
        }
        
        if Info['Age'] < 18 or len(str(Info['Pin'])) != 4:
            print("You are not eligible to open an account")
        else:
            print("Account created successfully")
            for i in Info:
                print(f"{i}: {Info[i]}")
                
            print("Please remember your account number")
                
            Bank.data.append(Info)
            Bank.__update()
                
    # Deposit Money
    def DepositMoney(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        
        userData = [i for i in Bank.data if i['AccountNumber'] == accountNumber and i['Pin'] == pin]
        
        if userData == False:
            print("Invalid account number or pin")
        else:
            amount = int(input("Enter the amount: "))
            if amount > 10000 and amount < 0:
                 print("You can't deposit more than 10000 or less than or equal to 0")
            else:
                # print(userData)
                userData[0]["Balance"] += amount
                Bank.__update()
                print("Money deposited successfully")
                
    # Withdraw Money WithdrawMoney
    def WithdrawMoney(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        
        userData = [i for i in Bank.data if i['AccountNumber'] == accountNumber and i['Pin'] == pin]
        
        if userData == False:
            print("Invalid account number or pin")
        else:
            withdrawAmount = int(input("how Much do you want to withdraw: "))
            if userData[0]["Balance"] < withdrawAmount:
                print("Sorry you don't have enough balance")
            else:
                # print(userData)
                userData[0]["Balance"] -= withdrawAmount
                Bank.__update()
                print("Money Withdrawn successfully")
        
    # Show Details
    def ShowDetails(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        
        userData = [i for i in Bank.data if i['AccountNumber'] == accountNumber and i['Pin'] == pin]
        
        print("Account Details \n")
        for i in userData[0]:
            print(f"{i}: {userData[0][i]}")
            
    # Update Details
    def UpdateDetails(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        
        userData = [i for i in Bank.data if i['AccountNumber'] == accountNumber and i['Pin'] == pin]
        
        if userData == False:
            print("Invalid account number or pin")
        else:
            print("You cannot change your account number, age and balance")
            print("You can change your pin, name & email ")
            
            newData = {
                "Name": input("Enter your New Name or Enter to skip: "),
                "Email": input("Enter your New Email or Enter to skip: "),
                "Pin": int(input("Enter your New Pin or Enter to skip: "))
            }
            
            if newData['Name'] == "":
                newData['Name'] = userData[0]['Name']
            if newData['Email'] == "":
                newData['Email'] = userData[0]['Email']
            if newData['Pin'] == "":
                newData['Pin'] = userData[0]['Pin']
                
            newData["Age"] = userData[0]['Age']
            newData["AccountNumber"] = userData[0]['AccountNumber']
            newData["Balance"] = userData[0]['Balance']
            
            if type(newData['Pin']) == str:
                newData['Pin'] = int(newData['Pin'])
                
            for i in newData:
                if newData[i] == userData[0][i]:
                    continue
                else:
                    userData[0][i] = newData[i]
           
            Bank.__update()
            print("Details updated successfully")
            
    # Delete Account
    def DeleteAccount(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        
        userData = [i for i in Bank.data if i['AccountNumber'] == accountNumber and i['Pin'] == pin]
        
        if userData == False:
            print("Invalid account number or pin")
        else:
            check = input("Are you sure you want to delete your account? (N/Y): ")
            if check == "N" or check == "n":
                print("Account not deleted")
            else:
                index = Bank.data.index(userData[0])
                Bank.data.pop(index)
                Bank.__update()
                print("Account deleted successfully")   
              
        
        
# Create an object  
user = Bank()

print("Press 1 for Create a new account")
print("Press 2 for Deposit Money")
print("Press 3 for Withdraw Money")
print("Press 4 for details")
print("Press 5 for Update Details")
print("Press 6 for Delete Account")

check = int(input("Enter your choice: "))

# Create a new account
if check == 1:
    user.CreateAccount()
    
# Deposit Money
if check == 2:
    user.DepositMoney()
 
# Withdraw Money 
if check == 3:
    user.WithdrawMoney()
    
# Details
if check == 4:
    user.ShowDetails()
    
# Update Details
if check == 5:
    user.UpdateDetails()
    
# Delete Account
if check == 6:
    user.DeleteAccount()