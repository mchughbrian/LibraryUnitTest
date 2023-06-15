from main import Book, Library

#Create book object
myBook = Book(isbn='1234',title='Python 101',author='Bob Marley')
print(myBook.isbn,myBook.title,myBook.author)

# Create a Library object
myLibrary = Library()

# Add the book to the library
myLibrary.add_book(myBook)

# Check if the book was added
if myLibrary.has_book("1234"):
    print("The book was added to the library.")
else:
    print("The book was not found in the library.")

# Output: The book was added to the library.

print(myLibrary.count_books())
