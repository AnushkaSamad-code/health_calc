class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
#patient class person se traits lerhi h
class patient(person): #patient ab person ka sara data use krrha h
    def __init__(self,name,age,disease): #__init__ (constructor)banate h tw parent class ko __init__ owerwrite (mita) deta h isse bachne k liye ham super().__init__ likhte h tak 
        #tak purana data set hojye or ham new data set kre "disease"..
        super().__init__(name,age)
        self.disease=disease
    def check(self):
        print(f"Patient Name:{self.name} | Age:{self.age} | Disease: {self.disease}")

p1= patient("Anushka", 19, "coding fever")
p2= patient("Laiba", 23, "study headche")
p3= patient("hoor", 11, "laughing fever")
p1.check()
p2.check()
p3.check()
