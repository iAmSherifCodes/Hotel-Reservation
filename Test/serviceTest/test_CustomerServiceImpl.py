from unittest import TestCase

from Utils.Exceptions.CustomerNotFound import CustomerNotFound
from data.model.Customer import Customer
from dto.Request.FindCustomerByEmailRequest import FindCustomerByEmailRequest
from dto.Request.RegisterCustomerRequest import RegisterCustomerRequest
from dto.Response.FindCustomerByEmailResponse import FindCustomerByEmailResponse
from service.CustomerServiceImpl import CustomerServiceImpl


class Test(TestCase):

    def setUp(self) -> None:
        self.service = CustomerServiceImpl()

    def test_register_customer_count_increment(self):
        self.register_request = RegisterCustomerRequest()
        self.register_request.set_email("johndoe@gmail.com")
        self.register_request.set_first_name("John")
        self.register_request.set_last_name("Doe")
        saved_response = self.service.register_new_customer(self.register_request)
        self.assertIsNotNone(saved_response)
        self.assertEqual("Registration Successful", saved_response.get_message())
        self.assertEqual(5, self.service.get_count_of_customers())

    def test_get_customer_by_email(self):
        first_request = RegisterCustomerRequest()
        first_request.set_first_name("Johns")
        first_request.set_last_name("Doely")
        first_request.set_email("johnsdoely@gmail.com")

        second_request = RegisterCustomerRequest()
        second_request.set_first_name("Janet")
        second_request.set_last_name("Doe")
        second_request.set_email("janetdoely@gmail.com")

        # Provided there are registered customers
        first_saved_customer = self.service.register_new_customer(first_request)
        second_saved_customer = self.service.register_new_customer(second_request)

        # Provided we have a request to find customers
        request: FindCustomerByEmailRequest = FindCustomerByEmailRequest()

        # Action
        request.set_customer_email("janetdoely@gmail.com")
        found_customer = self.service.find_customer_by_email(request)

        self.assertIsNotNone(found_customer)
        self.assertEqual(second_saved_customer.get_customer_id(), found_customer.get_id())

    def test_no_customer_found_by_email_raise_NoCustomerFound(self):
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

        # Provided we have a request object to find customers
        find_by_email_request: FindCustomerByEmailRequest = FindCustomerByEmailRequest()

        # Action
        find_by_email_request.set_customer_email("ayomide@gmail.com")

        with self.assertRaises(CustomerNotFound):
            self.service.find_customer_by_email(find_by_email_request)
