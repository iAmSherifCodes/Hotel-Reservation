class CreateCustomerResponse:
    def __init__(self):
        self._first_name = None
        self._message: str | None = None

    def get_message(self) -> str:
        return self._message
        # return f"{self._first_name} " + self._message

    def set_message(self, message) -> None:
        self._message = message

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name
