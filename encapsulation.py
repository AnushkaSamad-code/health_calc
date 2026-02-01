class BankAccount:
    def __init__(self, name, money):
        self.name = name       # Public (Sab dekh sakte hain)
        self.__balance = money # Private (Koi nahi dekh sakta) 🔒

    # Ye hai "Chaabi" (Getter Method)
    def show_balance(self):
        return f"User {self.name} has {self.__balance} rupees."

acc = BankAccount("Anushka", 5000)

# ❌ GALAT RASTA (Direct) -> Ye Error dega (Matlab Encapsulation chal rahi hai!)
# print(acc.__balance) 

# ✅ SAHI RASTA (Method ke zariye) -> Ye chal jayega!
print(acc.show_balance())