from Repository.ICustomerService import ICustomerService
from model.Customer import Customer


class CustomerServiceImpl(ICustomerService):

    def __init__(self):
        self._customers = []
        self._count = 0
        self._last_id_created = 0

    def add_customer(self, customer: Customer) -> Customer:
        self._customers.append(customer)
        customer.set_id(self._last_id_created + 1)
        self._last_id_created += 1
        return customer

    def get_customer(self, customer_email) -> Customer:
        for customer in self._customers:
            if customer.get_email() == customer_email:
                return customer
        for customer in self._customers:
            if customer.get_email != customer_email:
                raise NoCustomerFound
        # if customer_email not in self._customers:
        #     raise NoCustomerFound

    def get_all_customer(self) -> list[Customer]:
        return self._customers

    def get_last_id(self) -> int:
        return self._last_id_created

    def get_count_of_customers(self) -> int:
        return len(self._customers)


class NoCustomerFound(Exception):
    def __repr__(self):
        return f"No Customer Found"
