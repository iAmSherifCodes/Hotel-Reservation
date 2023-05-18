from Builder.Builder import Builder
from data.Repository.CustomerRepository import CustomerRepository
from data.Repository.CustomerRepositoryImpl import CustomerRepositoryImpl
from dto.Request.FindCustomerByEmailRequest import FindCustomerByEmailRequest
from dto.Request.RegisterCustomerRequest import RegisterCustomerRequest
from dto.Response.FindCustomerByEmailResponse import FindCustomerByEmailResponse
from dto.Response.RegisterCustomerResponse import RegisterCustomerResponse
from service.ICustomerService import ICustomerService
from data.model.Customer import Customer


class CustomerServiceImpl(ICustomerService):

    _customer_repository: CustomerRepository = CustomerRepositoryImpl()

    def __init__(self):
        pass

    def register_new_customer(self, customer_request: RegisterCustomerRequest) -> RegisterCustomerResponse:
        # new_customer = Customer()
        # new_customer.set_first_name(customer_request.get_first_name())
        # new_customer.set_last_name(customer_request.get_last_name())
        # new_customer.set_email(customer_request.get_email())

        new_customer = Builder.mapRegisterCustomerRequest(self, customer_request)
        saved_customer = self._customer_repository.save(new_customer)
        customer_response = Builder.mapRegisterCustomerResponse(self, saved_customer)
        return customer_response
        # saved_customer = self._customer_repository.save(new_customer)
        # customer_response = CreateCustomerResponse()
        # customer_response.set_first_name(saved_customer.get_first_name())
        # customer_response.set_message("Account Successfully Created")
        # return customer_response

    def find_customer_by_email(self, customer_email_request: FindCustomerByEmailRequest) -> FindCustomerByEmailResponse:
        found_customer: FindCustomerByEmailResponse = FindCustomerByEmailResponse()
        for customer in self.display_all_customers():
            if customer.get_email() == customer_email_request.get_customer_email():
                found_customer.set_customer(customer)
        return found_customer
        # found_customer: Customer | None = None
        # find_by_email_response: FindCustomerByEmailResponse = FindCustomerByEmailResponse()
        # for customer in self._customer_repository.get_all_customers():
        #     if customer.get_email() == customer_email_request:
        #         return customer
                # found_customer = customer
                # find_by_email_response.set_customer(customer)

        # return find_by_email_response
        # for customer in self._customers:
        #     if customer.get_email != customer_email:
        # raise NoCustomerFound
        # if customer_email not in self._customers:
        #     raise NoCustomerFound

    def find_customer_by_id(self, customer_id) -> Customer:
        pass
        # for customer in self._customer_repository.get_all_customers():
        #     if customer.get_id() == customer_id:
        #         return customer
        # raise NoCustomerFound

    def display_all_customers(self) -> list[Customer]:
        return self._customer_repository.get_all_customers()

    def get_count_of_customers(self) -> int:
        return self._customer_repository.count_of_customers()
