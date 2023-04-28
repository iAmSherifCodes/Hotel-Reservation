import abc

from data.model.Customer import Customer


class CustomerRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, customer: Customer) -> Customer:
        pass

    @abc.abstractmethod
    def find_by_id(self, customer_id: int) -> Customer:
        pass

    @abc.abstractmethod
    def get_all_customers(self) -> list[Customer]:
        pass
