from Utils.AppUtils import AppUtils
from Utils.Exceptions.InvalidRoomType import InvalidRoomType
from data.model.RoomType import RoomType


class Room:

    def __init__(self, room_type: RoomType = RoomType.NULL):
        self._price: int = 0
        self._room_id: str = AppUtils.generate_id()
        self._room_type: RoomType = room_type
        self._is_reserved: bool = False

    def get_room_id(self) -> str:
        return self._room_id

    def set_room_id(self, room_id: str) -> None:
        self._room_id = room_id

    def get_room_type(self) -> RoomType:
        return self._room_type

    def _is_room_single(self) -> bool:
        return self.get_room_type() == RoomType.SINGLE

    def _is_room_double(self) -> bool:
        return self.get_room_type() == RoomType.DOUBLE

    def _is_room_exclusive(self) -> bool:
        return self.get_room_type() == RoomType.EXCLUSIVE

    def get_room_price(self):
        # To make method return <class 'int'> from Enum.value
        # Got Error -> Expected type 'int', got '() -> Any | () -> Any' instead
        if self._is_room_single():
            self._price = RoomType.SINGLE.value
        if self._is_room_double():
            self._price = RoomType.DOUBLE.value
        if self._is_room_exclusive():
            self._price = RoomType.EXCLUSIVE.value

        return self._price

    def get_is_reserved(self) -> bool:
        return self._is_reserved

    def set_is_reserved(self, room_status: bool) -> None:
        self._is_reserved = room_status

    def set_room_type(self, room_type: str) -> None:
        if room_type.lower() == "single":
            self._room_type = RoomType.SINGLE
        elif room_type.lower() == "double":
            self._room_type = RoomType.DOUBLE
        elif room_type.lower() == "exclusive":
            self._room_type = RoomType.EXCLUSIVE
        else:
            raise InvalidRoomType

    def _get_room_description(self) -> str:
        if self._room_type == RoomType.SINGLE:
            return "SINGLE ROOM - ONE BED"
        elif self._room_type == RoomType.DOUBLE:
            return "TWO ROOMS - WITH VISITOR PARLOR"
        elif self._room_type == RoomType.EXCLUSIVE:
            return "EXCLUSIVE ROOM - WITH VISITOR PARLOR AND LODGE"

    def __repr__(self):
        return f"""
            --- {self.get_room_id()} ---
            Price : {self.get_room_price()}
            Room ID : {self.get_room_id()}
            Room Type : {self._get_room_description()}
            Room Availability : {not self._is_reserved}
            """

    # def __str__(self):
    #     return f"""
    #     ---ROOM---
    #     Price : {self.get_room_price()}
    #     Room Number : {self.get_room_number()}
    #     Room Type : {self.get_room_type()}
    #     IS ROOM FREE : {self.is_free}
    #     """
