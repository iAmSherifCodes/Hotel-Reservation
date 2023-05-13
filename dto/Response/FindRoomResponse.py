from data.model.Room import Room


class FindRoomResponse:

    def __init__(self):
        self._message: str | None = None
        self._rooms: list[Room] = []

    def get_message(self) -> str:
        return self._message

    def set_message(self, message):
        self._message = message

    def get_rooms(self) -> list[Room]:
        return self._rooms

    def set_rooms(self, rooms: list[Room]) -> None:
        self._rooms = rooms
