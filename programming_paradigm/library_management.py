# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title        # public
        self.author = author      # public
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' not available or already checked out.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book '{title}' not found or not checked out.")

    def list_available_books(self):
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books available.")
            return
        for book in available:
            print(f"{book.title} by {book.author}")
