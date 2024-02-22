# Also check if the account number already exists
# Also can generate a transaction id
# inintial balance should be put in the transaction
# Security , logging in the account

# got to learn about composition that another class can use some other class without inheriting from that class.
import random

class BankAccount:
    def __init__(self,name,initial_balance):
        self.account_number = random.randint(100000,999999)
        self.name = name
        self.balance = initial_balance
        self.transactions = []


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



account = Bank()
acc1 = account.create_account("Richie1" ,123456)
acc2 = account.create_account("Richie1" ,123456)

account.view_all_accounts()
acc2.deposit(1234)
acc1.deposit(1234)
acc1.withdraw(1234)
acc1.check_balance()
acc1.display_transactions()
acc1.transfer(1234, acc2)

print(acc1.transactions)
print(acc2.transactions)
