class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # 1. MAGIC METHOD: __str__ (String Representation)
    def __str__(self):
        return f"📖 Book: '{self.title}' written by {self.author}"

    # 2. MAGIC METHOD: __len__ (Length)
    def __len__(self):
        return self.pages

# Testing the Magic
my_book = Book("Harry Potter", "J.K. Rowling", 500)

# Normal tareeka (Magic Method ke baghair ye ganda lagta)
print(my_book)  
# Output: 📖 Book: 'Harry Potter' written by J.K. Rowling

# Length check karna
print(f"Total Pages: {len(my_book)}") 
# Output: Total Pages: 500