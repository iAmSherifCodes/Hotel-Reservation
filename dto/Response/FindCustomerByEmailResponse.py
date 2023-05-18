from data.model.Customer import Customer


class FindCustomerByEmailResponse:
    def __init__(self):
        self._customer: Customer = Customer()

    def set_customer(self, customer: Customer) -> None:
        self._customer = customer

    def get_customer(self) -> Customer:
        return self._customer
