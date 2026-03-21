# Complex Python Program: Library Management System (No User Input)

# ------------------------------
# Class Definitions
# ------------------------------

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"{self.book_id} - {self.title} by {self.author} | {status}"


class Library:
    def __init__(self):
        self.books = []
        self.log_file = "library_log.txt"

    def add_book(self, book):
        self.books.append(book)
        self._log_action(f"Added book: {book.title}")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and book.available:
                book.available = False
                self._log_action(f"Issued book: {book.title}")
                return f"Book issued: {book.title}"
        return "Book not available"

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and not book.available:
                book.available = True
                self._log_action(f"Returned book: {book.title}")
                return f"Book returned: {book.title}"
        return "Invalid return operation"

    def list_books(self):
        return [str(book) for book in self.books]

    def _log_action(self, message):
        with open(self.log_file, "a") as f:
            f.write(message + "\n")


# ------------------------------
# Program Execution (No Input)
# ------------------------------

library = Library()

# Add books (no user input)
books_to_add = [
    Book(101, "The Alchemist", "Paulo Coelho"),
    Book(102, "1984", "George Orwell"),
    Book(103, "To Kill a Mockingbird", "Harper Lee"),
    Book(104, "Atomic Habits", "James Clear"),
]

for b in books_to_add:
    library.add_book(b)

# Issue and return some books
print(library.issue_book(102))   # Issue book with ID 102
print(library.issue_book(104))   # Issue book with ID 104
print(library.return_book(104))  # Return Atomic Habits
print(library.issue_book(105))   # Invalid ID example

# Show all books
print("\n===== LIST OF BOOKS =====")
for info in library.list_books():
    print(info)
