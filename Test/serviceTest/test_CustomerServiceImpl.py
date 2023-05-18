from unittest import TestCase

from data.Repository.CustomerRepository import CustomerRepository
from data.Repository.CustomerRepositoryImpl import CustomerRepositoryImpl
from dto.Request.FindCustomerByEmailRequest import FindCustomerByEmailRequest
from dto.Request.RegisterCustomerRequest import RegisterCustomerRequest
from dto.Response.FindCustomerByEmailResponse import FindCustomerByEmailResponse
from dto.Response.RegisterCustomerResponse import RegisterCustomerResponse
from service.CustomerServiceImpl import CustomerServiceImpl
from data.model.Customer import Customer


class Test(TestCase):

    def setUp(self) -> None:
        self.service = CustomerServiceImpl()

    def test_that_when_add_customer_count_increment(self):
        self.register_request = RegisterCustomerRequest()
        self.register_request.set_email("johndoe@gmail.com")
        self.register_request.set_first_name("John")
        self.register_request.set_last_name("Doe")
        saved_response = self.service.register_new_customer(self.register_request)
        self.assertIsNotNone(saved_response)
        self.assertEqual("Registration Successful", saved_response.get_message())
        self.assertEqual(1, self.service.get_count_of_customers())

    def test_get_customer_by_email(self):
        first_customer_request = RegisterCustomerRequest()
        first_customer_request.set_first_name("Johns")
        first_customer_request.set_last_name("Doely")
        first_customer_request.set_email("johnsdoely@gmail.com")

        second_customer_request = RegisterCustomerRequest()
        second_customer_request.set_first_name("Janet")
        second_customer_request.set_last_name("Doe")
        second_customer_request.set_email("janetdoely@gmail.com")

        # Provided there are registered customers
        saved_first_customer = self.service.register_new_customer(first_customer_request)
        saved_second_customer = self.service.register_new_customer(second_customer_request)

        # Provided we have a request to find customers
        find_by_email_request: FindCustomerByEmailRequest = FindCustomerByEmailRequest()
        find_by_email_response: FindCustomerByEmailResponse = FindCustomerByEmailResponse()

        find_by_email_request.set_customer_email(second_customer_request.get_email())
        find_by_email_response.set_customer(self.service.find_customer_by_email(find_by_email_request).get_customer())
        print(find_by_email_response)
        # print(find_by_email_request.get_customer_email())
        # find_by_email_response.set_customer()
        # print(self.service.display_all_customers())
        # found_customer = self.service.find_customer_by_email(find_by_email_request).get_customer()
        # found_customer_response = self.service.find_customer_by_email(find_by_email_request)
        self.assertEqual(saved_second_customer, find_by_email_response.get_customer())

    # def test_no_customer_found_by_email_raise_NoCustomerFound(self):
    # first_customer = Customer()
    # second_customer = Customer()
    # first_customer.set_first_name("John")
    # first_customer.set_last_name("Doe")
    # first_customer.set_email("johndoe@gmail.com")
    # second_customer.set_first_name("Janet")
    # second_customer.set_last_name("Doe")
    # second_customer.set_email("janetdoe@gmail.com")
    # service = CustomerServiceImpl()
    # service.register_new_customer(first_customer)
    # service.register_new_customer(second_customer)
    # added_customer = service.add_customer(first_customer)
    # added_customer2 = service.add_customer(second_customer)
    # with self.assertRaises(NoCustomerFound):
    #     customer_email = service.find_customer_by_email("ayomide@gmail.com")
    #
    # def test_display_all_customers_return_all_saved_customers(self):
    #     first_customer = Customer()
    #     second_customer = Customer()
    #     third_customer = Customer()
    #     first_customer.set_first_name("John")
    #     first_customer.set_last_name("Doe")
    #     first_customer.set_email("johndoe@gmail.com")
    #     second_customer.set_first_name("Janet")
    #     second_customer.set_last_name("Doe")
    #     second_customer.set_email("janetdoe@gmail.com")
    #     third_customer.set_first_name("2pac")
    #     third_customer.set_last_name("Shakur")
    #     third_customer.set_email("shakur@gmail.com")
    #     service = CustomerServiceImpl()
    #     service.register_new_customer(first_customer)
    #     service.register_new_customer(third_customer)
    #     service.register_new_customer(second_customer)
    #     all_customers: list[Customer] = [first_customer, third_customer, second_customer]
    #     print(service.display_all_customers())
    #     self.assertEqual(all_customers, service.display_all_customers())
#
#
#
