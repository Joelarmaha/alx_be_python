class Book:
    def __init__(self, title, author):
        self.title = title                 # Public attribute
        self.author = author               # Public attribute
        self._is_checked_out = False       # Private attribute

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        status = "Available" if self.is_available() else "Checked out"
        return f'"{self.title}" by {self.author} — {status}'


class Library:
    def __init__(self):
        self._books = []   # Private list to store Book instances

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
            return True
        return False

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                return book.check_out()
        return None  # Book not found

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                return book.return_book()
        return None  # Book not found

    def list_available_books(self):
        return [book for book in self._books if book.is_available()]

    def list_all_books(self):
        return self._books

from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()