class Person:
    def __init__(self, name):
        self.name = name

class MedicalStaff(Person):
    def __init__(self, name, hospital):
        super().__init__(name) # Grandparent se name liya
        self.hospital = hospital

class Doctor(MedicalStaff):
    def __init__(self, name, hospital, specialty):
        super().__init__(name, hospital) # Parent se name aur hospital liya
        self.specialty = specialty

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Hospital: {self.hospital}")
        print(f"Specialty: {self.specialty}")

# Object banana
doc = Doctor("Anushka", "Cardio Clinic", "cardiologist")
doc.show_info()