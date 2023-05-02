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
        service.register_new_customer(new_customer)
        self.assertEqual(1, service.get_count_of_customers())

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
        service.register_new_customer(first_customer)
        service.register_new_customer(second_customer)
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

    def test_display_all_customers_return_all_saved_customers(self):
        first_customer = Customer()
        second_customer = Customer()
        third_customer = Customer()
        first_customer.set_first_name("John")
        first_customer.set_last_name("Doe")
        first_customer.set_email("johndoe@gmail.com")
        second_customer.set_first_name("Janet")
        second_customer.set_last_name("Doe")
        second_customer.set_email("janetdoe@gmail.com")
        third_customer.set_first_name("2pac")
        third_customer.set_last_name("Shakur")
        third_customer.set_email("shakur@gmail.com")
        service = CustomerServiceImpl()
        service.register_new_customer(first_customer)
        service.register_new_customer(third_customer)
        service.register_new_customer(second_customer)
        all_customers: list[Customer] = [first_customer, third_customer, second_customer]
        print(service.display_all_customers())
        self.assertEqual(all_customers, service.display_all_customers())
