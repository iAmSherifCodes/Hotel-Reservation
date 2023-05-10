from multipledispatch import dispatch

from data.model.Customer import Customer
from dto.Request.CreateCustomerRequest import CreateCustomerRequest
from dto.Response.CreateCustomerResponse import CreateCustomerResponse


class Builder:

    # @dispatch()
    @staticmethod
    def buildCreateCustomerRequest(self, customer_request: CreateCustomerRequest) -> Customer:
        new_customer = Customer()
        new_customer.set_first_name(customer_request.get_first_name())
        new_customer.set_last_name(customer_request.get_last_name())
        new_customer.set_email(customer_request.get_email())
        return new_customer

    # @dispatch()
    @staticmethod
    def buildCreateCustomerResponse(self, saved_customer: Customer) -> CreateCustomerResponse:
        customer_response = CreateCustomerResponse()
        customer_response.set_first_name(saved_customer.get_first_name())
        customer_response.set_message("Registration Successful")
        return customer_response
