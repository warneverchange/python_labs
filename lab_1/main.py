from typing import Any

#Зачтено


from CardManager import CardManager
from Reader import Reader
from Book import Book
from CardItem import CardItem
import json
from lupin import Mapper, Schema, fields as f
from Card import Card

file = open("output.json", "w")

card_manager = CardManager()

card_manager.create_card(Reader("Chechkin", "Konstantin", "89963250540", "Chkalova, 44"))
card_manager.add_book(Book("Hello", "askldflksadjgkl", "Art house", "978-5-389-02278-2"), 3)
card_manager.add_book_to_card("978-5-389-02278-2", card_manager.get_cards()[0], 2)


ReaderSchema = Schema({
    "firstName": f.String(binding="first_name"),
    "lastName": f.String(binding="last_name"),
    "phoneNumber": f.String(binding="_phone_number"),
    "address": f.String(binding="address")
})

BookSchema = Schema({
    "name": f.String(binding="_name"),
    "description": f.String(binding="_description"),
    "publishing": f.String(binding="_publishing"),
    "isbnNumber": f.String(binding="_isbn_number")
})

CardItemSchema = Schema({
    "book": f.Object(BookSchema),
    "dateOfIssue": f.Date(binding="date_of_issue"),
    "count": f.Int()
})

CardSchema = Schema({
    "reader": f.Object(ReaderSchema),
    "takenBooks": f.List(f.Object(CardItemSchema), binding="taken_books")
})

CardManagerSchema = Schema({
    "cards": f.List(f.Object(CardSchema), binding="_CardManager__cards"),
    "freeBooksKeys": f.List(f.Object(BookSchema), binding="_CardManager__free_books_keys"),
    "freeBooksValues": f.List(f.Int(), binding="_CardManager__free_books_values")
})

mapper = Mapper()
mapper.register(Book, BookSchema)
mapper.register(Reader, ReaderSchema)
mapper.register(CardItem, CardItemSchema)
mapper.register(Card, CardSchema)
mapper.register(CardManager, CardManagerSchema)

card_manager.prepare()

card_manager_dict = mapper.dump(card_manager, CardManagerSchema)

json.dump(card_manager_dict, file)


file.close()
file = open("output.json", "r")


card_manager_dict = json.load(file)

other_card_manager: CardManager = mapper.load(card_manager_dict, CardManagerSchema)

card_manager.backup()

other_card_manager.print_cards()
other_card_manager.print_books()

file.close()





