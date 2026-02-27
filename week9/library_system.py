# Week 9 - Library System using Composition


class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Added:", book.display_info())

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("Removed:", book.display_info())
                return
        print("Book not found")

    def list_books(self):
        print(f"\nBooks in {self.name}")
        for i, book in enumerate(self.books, 1):
            print(i, "-", book.display_info())

    def search_by_title(self, keyword):
        print("\nSearch Results:")
        for book in self.books:
            if keyword.lower() in book.title.lower():
                print(book.display_info())


# Testing
library = Library("City Library")

b1 = Book("Python Crash Course", "Eric Matthes", "111")
b2 = Book("Clean Code", "Robert Martin", "222")
b3 = Book("AI Basics", "John Doe", "333")

library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

library.list_books()
library.search_by_title("Python")
library.remove_book("Clean Code")
library.list_books()
