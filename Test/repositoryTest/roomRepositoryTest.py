from unittest import TestCase

from data.Repository.RoomRepository import RoomRepository
from data.Repository.RoomRepositoryImpl import RoomRepositoryImpl
from data.model.Room import Room


class Test(TestCase):

    def setUp(self) -> None:
        self.rooms: RoomRepository = RoomRepositoryImpl()
        self.first_room: Room = Room()
        self.first_room.set_room_type("Double")

    def test_save_room(self):
        saved_room = self.rooms.save(self.first_room)
        self.assertIsNotNone(saved_room)

    def test_find_by_id(self):
        saved_first_room = self.rooms.save(self.first_room)
        self.second_room: Room = Room()
        self.second_room.set_room_type("single")
        saved_second_room = self.rooms.save(self.second_room)
        self.assertIsNotNone(self.rooms.find_by_id(saved_second_room.get_room_id()))

    def test_find_by_id_returns_none_object(self):
        saved_first_room = self.rooms.save(self.first_room)
        self.second_room: Room = Room()
        self.second_room.set_room_type("single")
        saved_second_room = self.rooms.save(self.second_room)
        self.assertIsNone(self.rooms.find_by_id(saved_second_room.get_room_id() + "ieo"))


