from datetime import datetime
from unittest import TestCase
from Repository.ReservationServiceImpl import ReservationService
from dto.Customer import Customer
from dto.Room import Room


class Test(TestCase):

    def setUp(self) -> None:
        self.new_room = Room()
        self.room_service = ReservationService()
        self.room_service.add_room(self.new_room)
        self.first_customer = Customer("John", "Doe", "johndoe@gmail.com")

    def test_when_add_room_in_reservation_room_id_increment(self):
        self.assertEqual(1, self.room_service.get_last_id_generated())

    def test_when_add_room_in_reservation_room_has_a_number(self):
        self.assertEqual(1, self.new_room.get_room_number())

    def test_when_add_room_in_reservation_length_of_room_increase(self):
        self.room_service.add_room(self.new_room)
        self.assertEqual(2, self.room_service.get_length_of_rooms())

    def test_get_room_with_id_returns_room(self):
        second_room = Room()
        third_room = Room()
        self.room_service.add_room(third_room)
        self.room_service.add_room(second_room)
        self.assertEqual(third_room, self.room_service.get_room(2))

    def test_get_room_with_id_and_room_not_found_return_None(self):
        second_room = Room()
        third_room = Room()
        self.room_service.add_room(third_room)
        self.room_service.add_room(second_room)
        self.assertEqual(None, self.room_service.get_room(4), msg="Return None when room not found")

    def test_add_multiple_rooms(self):
        for _ in range(9):
            self.room_service.add_room(self.new_room)
        self.assertEqual(10, self.room_service.get_length_of_rooms(), msg="Just trying out loop on '.add_room' ")

    def test_that_when_room_is_reserved_get_is_reserved_is_true(self):
        check_in_date: datetime = datetime(2020, 5, 15)
        check_out_date: datetime = datetime(2020, 5, 20)
        customer_reserve_day = check_out_date - check_in_date
        self.room_service.reserve_a_room(self.first_customer, self.new_room, check_in_date, check_out_date)
        self.assertTrue(self.new_room.get_is_free())
