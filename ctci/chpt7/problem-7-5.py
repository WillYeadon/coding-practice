# Online book reader data structures

class onlineLibrary():
    def __init__(self):
        self.books = []
    
    def addBook(self, book):
        self.books.append(book)

    def printTitles(self):
        for i in self.books:
            print(i.title, 'by', i.author)
    
class book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

books = [
        ('To Kill a Mockingbird', 'Harper Lee', 1960),
        ('The Great Gatsby', 'F. Scott Fitzgerald', 1925),
        ('One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 1967),
        ('The Lord of the Rings', 'J.R.R. Tolkien', 1954),
        ('The Catcher in the Rye', 'J.D. Salinger', 1951),
        ('The Alchemist', 'Paulo Coelho', 1988),
        ('The Little Prince', 'Antoine de Saint-Exupéry', 1943),
        ('Pride and Prejudice', 'Jane Austen', 1813),
        ('The Hitchhiker\'s Guide to the Galaxy', 'Douglas Adams', 1979),
        ('Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 1997)
        ]

library = onlineLibrary()

for i in books:
    #print(i[0], i[1], i[2])
    library.addBook(book(i[0], i[1], i[2]))

library.printTitles()