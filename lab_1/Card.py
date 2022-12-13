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
        result = "Card: \n"
        for card_item in self.taken_books:
            result += "Card Item: \n\n"
            result += f"Reader: \n{self.reader.__str__()}\n"
            result += f"Books: \n"
            result += card_item.__str__()
        return result
