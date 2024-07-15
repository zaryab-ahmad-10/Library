class Library:
    def __init__(self):
        self.books = []
        self.authors = []


    def add_book(self, book):
        self.books.append(book)
        if book.author not in self.authors:
            self.authors.append(book.author)


    def find_books_by_author(self, author_name):
        return [book for book in self.books if book.author.name == author_name]


    def find_books_by_title(self, title):
        return [book for book in self.books if book.title == title]


    def __str__(self):
        return f"Books: {[book.title for book in self.books]}, Authors: {[author.name for author in self.authors]}"

