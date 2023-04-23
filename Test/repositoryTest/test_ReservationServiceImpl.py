from unittest import TestCase

from Repository.ReservationServiceImpl import ReservationService
from dto.Room import Room


class Test(TestCase):

    def test_when_add_room_in_reservation_room_id_increment(self):
        new_room = Room(True, 10)
        room_service = ReservationService()
        room_service.add_room(new_room)
        self.assertEqual(1, room_service.get_last_id_generated())

    def test_when_add_room_in_reservation_room_has_a_number(self):
        new_room = Room(True, 10)
        room_service = ReservationService()
        room_service.add_room(new_room)
        self.assertEqual(1, new_room.get_room_number())

    def test_when_add_room_in_reservation_length_of_room_increase(self):
        new_room = Room( True, 10)
        room_service = ReservationService()
        room_service.add_room(new_room)
        room_service.add_room(new_room)
        self.assertEqual(2, room_service.get_length_of_rooms())

    def test_get_room_with_id_returns_room(self):
        new_room = Room(True, 10)
        second_room = Room(True, 5)
        third_room = Room(True, 3)
        room_service = ReservationService()
        room_service.add_room(new_room)
        room_service.add_room(third_room)
        room_service.add_room(second_room)
        self.assertEqual(third_room, room_service.get_room(2))

    def test_get_room_with_id_and_room_not_found_return_None(self):
        new_room = Room(True, 10)
        second_room = Room(True, 5)
        third_room = Room(True, 3)
        room_service = ReservationService()
        room_service.add_room(new_room)
        room_service.add_room(third_room)
        room_service.add_room(second_room)
        self.assertEqual(None, room_service.get_room(4))
