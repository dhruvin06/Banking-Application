# Also check if the account number already exists
# Also can generate a transaction id
# inintial balance should be put in the transaction
# Security , logging in the account
# Gui
#bank login vs user login

# got to learn about composition that another class can use some other class without inheriting from that class.
import random

class BankAccount:
    def __init__(self,name,initial_balance):
        self.account_number = random.randint(100000,999999)
        self.name = name
        self.balance = initial_balance
        self.transactions = [f'Initial amount of Rs {self.balance} has been deposited']


    def deposit(self,amount):
        self.balance += amount
        self.transactions.append(f'Rs {amount} has been deposited to the account')

    def withdraw(self,amount):
        if (amount < self.balance):
            self.balance -= amount
            self.transactions.append(f'Rs {amount} has been withdrawn from the account')
        else:
            print('Insufficient Balance, Available Balance: {amount}')

    def transfer(self,amount,target_account):
        if (amount < self.balance):
            self.balance -= amount
            self.transactions.append(f'Rs {amount} has been transferred to {target_account.account_number}')
            target_account.balance += amount
            target_account.transactions.append(f'Rs {amount} has been transferred from account {self.account_number}')
        else:
            print('Insufficient Balance, Available Balance: {amount}')

    
    def check_balance(self):
        print(f'Your account balance is {self.balance}')

    def display_transactions(self):
        for transaction in self.transactions:
            print(transaction)

    def close_account(self):
        print(f'Account closed')
        self.balance = 0
        self. transactions =  []

     
class Bank:
    def __init__(self):
        self.accounts = []
    
    def create_account(self, name, initial_balance):
        account = BankAccount(name, initial_balance)
        self.accounts.append(account)
        return account

    def get_account(self, account_number):
        for accounts in self.accounts:
            if accounts.account_number == account_number:
                return accounts
        return None
        
    def view_all_accounts(self):
        for accounts in self.accounts:
            print(f'{accounts.account_number} , {accounts.name}')

     

answer = "y"
bank = Bank()
user_accounts = []

while answer == "y":
    print(f'''    1.Create Account
    2.Deposit
    3.Withdraw
    4.Transfer    
    5.Check Balance
    6.Display Transactions''')    

    user_input = int(input("Enter the number from the given options:"))


    if(user_input == 1):
        
        name = input("Enter the name of the account holder : ")
        initial_balance = int(input("Enter the intial balance : "))
        new_acc = bank.create_account(name, initial_balance)
        # user account gets appended to the list as object and then we access all the different acccounts even if created by one user

        user_accounts.append(new_acc)
        print(f'Account created with acccount number : {new_acc.account_number}')

    else:
        account_number = int(input("Enter the account number : "))
        # here we retrieve the account object
        current_account = bank.get_account(account_number)
    
        if(user_input == 2):
            amount =  int(input("Enter the amount to deposit : "))
            current_account.deposit(amount)
        
        if(user_input == 3):
            amount =  int(input("Enter the amount to withdraw : "))
            current_account.withdraw(amount) 

        if(user_input == 4):
            target_number = int(input("Enter the target account number : "))
            target_account = bank.get_account(target_number)
            amount = int(input("Enter the amount to transfer"))
            current_account.transfer(amount, target_account)
    
        if(user_input == 5):
            current_account.check_balance()

        if(user_input == 6):
            current_account.display_transactions()
    
    
    

    answer = input("Do you want to continue y/n : ")







