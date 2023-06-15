class Book:
    # Initialize a Book object with an ISBN, a title, and an author.
    def __init__(self, isbn, title, author):
        self.isbn = isbn  # The ISBN of the book. This is unique for each book.
        self.title = title  # The title of the book.
        self.author = author  # The author of the book.


class Library:
    # Initialize a Library object. The library starts with no books.
    def __init__(self):
        self.books = []  # A list of all the books in the library.

    # Add a book to the library.
    # If a book with the same ISBN is already in the library, raise a ValueError.
    def add_book(self, book):
        for b in self.books:
            if b.isbn == book.isbn:
                raise ValueError("A book with this ISBN already exists.")
        self.books.append(book)

    # Remove a book from the library.
    # If the book is not in the library, raise a ValueError.
    def remove_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                self.books.remove(b)
                return
        raise ValueError("Book not found.")

    # Check if a book is in the library.
    # Returns True if the book is in the library, and False otherwise.
    def has_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return True
        return False

    # Count the number of books in the library.
    # Returns the number of books in the library.
    def count_books(self):
        return len(self.books)
