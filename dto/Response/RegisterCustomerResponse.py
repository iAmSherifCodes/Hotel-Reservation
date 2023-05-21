class RegisterCustomerResponse:
    def __init__(self):
        self._first_name: str | None = None
        self._customer_id: str | None = None
        self._message: str | None = None
        self._last_name: str | None = None
        self._email: str | None = None

    def get_message(self) -> str:
        return self._message
        # return f"{self._first_name} " + self._message

    def set_message(self, message) -> None:
        self._message = message

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_last_name(self):
        return self._first_name

    def set_last_name(self, first_name):
        self._first_name = first_name

    def get_email(self):
        return self._first_name

    def set_email(self, first_name):
        self._first_name = first_name

    def get_customer_id(self) -> str:
        return self._customer_id
        # return f"{self._first_name} " + self._message

    def set_customer_id(self, customer_id) -> None:
        self._customer_id = customer_id
