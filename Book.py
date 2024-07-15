class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

        author.add_book(self)


    def __str__(self):
        return f"Book: {self.title}, Author: {self.author.name}"
