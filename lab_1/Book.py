import re


def check_isbn(isbn):
    check_digit = int(isbn[-1])
    match = re.search(r'(\d)-(\d{3})-(\d{5})', isbn[:-1])

    if not match:
        return False

    digits = match.group(1) + match.group(2) + match.group(3)
    result = 0

    for i, digit in enumerate(digits):
      result += (i + 1) * int(digit)

    return True if (result % 11) == check_digit else False


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
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def publishing(self):
        return self._publishing

    @publishing.setter
    def publishing(self, publishing: str):
        self._publishing = publishing

    @property
    def isbn_number(self):
        return self._isbn_number

    @isbn_number.setter
    def isbn_number(self, isbn_number: str):
        if check_isbn(isbn_number):
            self._isbn_number = isbn_number
        else:
            raise ValueError("ISBN number isn't correct")
