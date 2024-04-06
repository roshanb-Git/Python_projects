class Account:
    def __init__(self,account_number, balance=0):
        self.account_number =account_number
        self.balance =balance


    def deposit(self,amount):
        self.balance += amount
        #print(f'Amount deposited--------- \nAmount diposited : {amount} \nAccount Balance : {self.balance}')
        return self.balance
    
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            #print(f'Amount withdrawn------------- \nAmount withdrawn : {amount} \nAccount Balance : {self.balance}')
            return self.balance
        else:
            print(f'Insufficient balance************ \nAccount_balance :{self.balance}')
            


    def get_balance(self):
        print(f'Your Account balance : {self.balance}')

