class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def matches(self, keyword):
        return keyword.lower() in self.title.lower() or keyword.lower() in self.author.lower()

class Reservation:
    def __init__(self, user, book_title):
        self.user = user
        self.book_title = book_title
