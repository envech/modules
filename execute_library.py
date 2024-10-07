from library import Book

books = [
    Book("Brave New World", "Aldous Huxley", 2020, 29.99),
    Book("Do Androids dream of Electric Sheep", "Philip K. Dick", 2018, 19.99),
    Book("The Wind-Up Bird Chronicle", "Haruki Murakami", 2021, 39.99),
]

for book in books:
    print(book.get_info())

most_expensive_book = Book.most_expensive(books)
print(f"The most expensive book is: {most_expensive_book.get_info()}")

books[0].censor("Aldous Huxley", True)
print(books[0].get_info())