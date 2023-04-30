from unittest import TestCase

from data.Repository.CustomerRepositoryImpl import CustomerRepositoryImpl, CustomerNotFound
from data.model.Customer import Customer


class Test(TestCase):
    # customerRepository = CustomerRepositoryImpl()

    # customerRepository: CustomerRepository = CustomerRepositoryImpl()

    def setUp(self) -> None:
        self.customerRepository = CustomerRepositoryImpl()
        self.first_name = "John"
        self.second_name = "Doe"
        self.email = "JohnDoe@gmail.com"

    def test_that_customer_can_be_saved(self):
        new_customer = Customer()
        new_customer.set_first_name(self.first_name)
        new_customer.set_last_name(self.second_name)
        new_customer.set_email(self.email)
        self.assertEqual(new_customer, self.customerRepository.save(new_customer))

    def test_that_id_is_increasing(self):
        new_customer = Customer()
        new_customer.set_first_name(self.first_name)
        new_customer.set_last_name(self.second_name)
        new_customer.set_email(self.email)
        self.customerRepository.save(new_customer)
        self.assertEqual(1, new_customer.get_id())

    def test_that_customer_is_saved_count_of_customers_increase(self):
        new_customer = Customer()
        new_customer.set_first_name(self.first_name)
        new_customer.set_last_name(self.second_name)
        new_customer.set_email(self.email)
        self.customerRepository.save(new_customer)
        self.assertEqual(1, self.customerRepository.count_of_customers())

    def test_find_by_id_returns_customer(self):
        new_customer = Customer()
        new_customer.set_first_name(self.first_name)
        new_customer.set_last_name(self.second_name)
        new_customer.set_email(self.email)
        self.customerRepository.save(new_customer)
        # second_customer = Customer()
        # second_customer.set_first_name("Kodak")
        # second_customer.set_last_name("Black")
        # second_customer.set_email("kidak@gmail.com")
        # self.customerRepository.save(second_customer)
        # new_customer.set_first_name("Janet")
        # second_customer.set_first_name("2pac")
        # self.customerRepository.save(new_customer)
        # self.customerRepository.save(second_customer)
        # print(self.customerRepository.get_all_customers())
        # self.assertEqual(3, self.customerRepository.count_of_customers())
        self.assertEqual(new_customer, self.customerRepository.find_by_id(1))

    def test_that_customer_not_found_raise_exception(self):
        new_customer = Customer()
        new_customer.set_first_name(self.first_name)
        new_customer.set_last_name(self.second_name)
        new_customer.set_email(self.email)
        self.customerRepository.save(new_customer)
        with self.assertRaises(CustomerNotFound):
            self.assertEqual(new_customer, self.customerRepository.find_by_id(2))

    def test_that_if_customer_already_exist_update_customer(self):
        new_customer = Customer()
        new_customer.set_first_name(self.first_name)
        new_customer.set_last_name(self.second_name)
        new_customer.set_email(self.email)
        self.customerRepository.save(new_customer)
        self.assertEqual("John", new_customer.get_first_name())
        new_customer.set_first_name("Janet")
        self.customerRepository.save(new_customer)
        self.assertEqual("Janet", new_customer.get_first_name())
        self.assertEqual(1, new_customer.get_id())
