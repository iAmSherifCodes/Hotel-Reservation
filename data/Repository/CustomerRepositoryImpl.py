from Utils.AppUtils import AppUtils
from Utils.Exceptions.CustomerNotFound import CustomerNotFound
from data.Repository.CustomerRepository import CustomerRepository
from data.model.Customer import Customer


class CustomerRepositoryImpl(CustomerRepository):

    def __init__(self):
        self._customers = []

    def save(self, customer: Customer) -> Customer:
        customer.set_id(str(AppUtils.generate_id()))
        self._customers.append(customer)
        return customer

    def find_by_id(self, customer_id: str) -> Customer | None:
        for customer in self._customers:
            if customer.get_id() == customer_id:
                return customer
        return None

    def get_all_customers(self) -> list[Customer]:
        return self._customers

    def count_of_customers(self) -> int:
        return len(self._customers)
