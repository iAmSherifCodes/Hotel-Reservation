import abc

from data.model.Customer import Customer


class ICustomerService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_customer(self, customer: Customer):
        pass

    @abc.abstractmethod
    def get_customer(self, customer_email):
        pass

    @abc.abstractmethod
    def get_all_customer(self):
        pass
