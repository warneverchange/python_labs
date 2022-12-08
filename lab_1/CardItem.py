from Book import Book
from datetime import date


class CardItem:
    def __init__(self, book: Book, date_of_issue: date, count: int):
        self._book = book
        self._date_of_issue = date_of_issue
        self._count = count

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book: Book):
        self._book = book

    @property
    def date_of_issue(self):
        return self._date_of_issue

    @date_of_issue.setter
    def date_of_issue(self, date_of_issue: date):
        self._date_of_issue = date_of_issue

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count: int):
        self._count = count

