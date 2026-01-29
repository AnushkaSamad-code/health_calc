class student:

    def __init__ (self, name, semester):
        self.name=name
        self.semester=semester

    def show_details(self):
            print(f"Student:{self.name},Semester: {self.semester}")

s1 = student("Annu" , 1)
s2 = student("laiba" , 2)
s1.show_details()
s2.show_details()