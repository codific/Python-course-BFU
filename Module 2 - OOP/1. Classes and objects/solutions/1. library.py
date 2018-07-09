class Library:

    def __init__(self, name):
        self.name = name
        self.books = []


class Book:

    def __init__(self, title, author, publisher, isbn, release_date, has_hard_cover = False, total_pages = 0):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.release_date = release_date
        self.has_hard_cover = has_hard_cover
        self.total_pages = total_pages