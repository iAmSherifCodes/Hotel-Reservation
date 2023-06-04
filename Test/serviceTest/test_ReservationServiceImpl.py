from datetime import timedelta, date
from unittest import TestCase

from Utils.Exceptions.RoomNotAvailableForReservation import RoomNotAvailableForReservation
from data.model.Customer import Customer
from data.model.Room import Room
from dto.Request.FindReservationByCustomerEmailRequest import FindReservationByCustomerEmailRequest
from dto.Request.FindReservationByIdRequest import FindReservationByIdRequest
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
        first_reserve = reservation_service.reserve_a_room(customer, room_one, check_in_date, check_out_date1)
        reservation_service.reserve_a_room(customer, room_two, check_in_date, check_out_date2)
        reservation_service.reserve_a_room(customer, room_three, check_in_date, check_out_date3)
        reservation_service.reserve_a_room(customer, room_five, check_in_date, check_out_date4)
        reservation_service.reserve_a_room(customer, room_four, check_in_date, check_out_date5)

        self.assertTrue(room_one.get_is_reserved())
        self.assertEqual(7, len(reservation_service.search_for_available_rooms(check_in_date,
                                                                               check_out_date1)))

        # Find reservation by id
        email_request: FindReservationByIdRequest = FindReservationByIdRequest()
        email_request.set_id(first_reserve.get_reservation_id())
        response = reservation_service.find_reservation_by_id(email_request)

        # print(response.get_reservation())

        # Find reservation by customer email
        customer_request: FindReservationByCustomerEmailRequest = FindReservationByCustomerEmailRequest()
        customer_request.set_customer_email(customer.get_email())
        response = reservation_service.find_reservations_by_customer_email(customer_request)
        print(response)