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

book = Book('1984', 'George Orwell', 'New American Library', '99921-58-10-7', '01/07/1950', False, 328)
print(book)