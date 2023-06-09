import re
# from Utils.Exceptions import EmailErrorException


def is_email_valid(email: str) -> bool:
    # pattern = r'^[a-z]'
    form = r'^[a-zA-Z0-9]*@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    return bool(re.fullmatch(form, email))


class Customer:

    def __init__(self):
        self._first_name: str = ""
        self._last_name: str = ""
        self._customer_id: str = ""
        self._email: str = ""

    def get_first_name(self) -> str:
        return self._first_name

    def get_last_name(self) -> str:
        return self._last_name

    def get_email(self) -> str:
        return self._email

    def set_first_name(self, first_name: str) -> None:
        self._first_name = first_name

    def set_last_name(self, last_name: str) -> None:
        self._last_name = last_name

    def set_email(self, email: str) -> None:
        if is_email_valid(email):
            self._email = email
        else:
            raise Exception

    def get_id(self) -> str:
        return self._customer_id

    def set_id(self, customer_id: str) -> None:
        self._customer_id = customer_id

    def __repr__(self):
        return f"""
        ---CUSTOMER---
        Customer Name : {self.get_first_name() + " " + self._last_name}
        Customer Email : {self.get_email()}
        Customer ID : {self.get_id()}
        """
