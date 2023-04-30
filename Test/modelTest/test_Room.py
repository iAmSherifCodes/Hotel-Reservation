from datetime import date
from unittest import TestCase

from data.model.RoomType import RoomType
from data.model.Room import Room, InvalidRoomType


class TestRoom(TestCase):

    def setUp(self) -> None:
        self.room = Room()

    def test_that_room_not_null(self):
        self.assertIsNotNone(self.room)

    def test_that_room_isnone(self):
        self.assertEqual(RoomType.NULL, self.room.get_room_type())

    def test_that_room_isSingle_when_set_toSingle(self):
        self.room.set_room_type("SINGLE")
        self.assertEqual(RoomType.SINGLE, self.room.get_room_type())

    def test_that_room_cannot_be_setToNULL_raiseInvalidRoomTypeException(self):
        with self.assertRaises(InvalidRoomType):
            self.room.set_room_type("NULL")

    def test_room_Single_room_price_is_10(self):
        self.room.set_room_type("SINGLE")
        self.assertEqual(10, self.room.get_room_price())

    def test_room_Double_room_price_is_20(self):
        self.room.set_room_type("DOUBLE")
        self.assertEqual(20, self.room.get_room_price())

    def test_room_Exclusive_room_price_is_50(self):
        self.room.set_room_type("EXCLUSIVE")
        self.assertEqual(50, self.room.get_room_price())

    # def test_set_check_in_date(self):
    #     self.room.set_check_in_date(2020, 9, 9)
    #     new_date: date = date(2020, 9, 9)
    #     self.assertEqual(new_date, self.room.get_check_in_date())
    #
    # def test_set_check_out_date(self):
    #     self.room.set_check_out_date(2020, 9, 15)
    #     new_date: date = date(2020, 9, 15)
    #     self.assertEqual(new_date, self.room.get_check_out_date())
