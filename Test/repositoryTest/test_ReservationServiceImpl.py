from datetime import timedelta, date
from unittest import TestCase
from data.Repository import ReservationService, RoomNotAvailableForReservation, RoomNotFound
from dto.createNewCustomerRequest.Customer import Customer
from dto.Room import Room


class Test(TestCase):

    def setUp(self) -> None:
        self.check_in_date: date = date.today()
        self.check_out_date: date = date(2023, 5, 1)
        self.first_room = Room(check_in_date=self.check_in_date, check_out_date=self.check_out_date)
        self.room_service = ReservationService()
        self.room_service.add_room(self.first_room)
        self.first_customer = Customer("John", "Doe", "johndoe@gmail.com")
        self.room_service.reserve_a_room(self.first_customer, self.first_room, self.check_in_date, self.check_out_date)

    def test_when_add_room_in_reservation_room_id_increment(self):
        self.assertEqual(1, self.room_service.get_last_id_generated())

    def test_when_add_room_in_reservation_room_has_a_number(self):
        self.assertEqual(1, self.first_room.get_room_number())

    def test_when_add_room_in_reservation_length_of_room_increase(self):
        self.room_service.add_room(self.first_room)
        self.assertEqual(2, self.room_service.get_length_of_rooms())

    def test_get_room_with_id_returns_room(self):
        second_room = Room()
        third_room = Room()
        self.room_service.add_room(third_room)
        self.room_service.add_room(second_room)
        self.assertEqual(third_room, self.room_service.get_room(2))

    def test_get_room_with_id_and_room_not_found_raise_RoomNotFound(self):
        second_room = Room()
        third_room = Room()
        self.room_service.add_room(third_room)
        self.room_service.add_room(second_room)
        with self.assertRaises(RoomNotFound):
            self.room_service.get_room(4)

    def test_add_multiple_rooms(self):
        for _ in range(9):
            self.room_service.add_room(self.first_room)
        self.assertEqual(10, self.room_service.get_length_of_rooms(), msg="Just trying out loop on '.add_room' ")

    def test_that_when_room_is_reserved_get_is_reserved_is_true(self):
        self.assertTrue(self.first_room.is_reserved(), msg="Reserve a room, set is room reserved to true")

    def test_that_when_customer_day_elapses_room_becomes_unreserved(self):
        self.assertTrue(self.first_room.is_reserved())
        add_to_check_in_date: timedelta = timedelta(4)
        self.check_in_date += add_to_check_in_date
        self.first_room.set_check_in_date(self.check_in_date)
        print(self.check_in_date)
        print(self.check_out_date)
        self.assertFalse(self.first_room.is_reserved())

    def test_that_if_room_is_reserved_is_true_room_is_not_available_for_reservation(self):
        self.assertTrue(self.first_room.is_reserved())
        with self.assertRaises(RoomNotAvailableForReservation):
            self.room_service.reserve_a_room(self.first_customer,
                                             self.first_room,
                                             self.check_in_date,
                                             self.check_out_date)

    def test_that_if_room_is_reserved_suggest_other_free_rooms(self):
        second_check_in = date(2023, 4, 26)
        second_check_out = date(2023, 4, 29)
        second_room = Room(check_in_date=second_check_in, check_out_date=second_check_out)
        self.room_service.add_room(second_room)
        