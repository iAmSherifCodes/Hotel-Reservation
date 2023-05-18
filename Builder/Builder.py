from multipledispatch import dispatch

from data.model.Customer import Customer
from dto.Request.RegisterCustomerRequest import RegisterCustomerRequest
from dto.Response.RegisterCustomerResponse import RegisterCustomerResponse


class Builder:

    @staticmethod
    def mapRegisterCustomerRequest(self, customer_request: RegisterCustomerRequest) -> Customer:
        new_customer = Customer()
        new_customer.set_first_name(customer_request.get_first_name())
        new_customer.set_last_name(customer_request.get_last_name())
        new_customer.set_email(customer_request.get_email())
        return new_customer

    @staticmethod
    def mapRegisterCustomerResponse(self, saved_customer: Customer) -> RegisterCustomerResponse:
        customer_response = RegisterCustomerResponse()
        customer_response.set_first_name(saved_customer.get_first_name())
        customer_response.set_customer_id(saved_customer.get_id())
        customer_response.set_message("Registration Successful")
        return customer_response
