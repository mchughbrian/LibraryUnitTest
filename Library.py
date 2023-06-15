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

#use the count books, output should be 1
print(myLibrary.count_books())

#remove the book from myLibrary
myLibrary.remove_book('1234')

#check to make sure it was removed
print(myLibrary.count_books())

# Add the book to the library
myLibrary.add_book(myBook)

#try to remove a book that does not exist and handle the error appropriately
try:
    myLibrary.remove_book('4567')
except ValueError as e:
    print(e)