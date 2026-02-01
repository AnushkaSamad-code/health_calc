class Mother:
    def skill(self):
        print("Maa: Cooking and Management")

class Father:
    def skill(self):
        print("Baap: Business and Coding")

# Yahan order check karein: (Mother, Father)
class Child(Mother, Father):
    def my_skill(self):
        print("Child: Learning fast!")

# Test karna
anushka = Child()
anushka.skill() # Dekhein kiska function chalta hai?

# MRO Check karne ka tarika
print(Child.mro())