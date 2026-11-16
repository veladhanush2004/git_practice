class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    def borrow(self):
        if self.available:
            self.available = False
            return True
        else:  
            return False
    def display_info(self):
        availability = "Available" if self.available else "Not Available"
        print(f"Title: {self.title}, Author: {self.author}, Status: {availability}")

class Library:
    books = []
    def add_book(self, book):
        self.books.append(book)
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.borrow():
                    print(f"You have successfully borrowed '{book.title}'.")
                    return True
                else:
                    print(f"Sorry, '{book.title}' is currently not available.")
                    return False
        print(f"Book '{title}' not found.")     
        return None
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    print(f"You have successfully returned '{book.title}'.")
                    return True
        print(f"Book '{title}' not found or already available.")
        return False
    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            book.display_info()
            
b1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
b2 = Book("Python 101", "Ram")
lib = Library()
lib.add_book(b1)
lib.add_book(b2)
print("Available Books:")
lib.display_books()
lib.borrow_book("Python 101")
lib.borrow_book("Python 101")
lib.return_book("Python 101")
lib.return_book("Python 101")
lib.display_books()