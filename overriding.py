class Parent:
    def hobby(self):
        print("Parent's Hobby: Reading")

class Anushka(Parent):
    def hobby(self):
        print("Anushka's Hobby: Coding in Python!") # Overriding!

# Test
me = Anushka()
me.hobby() # Output Parent wala nahi, Anushka wala aayega!