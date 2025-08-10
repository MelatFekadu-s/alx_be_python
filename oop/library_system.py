class Book:
    def __init__(self, title, author):
        if not title or not author:
            raise ValueError("Title and author must be provided")
        self.title = title
        self.author = author

    def get_details(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        if not isinstance(file_size, int) or file_size <= 0:
            raise ValueError("File size must be a positive integer")
        self.file_size = file_size

    def get_details(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        if not isinstance(page_count, int) or page_count <= 0:
            raise ValueError("Page count must be a positive integer")
        self.page_count = page_count

    def get_details(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only instances of Book or its subclasses can be added")
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("Library is empty.")
        for book in self.books:
            print(book.get_details())