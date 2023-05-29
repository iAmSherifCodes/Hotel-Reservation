class FindReservationByCustomerEmailRequest:
    def __init__(self):
        self._customer_email: str = ""

    def get_customer_email(self) -> str:
        return self._customer_email

    def set_customer_email(self, email: str):
        self._customer_email = email
