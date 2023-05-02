from data.Repository.RoomRepository import RoomRepository
from data.model.Room import Room


class RoomNotFound(Exception):
    def __str__(self):
        return "Room Not found"


class RoomRepositoryImpl(RoomRepository):
    def __init__(self):
        self._rooms = []
        self._last_room_number_generated = 0

    def save(self, room: Room):
        room.set_room_number(self._last_room_number_generated + 1)
        self._rooms.append(room)
        self._last_room_number_generated += 1

    def find_by_id(self, room_id: int) -> Room:
        for room in self._rooms:
            if room.get_room_number() == room_id:
                return room
        raise RoomNotFound

    def get_all_rooms(self) -> list[Room]:
        return self._rooms
