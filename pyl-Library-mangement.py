class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

class Library:
    def _init_(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f'"{title}" added to library.')

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Available Books:")
        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(f'{book.title} by {book.author} - {status}')

    def issue_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_issued:
                book.is_issued = True
                print(f'You have issued "{title}".')
                return
        print(f'"{title}" is not available.')

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_issued:
                book.is_issued = False
                print(f'"{title}" has been returned.')
                return
        print(f'"{title}" was not issued or not found.')

# Demo Menu
library = Library()

while True:
    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        library.add_book(title, author)
    elif choice == '2':
        library.display_books()
    elif choice == '3':
        title = input("Enter title to issue: ")
        library.issue_book(title)
    elif choice == '4':
        title = input("Enter title to return: ")
        library.return_book(title)
    elif choice == '5':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")