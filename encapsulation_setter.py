class BankAccount:
    def __init__(self, name, money):
        self.name = name
        self.__balance = money # Locked Variable 🔒

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
my_acc.deposit(2000) # Ab balance 7000 ho jayega ✅
print("Total:", my_acc.get_balance())