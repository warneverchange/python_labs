import re
from typing import Match


def valid_phone_number(phone_number: str) -> Match[str] | None:
    pattern = r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"
    return re.fullmatch(pattern, phone_number)


class Reader:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 phone_number: str,
                 address: str):
        self.first_name = first_name
        self.last_name = last_name
        if valid_phone_number(phone_number):
            self._phone_number = phone_number
        else:
            raise ValueError("Phone number isn't correct")
        self.address = address

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

    def __eq__(self, other):
        if isinstance(other, Reader):
            return self.address == other.address \
                   and self.first_name == other.first_name \
                   and self.last_name == other.last_name \
                   and self.phone_number == other.phone_number
        else:
            raise TypeError()



