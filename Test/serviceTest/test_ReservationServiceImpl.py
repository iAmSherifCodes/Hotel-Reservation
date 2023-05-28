from datetime import timedelta, date
from unittest import TestCase

from Utils.Exceptions.RoomNotAvailableForReservation import RoomNotAvailableForReservation
from data.model.Customer import Customer
from data.model.Room import Room
from dto.Request.RegisterCustomerRequest import RegisterCustomerRequest
from service.CustomerServiceImpl import CustomerServiceImpl
from service.ReservationServiceImpl import ReservationServiceImpl
from service.RoomServiceImpl import RoomServiceImpl


class Test(TestCase):

    def test_that_we_have_a_reservation_service_impl(self):
        # reservation_service: IReservationService =
        self.assertIsNotNone(ReservationServiceImpl())

    def test_reserve_a_room(self):
        reservation_service = ReservationServiceImpl()

        # Provided we have several rooms in the hotel
        room_service = RoomServiceImpl()
        first_room = Room()
        second_room = Room()
        third_room = Room()
        fourth_room = Room()
        fifth_room = Room()
        room_one = room_service.add_room(fourth_room)
        room_two = room_service.add_room(fifth_room)
        room_three = room_service.add_room(third_room)
        room_four = room_service.add_room(second_room)
        room_five = room_service.add_room(first_room)

        room_service.get_all_rooms()

        # Provided we have customers
        customer_service = CustomerServiceImpl()
        first_customer = RegisterCustomerRequest()
        first_customer.set_email("johndoe@gmail.com")
        first_customer.set_first_name("John")
        first_customer.set_last_name("Doe")

        second_customer = RegisterCustomerRequest()
        second_customer.set_first_name("Johns")
        second_customer.set_last_name("Doely")
        second_customer.set_email("johnsdoely@gmail.com")

        third_customer = RegisterCustomerRequest()
        third_customer.set_first_name("Janet")
        third_customer.set_last_name("Doe")
        third_customer.set_email("janetdoely@gmail.com")

        # Provided customers are registered
        first_saved_customer = customer_service.register_new_customer(first_customer)
        second_saved_customer = customer_service.register_new_customer(second_customer)
        third_saved_customer = customer_service.register_new_customer(third_customer)
 
        # Provided there is a check-in and check-out from the customer
        check_in_date: date = date.today()
        check_out_date: date = date(2023, 5, 15)

        # first_customer
        customer = Customer()
        customer.set_first_name(first_saved_customer.get_first_name())
        customer.set_last_name(first_saved_customer.get_last_name())
        customer.set_email(first_saved_customer.get_email())
        customer.set_id(first_saved_customer.get_customer_id())

        # reservation_service
        reservation_service.reserve_a_room(customer, room_one, check_in_date, check_out_date)
        self.assertTrue(room_one.get_is_reserved())
        self.assertEqual(2, len(reservation_service.display_reservations()))

    def test_conflict_reservation_raise_RoomIsReservedException(self):
        reservation_service = ReservationServiceImpl()

        # Provided we have several rooms in the hotel
        room_service = RoomServiceImpl()
        first_room = Room()
        second_room = Room()
        third_room = Room()
        fourth_room = Room()
        fifth_room = Room()
        room_one = room_service.add_room(fourth_room)
        room_two = room_service.add_room(fifth_room)
        room_three = room_service.add_room(third_room)
        room_four = room_service.add_room(second_room)
        room_five = room_service.add_room(first_room)

        room_service.get_all_rooms()

        # Provided we have customers
        customer_service = CustomerServiceImpl()
        first_customer = RegisterCustomerRequest()
        first_customer.set_email("johndoe@gmail.com")
        first_customer.set_first_name("John")
        first_customer.set_last_name("Doe")

        second_customer = RegisterCustomerRequest()
        second_customer.set_first_name("Johns")
        second_customer.set_last_name("Doely")
        second_customer.set_email("johnsdoely@gmail.com")

        third_customer = RegisterCustomerRequest()
        third_customer.set_first_name("Janet")
        third_customer.set_last_name("Doe")
        third_customer.set_email("janetdoely@gmail.com")

        # Provided customers are registered
        first_saved_customer = customer_service.register_new_customer(first_customer)
        second_saved_customer = customer_service.register_new_customer(second_customer)
        third_saved_customer = customer_service.register_new_customer(third_customer)

        # Provided there is a check-in and check-out from the customer
        check_in_date: date = date.today()
        check_out_date: date = date(2023, 5, 15)

        # first_customer
        customer = Customer()
        customer.set_first_name(first_saved_customer.get_first_name())
        customer.set_last_name(first_saved_customer.get_last_name())
        customer.set_email(first_saved_customer.get_email())
        customer.set_id(first_saved_customer.get_customer_id())

        # reservation_service
        reservation_service.reserve_a_room(customer, room_one, check_in_date, check_out_date)
        self.assertTrue(room_one.get_is_reserved())

        with self.assertRaises(RoomNotAvailableForReservation):
            reservation_service.reserve_a_room(customer, room_one, check_in_date, check_out_date)

    def test_search_for_available_rooms(self):
        reservation_service = ReservationServiceImpl()

        # Provided we have several rooms in the hotel
        room_service = RoomServiceImpl()
        first_room = Room()
        first_room.set_room_type("Double")
        second_room = Room()
        second_room.set_room_type("SINGLE")
        third_room = Room()
        third_room.set_room_type("single")
        fourth_room = Room()
        fourth_room.set_room_type("exclusive")
        fifth_room = Room()
        fifth_room.set_room_type("double")
        room_one = room_service.add_room(fourth_room)
        room_two = room_service.add_room(fifth_room)
        room_three = room_service.add_room(third_room)
        room_four = room_service.add_room(second_room)
        room_five = room_service.add_room(first_room)
        # print(room_five.get_is_reserved())

        room_service.get_all_rooms()

        # Provided we have customers
        customer_service = CustomerServiceImpl()
        first_customer = RegisterCustomerRequest()
        first_customer.set_email("johndoe@gmail.com")
        first_customer.set_first_name("John")
        first_customer.set_last_name("Doe")

        second_customer = RegisterCustomerRequest()
        second_customer.set_first_name("Johns")
        second_customer.set_last_name("Doely")
        second_customer.set_email("johnsdoely@gmail.com")

        third_customer = RegisterCustomerRequest()
        third_customer.set_first_name("Janet")
        third_customer.set_last_name("Doe")
        third_customer.set_email("janetdoely@gmail.com")

        # Provided customers are registered
        first_saved_customer = customer_service.register_new_customer(first_customer)
        second_saved_customer = customer_service.register_new_customer(second_customer)
        third_saved_customer = customer_service.register_new_customer(third_customer)

        # Provided there is a check-in and check-out from the customer
        check_in_date: date = date.today()
        check_out_date1: date = date(2023, 6, 1)
        check_out_date2: date = date(2023, 6, 2)
        check_out_date3: date = date(2023, 6, 3)
        check_out_date4: date = date(2023, 6, 4)
        check_out_date5: date = date(2023, 6, 5)

        # first_customer
        customer = Customer()
        customer.set_first_name(first_saved_customer.get_first_name())
        customer.set_last_name(first_saved_customer.get_last_name())
        customer.set_email(first_saved_customer.get_email())
        customer.set_id(first_saved_customer.get_customer_id())

        # reservation_service
        reservation_service.reserve_a_room(customer, room_one, check_in_date, check_out_date1)
        reservation_service.reserve_a_room(customer, room_two, check_in_date, check_out_date2)
        reservation_service.reserve_a_room(customer, room_three, check_in_date, check_out_date3)
        reservation_service.reserve_a_room(customer, room_five, check_in_date, check_out_date4)
        reservation_service.reserve_a_room(customer, room_four, check_in_date, check_out_date5)

        self.assertTrue(room_one.get_is_reserved())
        self.assertEqual(3, len(reservation_service.search_for_available_rooms(check_in_date,
                                                                               check_out_date1)))
        # print(reservation_service.search_for_available_rooms(check_in_date, check_out_date))

    # def setUp(self) -> None:
    #     self.reservation_service = ReservationServiceImpl()
    #     self.check_in_date: date = date.today()
    #     self.check_out_date: date = date(2023, 5, 1)
    #     self.first_room = Room()
    #     self.first_room.set_room_type(RoomType.SINGLE)
    #     self.room_service = RoomServiceImpl()
    #     self.room_service.add_room(self.first_room)
    #     self.first_customer = Customer("John", "Doe", "johndoe@gmail.com")
    #     self.reservation_service.reserve_a_room(self.first_customer, self.first_room, self.check_in_date,
    #                                             self.check_out_date)
    #
    # def test_when_add_room_in_reservation_room_id_increment(self):
    #     self.assertEqual(1, self.reservation_service.get_last_id_generated())
    #
    # def test_when_add_room_in_reservation_room_has_a_number(self):
    #     self.assertEqual(1, self.first_room.get_room_number())
    #
    # def test_when_add_room_in_reservation_length_of_room_increase(self):
    #     self.room_service.add_room(self.first_room)
    #     self.assertEqual(2, self.reservation_service.get_length_of_rooms())
    #
    # def test_get_room_with_id_returns_room(self):
    #     second_room = Room()
    #     third_room = Room()
    #     self.room_service.add_room(third_room)
    #     self.room_service.add_room(second_room)
    #     self.assertEqual(third_room, self.room_service.get_room(2))
    #
    # def test_get_room_with_id_and_room_not_found_raise_RoomNotFound(self):
    #     second_room = Room()
    #     third_room = Room()
    #     self.room_service.add_room(third_room)
    #     self.room_service.add_room(second_room)
    #     with self.assertRaises(RoomNotFound):
    #         self.room_service.get_room(4)
    #
    # def test_add_multiple_rooms(self):
    #     for _ in range(9):
    #         self.room_service.add_room(self.first_room)
    #     self.assertEqual(10,
    #     self.reservation_service.get_length_of_rooms(),
    #     msg="Just trying out loop on '.add_room' ")
    #
    # def test_that_when_room_is_reserved_get_is_reserved_is_true(self):
    #     self.assertTrue(self.first_room.is_reserved(), msg="Reserve a room, set is room reserved to true")
    #
    # def test_that_when_customer_day_elapses_room_becomes_unreserved(self):
    #     self.assertTrue(self.first_room.is_reserved())
    #     add_to_check_in_date: timedelta = timedelta(2)
    #     self.check_in_date += add_to_check_in_date
    #     self.first_room.set_check_in_date(self.check_in_date)
    #     print(self.check_in_date)
    #     print(self.check_out_date)
    #     self.assertFalse(self.first_room.is_reserved())
    #
    # def test_that_if_room_is_reserved_is_true_room_is_not_available_for_reservation(self):
    #     self.assertTrue(self.first_room.is_reserved())
    #     with self.assertRaises(RoomNotAvailableForReservation):
    #         self.reservation_service.reserve_a_room(self.first_customer,
    #                                                 self.first_room,
    #                                                 self.check_in_date,
    #                                                 self.check_out_date)
    #
    # def test_that_if_room_is_reserved_suggest_other_free_rooms(self):
    #     second_check_in = date(2023, 4, 26)
    #     second_check_out = date(2023, 4, 29)
    #     second_room = Room(check_in_date=second_check_in, check_out_date=second_check_out)
    #     self.room_service.add_room(second_room)
