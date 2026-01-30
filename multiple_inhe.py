class student:
    def study(self):
       self.university="NUST"
       self.course = "BSCS"
class hospitalworker:
    def duty(self):
       self.ward= "Emergency"
       self.shift= "Morning"
#mulple inheritance:child class dono parents ka data combine krega
class medicalintern(student,hospitalworker):
    def __init__(self,name):
        self.name = name
#active both parents data
        student.study(self)
        hospitalworker.duty(self)
    def show(self):
        print(f"Name:{self.name}")
        print(f"Uni:{self.university} | Course:{self.course}")
        print(f"Duty Ward:{self.ward} | Shift:{self.shift}")
#objects
anushka= medicalintern("Anushka Sheikh")
anushka.show()