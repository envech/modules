class Book:
    def __init__(self, title, author, year, price, stoplist=False):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.stoplist = stoplist

    def get_info(self):
        return f"Author: {self.author}, Title: {self.title}, Year: {self.year}, Price: {self.price}, Stoplist: {self.stoplist}"

    def most_expensive(books):
        most_expensive_book = None
        max_price = -1
        for book in books:
            price = book.price
            if price > max_price:
                max_price = price
                most_expensive_book = book
            return most_expensive_book

    def set_stoplist(self, value):
        self.stoplist = value

    def censor(self, author_name, value):
        if self.author == author_name:
            self.stoplist = value