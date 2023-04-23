from enum import property

from dto.IRoom import IRoom

from dto.RoomType import RoomType


class Room(IRoom):

    def __init__(self, is_free: bool, room_type: RoomType = RoomType.NULL):
        self._price: int = 0
        self._room_number: int = 0
        self._room_id: str = "ROOM-" + str(self.get_room_number())
        self._room_type: RoomType = room_type
        self._is_free: bool = is_free

    def get_room_id(self) -> str:
        return self._room_id

    def get_room_type(self) -> RoomType:
        return self._room_type

    def room_price(self):
        if self.get_room_type() == RoomType.SINGLE:
            self._price = RoomType.SINGLE.value

        return self._price

    def get_room_number(self) -> int:
        return self._room_number

    def get_is_free(self) -> bool:
        return self._is_free

    def set_room_type(self, room_type: RoomType) -> None:
        if room_type in RoomType and room_type != RoomType.NULL:
            self._room_type = room_type
        else:
            raise InvalidRoomType

    def set_room_price(self) -> int:
        return self._price

    def set_room_number(self, room_id: int) -> None:
        self._room_number = room_id

    def set_is_room_free(self, is_room_free: bool) -> None:
        self._is_free = is_room_free

    def __repr__(self):
        return f"""
        ---ROOM RE---
        Price : {self.room_price()}
        Room ID : {self.get_room_id()}
        Room Type : {self.get_room_type()}
        Room Availability : {self._is_free}
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
