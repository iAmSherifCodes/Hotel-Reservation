from Builder.Builder import Builder
from data.Repository.CustomerRepository import CustomerRepository
from data.Repository.CustomerRepositoryImpl import CustomerRepositoryImpl
from dto.Request.CreateCustomerRequest import CreateCustomerRequest
from dto.Response.CreateCustomerResponse import CreateCustomerResponse
from service.ICustomerService import ICustomerService
from data.model.Customer import Customer


class CustomerServiceImpl(ICustomerService):
    _customer_repository: CustomerRepository = CustomerRepositoryImpl()

    def __init__(self):
        pass

    def register_new_customer(self, customer_request: CreateCustomerRequest) -> CreateCustomerResponse:
        # new_customer = Customer()
        # new_customer.set_first_name(customer_request.get_first_name())
        # new_customer.set_last_name(customer_request.get_last_name())
        # new_customer.set_email(customer_request.get_email())

        new_customer = Builder.buildCreateCustomerRequest(self, customer_request)
        saved_customer = self._customer_repository.save(new_customer)
        customer_response = Builder.buildCreateCustomerResponse(self, saved_customer)
        return customer_response
        # saved_customer = self._customer_repository.save(new_customer)
        # customer_response = CreateCustomerResponse()
        # customer_response.set_first_name(saved_customer.get_first_name())
        # customer_response.set_message("Account Successfully Created")
        # return customer_response

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
