from datetime import datetime, date
from unittest import TestCase

from dto.RoomType import RoomType
from dto.Room import Room, InvalidRoomType


class TestRoom(TestCase):

    def setUp(self) -> None:
        self.room = Room()

    def test_that_room_not_null(self):
        self.assertIsNotNone(self.room)

    def test_that_room_isnone(self):
        self.assertEqual(RoomType.NULL, self.room.get_room_type())

    def test_that_room_isSingle_when_set_toSingle(self):
        self.room.set_room_type(RoomType.SINGLE)
        self.assertEqual(RoomType.SINGLE, self.room.get_room_type())

    def test_that_room_cannot_be_setToNULL_raiseInvalidRoomTypeException(self):
        with self.assertRaises(InvalidRoomType):
            self.room.set_room_type(RoomType.NULL)

    def test_room_Single_room_price_is_10(self):
        self.room.set_room_type(RoomType.SINGLE)
        self.assertEqual(10, self.room.room_price())

    def test_room_Double_room_price_is_20(self):
        self.room.set_room_type(RoomType.DOUBLE)
        self.assertEqual(20, self.room.room_price())

    def test_room_Exclusive_room_price_is_50(self):
        self.room.set_room_type(RoomType.EXCLUSIVE)
        self.assertEqual(50, self.room.room_price())

    def test_set_check_in_date(self):
        self.room.set_check_in_date(2020, 9, 9)
        new_date: datetime = datetime(2020, 9, 9)
        self.assertEqual(new_date.date(), self.room.get_check_in_date())

    def test_set_check_out_date(self):
        self.room.set_check_out_date(2020, 9, 15)
        new_date: datetime = datetime(2020, 9, 15)
        self.assertEqual(new_date.date(), self.room.get_check_out_date())
