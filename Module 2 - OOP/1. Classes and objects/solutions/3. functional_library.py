class Library:

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def add_multiple_books(self, books):
        for book in books:
            self.add_book(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def remove_multiple_books(self, books):
        for book in books:
            self.remove_book(book)

    def search_book(self, title='', author=''):
        filter_lambda = lambda book: title.lower() in book.title.lower()
        if author:
            filter_lambda = lambda book: title.lower() in book.title.lower() \
                                         or author.lower() in book.author.lower()
        filtered_books = filter(filter_lambda, self.books)
        if not filtered_books:
            print('No books found.')
        else:
            for book in filtered_books:
                print(book)

    def get_book_info(self, book):
        if book in self.books:
            print(book)
        else:
            print('Book not found.')

    def list_books(self):
        if self.books:
            print(f'Total number of books: {len(self.books)}')
            for book in self.books:
                print(book)
                print('=' * 30)
        else:
            print('No books in the library.')



class Book:

    def __init__(self, title, author, publisher, isbn, release_date, has_hard_cover = False, total_pages = 0):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.release_date = release_date
        self.has_hard_cover = has_hard_cover
        self.total_pages = total_pages

    def __str__(self):
        book_info = f'''
        Title - {self.title}
        Author - {self.author}
        Publisher - {self.publisher}
        ISBN - {self.isbn}
        Release date - {self.release_date}
        Hard cover - {'yes' if self.has_hard_cover else 'no'}
        Total pages - {self.total_pages if self.total_pages else 'N/A'}
        '''
        return book_info


library = Library('Town library')

first_book = Book('1984', 'George Orwell', 'New American Library', '99921-58-10-7', '01/07/1950', False, 328)
second_book = Book("Harry Potter and the Sorcerer's Stone", 'J.K. Rowling', 'Scholastic', '978-0439708180', '01/09/1998', False, 309)

# Adding books one by one
# library.add_book(first_book)
# library.add_book(second_book)

# Adding multiple books
library.add_multiple_books([first_book, second_book])

# Printing info for the specified book
library.get_book_info(first_book)

# Searching for books by title and author
library.search_book(title='harry potter', author='george')

# Removing a specific book
library.remove_book(second_book)

# Listing all the books in the library
library.list_books()