class BankAccount:
    def __init__(self, name, money):
        self.name = name
        self.__balance = money # Locked Variable 

    # 1. Getter (Dekhne ke liye - Kal kiya tha)
    def get_balance(self):
        return self.__balance

    # 2. Setter (Paise dalne ke liye - Aaj ka naya kaam)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Success! {amount} rupees added.")
        else:
            print("Error: Negative value not allowed!")

# Bas chota sa test
my_acc = BankAccount("Anushka", 5000)
my_acc.deposit(2000) # Ab balance 7000 ho jayega 
print("Total:", my_acc.get_balance())




# for withdrow
class BankAccount:
    def __init__(self, name, money):
        self.name = name
        self.__balance = money

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Error: Negative value!")

    # NAYA KAAM: Withdraw Method (Paise nikalna)
    def withdraw(self, amount):
        if 0 < amount <= self.__balance: # Check: Paise hain bhi ya nahi?
            self.__balance -= amount
            print(f"Success! Withdrew {amount} rupees.")
        else:
            print("Error: Insufficient balance or invalid amount!")

# Testing
acc = BankAccount("Anushka", 7000)
acc.withdraw(3000) # Chalna chahiye (Balance 4000 bachega) 
acc.withdraw(10000) # Error aana chahiye (Paise kam hain) 
print("Final Balance:", acc.get_balance())