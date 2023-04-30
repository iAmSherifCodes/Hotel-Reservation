# ToDo
#  - write the logic for customer Repo
from data.Repository.CustomerRepository import CustomerRepository
from data.model.Customer import Customer


class CustomerNotFound(Exception):
    def __repr__(self):
        return "Customer Not Found"


class CustomerRepositoryImpl(CustomerRepository):

    def __init__(self):
        self.customers = []
        self.last_id_generated = 0

    def save(self, customer: Customer) -> Customer:
        customer_exist: bool = customer.get_id() != 0
        if customer_exist:
            return self._update_customer(customer)
        else:
            return self._save_new_customer(customer)

    def _update_customer(self, customer: Customer) -> Customer:
        self.customers.remove(self.find_by_id(customer.get_id()))
        self.customers.append(customer)
        return customer

    def _save_new_customer(self, customer: Customer) -> Customer:
        customer.set_id(self.last_id_generated + 1)
        self.customers.append(customer)
        self.last_id_generated += 1
        return customer

    def find_by_id(self, customer_id: int) -> Customer:

        for customer in self.customers:
            id_match: bool = customer.get_id() == customer_id

            if id_match:
                return customer
        raise CustomerNotFound

    def get_all_customers(self) -> list[Customer]:
        return self.customers

    def count_of_customers(self) -> int:
        return len(self.customers)
