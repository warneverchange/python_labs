from Reader import Reader
from Card import Card
from Book import Book


class CardManager:
    __cards: list = []

    __free_books: dict = {}


    __free_books_keys: list = []
    __free_books_values: list = []

    def __init__(self):
        pass

    def create_card(self, reader: Reader):
        card = Card(reader)
        if card not in self.__cards:
            self.__cards.append(Card(reader))
        else:
            raise ValueError("Reader already exist")

    def add_book(self, book: Book, quantity: int):
        if book not in self.__free_books.keys():
            self.__free_books[book] = quantity

    def backup(self):
        for i in range(len(self.__free_books_keys)):
            self.__free_books[self.__free_books_keys[i]] = self.__free_books_values[i]

    def prepare(self):
        for key in self.__free_books.keys():
            self.__free_books_keys.append(key)
            self.__free_books_values.append(self.__free_books[key])

    def add_book_to_card(self, isbn_number: str, card: Card, quantity: int):
        for book in self.__free_books.keys():
            if book.isbn_number == isbn_number \
                    and self.__free_books[book] - quantity >= 0:
                card.create_card_item(book, quantity)
                self.__free_books[book] -= quantity
                break

    def return_book(self, isbn_number: str, card: Card):
        pass

    def get_cards(self) -> list:
        return self.__cards

    def print_books(self, indent=0):
        print('\t' * indent + "Books:")
        for book in self.__free_books.keys():
            print('\t' * (indent + 1) + book.__str__() + ", Count: " + str(self.__free_books[book]))

    def print_cards(self, indent=0):
        for card in self.__cards:
            print('\t' * indent + card.__str__())
