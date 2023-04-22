from unittest import TestCase
from Repository.CustomerServiceImpl import CustomerServiceImpl, NoCustomerFound
from model.Customer import Customer


class Test(TestCase):
    def test_that_when_add_customer_count_increment(self):
        new_customer = Customer("John", "Doe", "johndoe@gmail.com")
        service = CustomerServiceImpl()
        added_customer = service.add_customer(new_customer)
        added_customer2 = service.add_customer(new_customer)
        self.assertEqual(2, service.get_last_id())

    def test_get_customer_by_email(self):
        first_customer = Customer("John", "Doe", "johndoe@gmail.com")
        second_customer = Customer("Janet", "Doe", "janetdoe@gmail.com")
        service = CustomerServiceImpl()
        added_customer = service.add_customer(first_customer)
        added_customer2 = service.add_customer(second_customer)
        self.assertEqual(second_customer, service.get_customer("janetdoe@gmail.com"))

    def test_no_customer_found_by_email_raise_NoCustomerFound(self):
        first_customer = Customer("John", "Doe", "johndoe@gmail.com")
        second_customer = Customer("Janet", "Doe", "janetdoe@gmail.com")
        service = CustomerServiceImpl()
        added_customer = service.add_customer(first_customer)
        added_customer2 = service.add_customer(second_customer)
        with self.assertRaises(NoCustomerFound):
            customer_email = service.get_customer("ayomide@gmail.com")
