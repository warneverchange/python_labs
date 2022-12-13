import re

import re
import sys

# `regex` checks for ISBN-10 or ISBN-13 format


def check_isbn(isbn: str):
    regex = re.compile(r"^(?:ISBN(?:-1[03])?:? )?(?=[-0-9 ]{17}$|[-0-9X ]{13}$|[0-9X]"
                       r"{10}$)(?:97[89][- ]?)?[0-9]{1,5}[- ]?(?:[0-9]+[- ]?){2}[0-9X]$")
    if regex.search(isbn):
        chars = list(re.sub("[^0-9X]", "", isbn)    )
        last = chars.pop()

        if len(chars) == 9:
            # Compute the ISBN-10 check digit
            val = sum((x + 2) * int(y) for x, y in enumerate(reversed(chars)))
            check = 11 - (val % 11)
            if check == 10:
                check = "X"
            elif check == 11:
                check = "0"
        else:
            # Compute the ISBN-13 check digit
            val = sum((x % 2 * 2 + 1) * int(y) for x, y in enumerate(chars))
            check = 10 - (val % 10)
            if check == 10:
                check = "0"

        if str(check) == last:
            return True
        else:
            return False
    else:
        return False


class Book:
    def __init__(self, name: str, description: str, publishing: str, _isbn_number: str):
        self._name = name
        self._description = description
        self._publishing = publishing
        if check_isbn(_isbn_number):
            self._isbn_number = _isbn_number
        else:
            raise ValueError("ISBN number isn't correct")

    @property
    def isbn_number(self):
        return self._isbn_number

    @isbn_number.setter
    def isbn_number(self, isbn_number: str):
        if check_isbn(isbn_number):
            self._isbn_number = isbn_number
        else:
            raise ValueError("ISBN number isn't correct")

    def __str__(self) -> str:
        return f"(Name: {self._name}, Description: {self._description}," \
               f" Publishing: {self._publishing}, ISBN number: {self._isbn_number})"

