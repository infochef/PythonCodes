"""
File: createClass.py
Author: Somnath
Date: 24/05/26
Description: Bank model to understand class, instance variable and instance method
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner # instance variable
        self.balance = balance # instance variable

    # instance method
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"{deposit_amount} is deposited in the bank account. Current balance is {self.balance}")

    def withdraw(self, withdrawn_amount):
        if withdrawn_amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= withdrawn_amount
            print(f"{withdrawn_amount} is withdrawn from the bank account. Current balance is {self.balance}")

    def get_balance(self):
        return print(f"{self.owner} current account balance is {self.balance}")

albert_account = BankAccount('Albert', 5000)
print(albert_account)
albert_account.deposit(100)
albert_account.withdraw(300)
albert_account.get_balance()