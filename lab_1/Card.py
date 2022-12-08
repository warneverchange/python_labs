from Reader import Reader
from CardItem import CardItem
from Book import Book
from datetime import date


class Card:
    taken_books: list = []

    @property
    def reader(self):
        return self._reader

    @reader.setter
    def reader(self, reader: Reader):
        self._reader = reader

    def __init__(self, reader: Reader):
        self._reader = reader

    def create_card_item(self, book: Book, quantity: int):
        card_item = CardItem(book, date.today(), quantity)
        self.taken_books.append(card_item)
