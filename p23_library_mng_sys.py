class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print("Book added successfully!")
    def view_books(self):
        if not self.books:
            print("No books found!")
        else:
            for book in self.books:
                print(
                    "Title:", book.title,
                    "| Author:", book.author,
                    "| Available:", book.available
                )
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print("Book found!")
                print("Title:", book.title)
                print("Author:", book.author)
                print("Available:", book.available)
                return
        print("Book not found!")
    def borrow_book(self, title):
     for book in self.books:
        if book.title.lower() == title.lower():
            if book.available:
                book.available = False
                print("Book borrowed successfully!")
            else:
                print("Book is already borrowed!")
            return
    print("Book not found!")
    def return_book(self, title):
     for book in self.books:
        if book.title.lower() == title.lower():
            if not book.available:
                book.available = True
                print("Book returned successfully!")
            else:
                print("This book was not borrowed.")
            return
    print("Book not found!")
library = Library()
while True:
    print("\n==== LIBRARY MANAGEMENT SYSTEM ====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4.Borrow Book")
    print("5.Return Book")
    print("6.Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        title = input("Enter book name: ")
        author = input("Enter author name: ")
        library.add_book(title, author)
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        title = input("Enter book name to search: ")
        library.search_book(title)
    elif choice == "4":
     title = input("Enter book name to borrow: ")
     library.borrow_book(title)
    elif choice==5:
        title=input("Enter book name to return:")
        library.return_book(title)
    elif choice == "6":
        print("Thank you for using Library Management System!")
        break
    else:
        print("Enter a valid option!")