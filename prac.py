from datetime import date, timedelta

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.borrowed_by = None
        self.due_date = None

    def borrow(self, member):
        if not self.available:
            return False
        self.available = False
        self.borrowed_by = member
        self.due_date = date.today() + timedelta(days=14)
        return True

    def give_back(self):
        self.available = True
        self.borrowed_by = None
        self.due_date = None

    def display_info(self):
        status = "Available" if self.available else f"Borrowed by {self.borrowed_by}, due {self.due_date}"
        print(f"[{self.isbn}] {self.title} by {self.author} - {status}")


class Library:
    def __init__(self):
        self.books = []          # instance attribute, not shared

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def search(self, keyword):
        keyword = keyword.lower()
        return [b for b in self.books
                if keyword in b.title.lower() or keyword in b.author.lower()]

    def borrow_book(self, title, member):
        book = self.find_book(title)
        if book is None:
            print(f"Book '{title}' not found.")
            return False
        if not book.borrow(member):
            print(f"Sorry, '{book.title}' is currently not available.")
            return False
        print(f"{member} borrowed '{book.title}'. Due on {book.due_date}.")
        return True

    def return_book(self, title):
        book = self.find_book(title)
        if book is None:
            print(f"Book '{title}' not found.")
            return False
        if book.available:
            print(f"'{book.title}' was not borrowed.")
            return False
        book.give_back()
        print(f"'{book.title}' returned successfully.")
        return True

    def remove_book(self, title):
        book = self.find_book(title)
        if book:
            self.books.remove(book)
            return True
        return False

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            book.display_info()


lib = Library()
lib.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "101"))
lib.add_book(Book("Python 101", "Ram", "102"))

lib.display_books()
lib.borrow_book("python 101", "Dhanush")
lib.borrow_book("Python 101", "Arun")
lib.return_book("Python 101")
lib.return_book("Python 101")
print(lib.search("ram"))