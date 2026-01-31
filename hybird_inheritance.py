class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def __init__(self, name, hospital):
        # Yahan hum manual call kar rahe hain parents ko
        Person.__init__(self, name) 
        self.hospital = hospital

class Researcher(Person):
    def __init__(self, name, lab):
        Person.__init__(self, name)
        self.lab = lab

class MedicalScientist(Doctor, Researcher):
    def __init__(self, name, hospital, lab):
        # Sabse important step: Teeno levels ko connect karna
        Doctor.__init__(self, name, hospital)
        Researcher.__init__(self, name, lab)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Hospital: {self.hospital}")
        print(f"Research Lab: {self.lab}")

# Object creation
sc = MedicalScientist("Anushka", "JSMU", "Cardio Lab")
sc.display()