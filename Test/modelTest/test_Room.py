from unittest import TestCase

from model.RoomType import RoomType
from model.Room import Room, InvalidRoomType


class TestRoom(TestCase):

    def test_that_room_not_null(self):
        room = Room(True, 13)
        self.assertIsNotNone(room)

    def test_that_room_isnone(self):
        room = Room(True, 13)
        self.assertEqual(RoomType.NULL, room.get_room_type())

    def test_that_room_isSingle_when_set_toSingle(self):
        room = Room(True, 13)
        room.set_room_type(RoomType.SINGLE)
        self.assertEqual(RoomType.SINGLE, room.get_room_type())

    def test_that_room_cannot_be_setToNULL_raiseInvalidRoomTypeException(self):
        room = Room(True, 13)
        with self.assertRaises(InvalidRoomType):
            room.set_room_type(RoomType.NULL)
