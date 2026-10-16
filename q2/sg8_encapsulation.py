class BankAccount: # Defines/creates a class called Bank account
    def __init__(self,  account_holder, account_number, balance=0): # creates a constructor method for the class Bank account that has 3 parameters/attributes
        self.__account_number = account_number # stores a piravte parameter/attribute for the account number because of the 2 underscores
        self.__account_holder = account_holder # Stores a private parameter/attribute for the account holder because of the 2 undescores
        self.__balance = balance # Stores a private parameter/attribute for the balance because of the 2 underscores
#Allows desposting money into the bank account and updates the balance to the correct amount. Making it sure the deposit amount is positive.

    def deposit(self, amount):  #Defines a method that is called "deposit" that has a parameter called amount. this method allows depositing money to update the balance
        if amount > 0: # makes it sure to check if the ammount is not 0 or negative
            self.__balance += amount  # adds the deposit amount to the current balance
            print(f"Deposited {amount}. Your new balance is {self.__balance}.") # prints or displays the new balance after the deposit 
        else: # if the deposit is 0 or negative, "if" statement will not be excuted and the "else" statement will be executed 
            print("Deposit amount should be positive.")  # if "else" is executed, it will display "Deposit amount should be positive."
    




# Allows withdrawing money from the bank acount and updates the bank account's balance to the correct amount. Making sure the withdraw amount is positive and less than or equal to the current balance.

    def withdraw(self, amount):  # defines a method called withdraw and has a parameter called ammount
        if 0 < amount <= self.__balance:  # makes sure to check if the withdraw amount is positive and lessthan or equal to the current balance.
            self.__balance -= amount  # this allows the withdraw amount to subract from the current balance and update and get a new balance
            print(f"Withdrew {amount}. Your new balance is {self.__balance}.")  # prints or displays new balance after the action
        else:  # when the "if" statement is not satisfied, else statement will be executed and will display the following message
            print("Withdrawal amount must be positive and less than or equal to the current balance.")  # when the else statement is executed it will print "Withdrawal amount must be positive and less than or equal to the current balance."

#get the current balance of the bank account.
    def get_balance(self):  # this defines a method called get_balance that will return the current balance of the bank account
        print(f"Current balance is: {self.__balance}") # prints the current balance of the bank account
        return self.__balance  # allows the method to return the current balance when it is executed

    
#get the account information of the bank account including account number, account holder, and balance.
    def get_account_info(self):  # defines a method get_account_info this will return the account info of the bank account with the ff acount number, account holder, and balance
       print(f"Account Information: {self.__account_number}, {self.__account_holder}, {self.__balance}") #prints the account info of the bank account.

#-----------------Example Usage-----------------
account = BankAccount("Paul Jacob", "456789", 1000) # Account holder 
account.withdraw(1100) # Should print error
get_balance = account.get_balance() # Should print current balance
get_account_info = account.get_account_info() #should print account information
















































































#RENEE BATERBONIA MAMAMMAMAMAMMAMAMAMA