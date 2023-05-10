from unittest import TestCase

from Utils.Exceptions.EmailErrorException import EmailErrorException
from data.model.Customer import is_email_valid, Customer


class Test(TestCase):
    def test_is_email_valid(self):
        email = 'iAmSherif@code.code'
        self.assertEqual(True, is_email_valid(email))

    def test_customer_pass_invalid_email_in_constructor_raise_exception(self):
        with self.assertRaises(EmailErrorException) as err:
            new_customer = Customer()
            new_customer.set_email("john@doegmail.673com")

    def test_that_customer_pass_valid(self):
        new_customer = Customer()
        self.assertIsNotNone(new_customer)

    def test_customer(self):
        new_customer = Customer()
        new_customer.set_last_name("Ola")
        new_customer.set_first_name("Software Engineer Sherifdeen")
        new_customer.set_email("myemail@example.me")
        self.assertIsNotNone(new_customer)
        print(new_customer)
