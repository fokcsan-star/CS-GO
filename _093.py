class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount}. New balance: {self.__balance}")
            else:
                print(f"Error: Insufficient funds. Balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount")
    
    def get_balance(self):
        return self.__balance



account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)
print(f"Final balance: {account.get_balance()}")