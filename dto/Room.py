from datetime import date

from multipledispatch import dispatch

from dto.IRoom import IRoom

from dto.RoomType import RoomType


class Room(IRoom):

    def __init__(self, check_in_date: date = date(1, 1, 1), check_out_date: date = date(2, 1, 1),
                 room_type: RoomType = RoomType.NULL):
        self._check_in_date: date = check_in_date
        self._check_out_date: date = check_out_date
        self._price: int = 0
        self._room_number: int = 0
        self._room_id: str = "ROOM " + str(self.get_room_number())
        self._room_type: RoomType = room_type
        self._is_reserved: bool = False

    @dispatch(int, int, int)
    def set_check_in_date(self, year: int, month: int, day: int) -> None:
        self._check_in_date = date(year, month, day)

    @dispatch(date)
    def set_check_in_date(self, new_date: date) -> None:
        self._check_in_date = new_date

    @dispatch(int, int, int)
    def set_check_out_date(self, year: int, month: int, day: int) -> None:
        self._check_out_date = date(year, month, day)

    @dispatch(date)
    def set_check_out_date(self, new_date: date) -> None:
        self._check_out_date = new_date

    def get_check_in_date(self) -> date:
        return self._check_in_date

    def get_check_out_date(self) -> date:
        return self._check_out_date

    def get_room_id(self) -> str:
        return "ROOM " + str(self.get_room_number())

    def get_room_type(self) -> RoomType:
        return self._room_type

    def _is_room_single(self) -> bool:
        return self.get_room_type() == RoomType.SINGLE

    def _is_room_double(self) -> bool:
        return self.get_room_type() == RoomType.DOUBLE

    def _is_room_exclusive(self) -> bool:
        return self.get_room_type() == RoomType.EXCLUSIVE

    def room_price(self):
        # To make method return <class 'int'> from Enum.value
        # Got Error -> Expected type 'int', got '() -> Any | () -> Any' instead
        if self._is_room_single():
            self._price = RoomType.SINGLE.value
        if self._is_room_double():
            self._price = RoomType.DOUBLE.value
        if self._is_room_exclusive():
            self._price = RoomType.EXCLUSIVE.value

        return self._price

    def get_room_number(self) -> int:
        return self._room_number

    def is_reserved(self) -> bool:
        if self.get_check_in_date() == self.get_check_out_date():
            return not self._is_reserved
        return self._is_reserved

    def set_is_reserved(self, room_status: bool) -> None:
        self._is_reserved = room_status

    def set_room_type(self, room_type: RoomType) -> None:
        if room_type in RoomType and room_type != RoomType.NULL:
            self._room_type = room_type
        else:
            raise InvalidRoomType

    def set_room_price(self) -> int:
        return self._price

    def set_room_number(self, room_id: int) -> None:
        self._room_number = room_id

    def __repr__(self):
        return f"""
        --- {self.get_room_id()} ---
        Price : {self.room_price()}
        Room ID : {self.get_room_id()}
        Room Type : {self.get_room_type()}
        Check In Date : {self.get_check_in_date()}
        Check Out Date : {self.get_check_out_date()}
        Room Availability : {not self._is_reserved}
        """


class InvalidRoomType(Exception):
    def __repr__(self):
        return "Invalid Room Type"
    # def __str__(self):
    #     return f"""
    #     ---ROOM---
    #     Price : {self.get_room_price()}
    #     Room Number : {self.get_room_number()}
    #     Room Type : {self.get_room_type()}
    #     IS ROOM FREE : {self.is_free}
    #     """
