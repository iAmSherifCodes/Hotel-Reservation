class FindCustomerByEmailResponse:
    def __init__(self, first_name: str, last_name: str, email: str, c_id: str):
        self._first_name: str = first_name
        self._last_name: str = last_name
        self._email: str = email
        self._id: str = c_id

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
        self._email = email

    def get_id(self):
        return self._id

    def __repr__(self):
        return f"""
        ---FOUND CUSTOMER---
        Customer Name : {self.get_first_name() + " " + self._last_name}
        Customer Email : {self.get_email()}
        Customer ID: {self.get_id()}
        """
