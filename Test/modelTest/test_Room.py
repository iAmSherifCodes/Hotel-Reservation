from unittest import TestCase

from dto.RoomType import RoomType
from dto.Room import Room, InvalidRoomType


class TestRoom(TestCase):

    def test_that_room_not_null(self):
        room = Room(True)
        self.assertIsNotNone(room)

    def test_that_room_isnone(self):
        room = Room(True)
        self.assertEqual(RoomType.NULL, room.get_room_type())

    def test_that_room_isSingle_when_set_toSingle(self):
        room = Room(True)
        room.set_room_type(RoomType.SINGLE)
        self.assertEqual(RoomType.SINGLE, room.get_room_type())

    def test_that_room_cannot_be_setToNULL_raiseInvalidRoomTypeException(self):
        room = Room(True)
        with self.assertRaises(InvalidRoomType):
            room.set_room_type(RoomType.NULL)

    def test_room_Single_room_price_is_10(self):
        room = Room(True)
        room.set_room_type(RoomType.SINGLE)
        print(room.room_price())
        self.assertEqual(10, room.room_price())
