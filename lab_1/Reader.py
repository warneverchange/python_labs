import re
from typing import Match


def valid_phone_number(phone_number: str) -> Match[str] | None:
    pattern = "^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"
    return re.fullmatch(pattern, phone_number)


class Reader:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 phone_number: str,
                 address: str):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self._address = address

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address: str):
        self._address = address

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str):
        if valid_phone_number(phone_number):
            self._phone_number = phone_number
        else:
            raise ValueError("Phone number isn't correct")

    def __str__(self):
        return f"First name: {self.first_name}\n" \
               f"Last name: {self.last_name}\n" \
               f"Phone number: {self.phone_number}\n" \
               f"Address: {self.address}\n"



