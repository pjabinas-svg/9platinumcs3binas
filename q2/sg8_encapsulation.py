class BankAccount: 
    def __init__(self,  account_holder, account_number, balance=0): 
        self.__account_number = account_number # Private attribute for account number
        self.__account_holder = account_holder # Private attribute for account holder
        self.__balance = balance # Private attribute for balance
#Allows desposting money into the bank account and updates the balance to the correct amount. Making it sure the deposit amount is positive.

    def deposit(self, amount): 
        if amount > 0: 
            self.__balance += amount 
            print(f"Deposited {amount}. Your new balance is {self.__balance}.") 
        else: 
            print("Deposit amount should be positive.") 
    




# Allows withdrawing money from the bank acount and updates the bank account's balance to the correct amount. Making sure the withdraw amount is positive and less than or equal to the current balance.

    def withdraw(self, amount): 
        if 0 < amount <= self.__balance: 
            self.__balance -= amount 
            print(f"Withdrew {amount}. Your new balance is {self.__balance}.") 
        else: 
            print("Withdrawal amount must be positive and less than or equal to the current balance.") 

#get the current balance of the bank account.
    def get_balance(self): 
        print(f"Current balance is: {self.__balance}")
        return self.__balance 

    
#get the account information of the bank account including account number, account holder, and balance.
    def get_account_info(self): 
       print(f"Account Information: {self.__account_number}, {self.__account_holder}, {self.__balance}")

#-----------------Example Usage-----------------
account = BankAccount("Paul Jacob", "456789", 1000) # Account holder 
account.withdraw(1100) # Should print error
get_balance = account.get_balance() # Should print current balance
get_account_info = account.get_account_info() #should print account information
