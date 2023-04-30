# ToDo
#  - write the logic for customer Repo
from data.Repository.CustomerRepository import CustomerRepository
from data.model.Customer import Customer


class CustomerNotFound(Exception):
    def __repr__(self):
        return "Customer Not Found"


class CustomerRepositoryImpl(CustomerRepository):

    def __init__(self):
        self._customers = []
        self._last_id_generated = 0

    def save(self, customer: Customer) -> Customer:
        customer_exist: bool = customer.get_id() != 0
        if customer_exist:
            return self._update_customer(customer)
        else:
            return self._save_new_customer(customer)

    def _update_customer(self, customer: Customer) -> Customer:
        self._customers.remove(self.find_by_id(customer.get_id()))
        self._customers.append(customer)
        return customer

    def _save_new_customer(self, customer: Customer) -> Customer:
        customer.set_id(self._last_id_generated + 1)
        self._customers.append(customer)
        self._last_id_generated += 1
        return customer

    def find_by_id(self, customer_id: int) -> Customer:

        for customer in self._customers:
            id_match: bool = customer.get_id() == customer_id

            if id_match:
                return customer
        raise CustomerNotFound

    def get_all_customers(self) -> list[Customer]:
        return self._customers

    def count_of_customers(self) -> int:
        return len(self._customers)
