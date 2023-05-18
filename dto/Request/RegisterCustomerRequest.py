
class RegisterCustomerRequest:

    def __init__(self):
        self._first_name: str | None = None
        self._last_name: str | None = None
        self._email: str | None = None

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
