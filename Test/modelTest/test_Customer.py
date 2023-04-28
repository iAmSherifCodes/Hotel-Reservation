from unittest import TestCase

from data.model.Customer import is_email_valid, Customer, EmailErrorException


class Test(TestCase):
    def test_is_email_valid(self):
        email = 'iAmSherif@code.code'
        self.assertEqual(True, is_email_valid(email))

    def test_customer_pass_invalid_email_in_constructor_raise_exception(self):
        with self.assertRaises(EmailErrorException):
            new_customer = Customer("John", "Doe", "johndow.com@gmail")

    def test_that_customer_pass_valid(self):
        new_customer = Customer("John", "Doe", "johndoe@gmail.com")
        self.assertIsNotNone(new_customer)
