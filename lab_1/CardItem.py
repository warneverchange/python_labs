from Book import Book
from datetime import date


class CardItem:
    def __init__(self, book: Book, date_of_issue: date, count: int):
        self.book = book
        self.date_of_issue = date_of_issue
        self.count = count

    def __str__(self):
        return f"(Book: ({self.book}), Date: {self.date_of_issue}, Count: {self.count})"