from model.IRoom import IRoom
from model.RoomType import RoomType


class Room(IRoom):

    def __init__(self, is_free: bool, price: int):
        self.price = price
        self.room_number = 0
        self.room_type = RoomType.NULL
        self.is_free = is_free

    def get_room_type(self) -> RoomType:
        return self.room_type

    def get_room_price(self) -> int:
        return self.price

    def get_room_number(self) -> int:
        return self.room_number

    def get_is_free(self) -> bool:
        return self.is_free

    def set_room_type(self, room_type: RoomType) -> None:
        if room_type in RoomType and room_type != RoomType.NULL:
            self.room_type = room_type
        else:
            raise InvalidRoomType

    def set_room_price(self) -> int:
        return self.price

    def set_room_number(self, room_id: int) -> None:
        self.room_number = room_id

    def set_is_room_free(self, is_room_free: bool) -> None:
        self.is_free = is_room_free

    def __repr__(self):
        return f"""
        ---ROOM RE---
        Price : {self.get_room_price()}
        Room Number : {self.get_room_number}
        Room Type : {self.get_room_type()}
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
