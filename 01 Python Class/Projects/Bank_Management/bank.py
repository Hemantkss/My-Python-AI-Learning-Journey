import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    @classmethod
    def load_data(cls):
        if Path(cls.database).exists():
            with open(cls.database) as fs:
                cls.data = json.load(fs)
        else:
            cls.data = []

    @classmethod
    def save_data(cls):
        with open(cls.database, "w") as fs:
            json.dump(cls.data, fs, indent=4)

    @staticmethod
    def generate_account_number():
        parts = random.choices(string.ascii_letters + string.digits, k=7)
        special = random.choice("!@#$%&*^")
        parts.append(special)
        random.shuffle(parts)
        return ''.join(parts)

    @classmethod
    def create_account(cls, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "You are not eligible to open an account"

        account = {
            "Name": name,
            "Age": age,
            "Email": email,
            "Pin": pin,
            "AccountNumber": cls.generate_account_number(),
            "Balance": 0
        }
        cls.data.append(account)
        cls.save_data()
        return True, account

    @classmethod
    def find_user(cls, acc_no, pin):
        return next((user for user in cls.data if user["AccountNumber"] == acc_no and user["Pin"] == pin), None)

    @classmethod
    def deposit(cls, acc_no, pin, amount):
        user = cls.find_user(acc_no, pin)
        if not user:
            return False, "Invalid credentials"
        if amount <= 0 or amount > 10000:
            return False, "Amount must be between 1 and 10,000"
        user["Balance"] += amount
        cls.save_data()
        return True, f"Deposited {amount} successfully."

    @classmethod
    def withdraw(cls, acc_no, pin, amount):
        user = cls.find_user(acc_no, pin)
        if not user:
            return False, "Invalid credentials"
        if amount > user["Balance"]:
            return False, "Insufficient balance"
        user["Balance"] -= amount
        cls.save_data()
        return True, f"Withdrew {amount} successfully."

    @classmethod
    def get_details(cls, acc_no, pin):
        user = cls.find_user(acc_no, pin)
        if not user:
            return False, "Invalid credentials"
        return True, user

    @classmethod
    def update_details(cls, acc_no, pin, name=None, email=None, new_pin=None):
        user = cls.find_user(acc_no, pin)
        if not user:
            return False, "Invalid credentials"
        if name:
            user["Name"] = name
        if email:
            user["Email"] = email
        if new_pin:
            user["Pin"] = new_pin
        cls.save_data()
        return True, "Details updated."

    @classmethod
    def delete_account(cls, acc_no, pin):
        user = cls.find_user(acc_no, pin)
        if not user:
            return False, "Invalid credentials"
        cls.data.remove(user)
        cls.save_data()
        return True, "Account deleted."
