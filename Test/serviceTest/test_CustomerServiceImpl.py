from unittest import TestCase
from service.CustomerServiceImpl import CustomerServiceImpl, NoCustomerFound
from data.model.Customer import Customer


class Test(TestCase):
    def test_that_when_add_customer_count_increment(self):
        new_customer = Customer()
        new_customer.set_first_name("John")
        new_customer.set_last_name("Doe")
        new_customer.set_email("johndoe@gmail.com")
        service = CustomerServiceImpl()
        # added_customer = service.register_new_customer(new_customer)
        # added_customer2 = service.register_new_customer(new_customer)
        self.assertEqual(2, service.get_last_id())

    def test_get_customer_by_email(self):
        first_customer = Customer()
        first_customer.set_first_name("John")
        first_customer.set_last_name("Doe")
        first_customer.set_email("johndoe@gmail.com")
        second_customer = Customer()
        second_customer.set_first_name("Janet")
        second_customer.set_last_name("Doe")
        second_customer.set_email("janetdoe@gmail.com")
        service = CustomerServiceImpl()
        # added_customer = service.register_new_customer(first_customer)
        # added_customer2 = service.register_new_customer(second_customer)
        self.assertEqual(second_customer, service.find_customer_by_email("janetdoe@gmail.com"))

    def test_no_customer_found_by_email_raise_NoCustomerFound(self):
        first_customer = Customer()
        second_customer = Customer()
        first_customer.set_first_name("John")
        first_customer.set_last_name("Doe")
        first_customer.set_email("johndoe@gmail.com")
        second_customer.set_first_name("Janet")
        second_customer.set_last_name("Doe")
        second_customer.set_email("janetdoe@gmail.com")
        service = CustomerServiceImpl()
        service.register_new_customer(first_customer)
        service.register_new_customer(second_customer)
        # added_customer = service.add_customer(first_customer)
        # added_customer2 = service.add_customer(second_customer)
        with self.assertRaises(NoCustomerFound):
            customer_email = service.find_customer_by_email("ayomide@gmail.com")
