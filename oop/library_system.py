class Book:
    def __int__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, file_size):
        self.file_size = file_size

    def __int__(self):
        return self.file_size


class PrintBook(Book):
    def __init__(self, page_count):
        self.page_count = page_count

    def __int__(self):
        return self.page_count


books = (Book, Ebook, PrintBook)


class Library(Book, EBook, PrintBook):
    def __init__(self, add_book, list_books):
        self.add_book = add_book
        self.list_books = list_books

    def add_book(self, book):
        book = Book + EBook + PrintBook
        return book
    def list_books(self):
        return books

