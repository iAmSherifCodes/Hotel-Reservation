from model.IRoom import IRoom
from model.Room import Room
from model.RoomType import RoomType


class FreeRoom(Room):

    def __init__(self, room_number: int, is_free: bool, price: int = 0):
        super().__init__(room_number, is_free, price)
        # self.price = 0
    #     self.room_number = room_number
    #     self.room_type = RoomType.SINGLE
    #     self.is_free = is_free
    #
    # def get_room_number(self) -> int:
    #     return self.room_number
    #
    # def get_room_price(self) -> int:
    #     return self.price
    #
    # def get_room_type(self) -> RoomType:
    #     return self.room_type
    #
    # def is_free(self):
    #     return self.is_free

    def __str__(self):
        return f"""
        ---FREE ROOM---
        Price : {self.get_room_price()}
        Room Number : {self.get_room_number}
        Is free : {self.g}
        """

f  = FreeRoom(12,True)
print(f)