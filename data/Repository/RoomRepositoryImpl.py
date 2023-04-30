# ToDo
#  - write the logic for Room Repo
from data.Repository.RoomRepository import RoomRepository
from data.model.Room import Room
from service.ReservationServiceImpl import RoomNotFound


class RoomRepositoryImpl(RoomRepository):
    def __init__(self):
        self.rooms = []
        self.last_room_number_generated = 0

    def save(self, room: Room):
        room.set_room_number(self.last_room_number_generated + 1)
        self.rooms.append(room)
        self.last_room_number_generated += 1

    def find_by_id(self, room_id: int) -> Room:
        for room in self.rooms:
            if room.get_room_number() == room_id:
                return room
        raise RoomNotFound

    def get_all_rooms(self) -> list[Room]:
        return self.rooms
