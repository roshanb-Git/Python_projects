from bank_sys.customer import Customer 
from bank_sys.account import Account

def main():

    #create Account
    acct1 = Account(12345, 0) 

    #Create Customer
    customer1 =Customer("Alex",acct1)

    
    #print initial balance
    print(f'Initial Balance : {acct1.balance}')

    #Deposit money
    amount_deposit = customer1.get_account().deposit(5000)
    #print updated balance
    print(f'Amount of deposit:{amount_deposit} \nYour account balance : {acct1.balance}')

    #withdraw money
    amount_withdraw = customer1.get_account().withdraw(12500)
    #print updated balance
    print(f'Amount of withdraw {amount_withdraw} \nYour account balance : {acct1.balance}')

 
if __name__ == "__main__":
    main()