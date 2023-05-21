import abc

from data.model.Customer import Customer
from dto.Request import RegisterCustomerRequest
from dto.Response import RegisterCustomerResponse


class ICustomerService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def register_new_customer(self, register_user_request: RegisterCustomerRequest) -> RegisterCustomerResponse:
        pass

    @abc.abstractmethod
    def find_customer_by_email(self, customer_email: str) -> Customer:
        pass

    # @abc.abstractmethod
    # def find_customer_by_id(self, customer_id: int) -> Customer:
    #     pass

    @abc.abstractmethod
    def display_all_customers(self) -> list[Customer]:
        pass
