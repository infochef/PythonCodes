"""
File: BankAccount.py
Author: Somnath
Date: 24/05/26
Description: Bank Account model using oops concept
"""


class BankAccount:
    def __init__(self, accountNumber, accountHolderName, balance):
        self.accountNumber = accountNumber
        self.accountHolderName = accountHolderName
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return False

        self.balance += amount
        print(f"{amount} deposited to {self.accountHolderName}. Balance: {self.balance}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
            return False

        if amount > self.balance:
            print("Insufficient Balance")
            return False

        self.balance -= amount
        print(f"{amount} withdrawn from {self.accountHolderName}. Balance: {self.balance}")
        return True

    def get_balance(self):
        print(f"{self.accountHolderName}'s balance: {self.balance}")


# ------------------ BANK SYSTEM ------------------

class BankSystem:
    def __init__(self):
        self.accounts = []

    # Add account
    def add_account(self, account):
        self.accounts.append(account)

    # Find account by account number
    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.accountNumber == account_number:
                return acc
        return None

    # Transfer money using account numbers
    def transfer(self, sender_acc_no, receiver_acc_no, amount):
        sender = self.find_account(sender_acc_no)
        receiver = self.find_account(receiver_acc_no)

        if not sender:
            print("Sender account not found")
            return

        if not receiver:
            print("Receiver account not found")
            return

        if sender == receiver:
            print("Cannot transfer to same account")
            return

        if sender.withdraw(amount):
            receiver.deposit(amount)
            print(f"{amount} transferred from {sender.accountHolderName} to {receiver.accountHolderName}")
        else:
            print("Transfer failed")


# ------------------ USAGE ------------------

# Create bank system
bank = BankSystem()

# Create accounts
acc1 = BankAccount(101, "Sam", 5000)
acc2 = BankAccount(102, "John", 3000)
acc3 = BankAccount(103, "Alice", 7000)

# Add accounts to system
bank.add_account(acc1)
bank.add_account(acc2)
bank.add_account(acc3)

# Operations
acc1.deposit(1000)
acc2.withdraw(500)

# Transfer using account numbers (realistic)
bank.transfer(101, 102, 2000)

# Check balances
acc1.get_balance()
acc2.get_balance()
acc3.get_balance()