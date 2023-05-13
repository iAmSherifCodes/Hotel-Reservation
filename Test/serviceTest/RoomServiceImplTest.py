from unittest import TestCase

from Utils.Exceptions.RoomNotFound import RoomNotFound
from data.model.Room import Room
from service.IRoom import IRoom
from service.RoomServiceImpl import RoomServiceImpl


class Test(TestCase):
    def setUp(self) -> None:
        self.room_service = RoomServiceImpl()

    def test_that_room_service_impl_not_none(self):
        room_service: IRoom = RoomServiceImpl()
        self.assertIsNotNone(room_service)

    def test_that_when_we_add_room_can_get_room_with_room_number(self):
        room1 = Room()
        room1.set_room_type("single")
        room2 = Room()
        room2.set_room_type("double")
        room3 = Room()
        room3.set_room_type("exclusive")
        self.room_service.add_room(room3)
        self.room_service.add_room(room2)
        self.room_service.add_room(room1)
        print(room1)
        print(self.room_service.get_room(1))
        self.assertEqual(room1, self.room_service.get_room(3))

    def test_room_not_found_raise_exception(self):
        room1 = Room()
        room1.set_room_type("single")
        room2 = Room()
        room2.set_room_type("double")
        room3 = Room()
        room3.set_room_type("exclusive")
        self.room_service.add_room(room3)
        self.room_service.add_room(room2)
        with self.assertRaises(RoomNotFound):
            self.room_service.get_room(3)

