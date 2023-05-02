from data.Repository.CustomerRepository import CustomerRepository
from data.Repository.CustomerRepositoryImpl import CustomerRepositoryImpl
from service.ICustomerService import ICustomerService
from data.model.Customer import Customer


class CustomerServiceImpl(ICustomerService):

    def __init__(self):
        self._customer_repository: CustomerRepository = CustomerRepositoryImpl()
        self._count = 0
        self._last_id_created = 0

    def register_new_customer(self, customer: Customer) -> Customer:
        self._customer_repository.save(customer)
        customer.set_id(self._last_id_created + 1)
        self._last_id_created += 1
        return customer

    def find_customer_by_email(self, customer_email) -> Customer:
        for customer in self._customer_repository.get_all_customers():
            if customer.get_email() == customer_email:
                return customer
        # for customer in self._customers:
        #     if customer.get_email != customer_email:
        raise NoCustomerFound
        # if customer_email not in self._customers:
        #     raise NoCustomerFound

    def find_customer_by_id(self, customer_id) -> Customer:
        for customer in self._customer_repository.get_all_customers():
            if customer.get_id() == customer_id:
                return customer
        raise NoCustomerFound

    def display_all_customers(self) -> list[Customer]:
        return self._customer_repository.get_all_customers()

    def get_count_of_customers(self) -> int:
        return self._customer_repository.count_of_customers()


class NoCustomerFound(Exception):
    def __repr__(self):
        return f"No Customer Found"
