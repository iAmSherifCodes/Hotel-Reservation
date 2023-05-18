class FindCustomerByEmailRequest:
    def __init__(self):
        self._customer_email: str | None = None

    def set_customer_email(self, customer_email: str) -> None:
        self._customer_email = customer_email

    def get_customer_email(self) -> str:
        return self._customer_email
