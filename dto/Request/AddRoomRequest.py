from data.model.RoomType import RoomType


class AddRoomRequest:
    def __init__(self):
        self._price: int = 0
        self._room_type: str = ""

    def get_price(self) -> int:
        return self._price

    def set_price(self, price: int) -> None:
        self._price = price

    def get_room_type(self) -> str:
        return self._room_type

    def set_room_type(self, room_type: str) -> None:
        self._room_type = room_type
