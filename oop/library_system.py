class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title and self.author


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __int__(self):
        return self.file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __int__(self):
        return self.page_count


class Library():
    books = [Book, EBook, PrintBook]

    def __init__(self, add_book, list_books):
        self.add_book = add_book
        self.list_books = list_books

    def add_book(self, books):
        self.books = books
        self.books = [], "append"
        return book

    def list_books(self):
        return f' {self.title} by {self.author}, {self.page_count}'
