from data.model.Room import Room


class FreeRoom(Room):

    def __init__(self):
        super().__init__()
        self._price = 0

    def set_room_price(self) -> None:
        self._price = 0

    def get_room_price(self) -> int:
        return self._price

    def __str__(self):
        return f"""
        ---FREE ROOM---
        Price : {self.get_room_price()}
        Room Number : {self.get_room_number}
        Is Reserved : {self.is_reserved()}
        """
