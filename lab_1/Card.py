from Reader import Reader
from CardItem import CardItem
from Book import Book
from datetime import date


class Card:
    taken_books: list = []

    def __init__(self, reader: Reader):
        self.reader = reader

    def create_card_item(self, book: Book, quantity: int):
        card_item: CardItem = CardItem(book, date.today(), quantity)
        self.taken_books.append(card_item)

    def __eq__(self, other):
        if isinstance(other, Card):
            return other.reader == self.reader
        else:
            raise TypeError()

    def __str__(self):
        result = "Card: ("
        for card_item in self.taken_books:
            result += "Card Item: ("
            result += f"Reader: {self.reader.__str__()})"
            result += f"Books: ("
            result += f"{card_item.__str__()}))"
        return result
