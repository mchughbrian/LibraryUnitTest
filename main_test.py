import unittest
from main import Library, Book  # replace with your actual module name


class TestLibrary(unittest.TestCase):

    def setUp(self):
        """ Create a Library object and a Book object for use in test cases """
        self.library = Library()
        self.book = Book("978-3-16-148410-0", "A Great Book", "John Doe")

    def test_add_book(self):
        """ Test that a book can be added to the library """
        # Initially, the library is empty
        self.assertEqual(self.library.count_books(), 0, "Library should be empty initially.")

        # Add a book and confirm count_books() increases
        self.library.add_book(self.book)
        self.assertEqual(self.library.count_books(), 1, "Failed to add book.")

        # Test that adding a book with an existing ISBN raises a ValueError
        with self.assertRaises(ValueError):
            self.library.add_book(self.book)

    def test_remove_book(self):
        """ Test that a book can be removed from the library """
        # Add a book to the library
        self.library.add_book(self.book)

        # Confirm the book is in the library
        self.assertTrue(self.library.has_book("978-3-16-148410-0"), "Book should be in library.")

        # Remove the book and confirm count_books() decreases
        self.library.remove_book("978-3-16-148410-0")
        self.assertEqual(self.library.count_books(), 0, "Failed to remove book.")

        # Test that removing a book not in library raises a ValueError
        with self.assertRaises(ValueError):
            self.library.remove_book("978-3-16-148410-0")

    def test_has_book(self):
        """ Test the has_book method """
        # Add a book to the library
        self.library.add_book(self.book)

        # Confirm the book is in the library
        self.assertTrue(self.library.has_book("978-3-16-148410-0"), "Book should be in library.")

        # Remove the book
        self.library.remove_book("978-3-16-148410-0")

        # Confirm the book is no longer in the library
        self.assertFalse(self.library.has_book("978-3-16-148410-0"), "Book should not be in library.")

    def test_count_books(self):
        """ Test the count_books method """
        # Initially, the library is empty
        self.assertEqual(self.library.count_books(), 0, "Library should be empty initially.")

        # Add a book and confirm count_books() increases
        self.library.add_book(self.book)
        self.assertEqual(self.library.count_books(), 1, "Failed on book count after adding a book.")

        # Remove the book and confirm count_books() decreases
        self.library.remove_book("978-3-16-148410-0")
        self.assertEqual(self.library.count_books(), 0, "Failed on book count after removing a book.")


if __name__ == '__main__':
    unittest.main()
