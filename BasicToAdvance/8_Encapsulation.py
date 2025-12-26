class Bank:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number  # Private attribute
        self.__balance = initial_balance        # Private attribute

    #setter
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")
    #setter
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid withdrawal amount.")
    #getter
    def get_balance(self):
        return self.__balance
    #getter
    def get_account_number(self):
        return self.__account_number
    
# Example usage
account = Bank("123456789", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Account Number: {account.get_account_number()}")
print(f"Current Balance: ${account.get_balance():.2f}")
# Trying to access private attributes directly will raise an AttributeError
# print(account.__balance)      #AttributeError: 'Bank' object has no attribute '__balance'.


# Deposited: $500.00
# Withdrew: $200.00
# Account Number: 123456789
# Current Balance: $1300.00