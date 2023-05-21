from Builder.Builder import Builder
from Utils.Exceptions.CustomerNotFound import CustomerNotFound
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
        customer_email: str = customer_email_request.get_customer_email()

        found_customer: Customer = Customer()
        for customer in self.display_all_customers():
            if customer.get_email() == customer_email:
                # found_customer.set_first_name(customer.get_first_name())
                # found_customer.set_last_name(customer.get_last_name())
                # found_customer.set_email(customer.get_email())
                response: FindCustomerByEmailResponse = FindCustomerByEmailResponse(customer.get_first_name(),
                                                                                    customer.get_last_name(),
                                                                                    customer.get_email(),
                                                                                    customer.get_id())
                return response

        raise CustomerNotFound

    def display_all_customers(self) -> list[Customer]:
        return self._customer_repository.get_all_customers()

    def get_count_of_customers(self) -> int:
        return self._customer_repository.count_of_customers()
