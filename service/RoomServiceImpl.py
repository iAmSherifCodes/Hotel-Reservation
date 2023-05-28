from Utils.Exceptions.RoomNotFound import RoomNotFound
from data.Repository.RoomRepository import RoomRepository
from data.Repository.RoomRepositoryImpl import RoomRepositoryImpl
from data.model.Room import Room
from service.IRoom import IRoom


class RoomServiceImpl(IRoom):

    def __init__(self):
        self._room_repository: RoomRepository = RoomRepositoryImpl()

    def add_room(self, room: Room) -> Room:
        return self._room_repository.save(room)

    def get_room_by_id(self, room_id: str) -> Room:
        for room in self._room_repository.get_all_rooms():
            if room.get_room_id() == room_id:
                return room
        raise RoomNotFound()

    def get_all_rooms(self) -> list[Room]:
        return self._room_repository.get_all_rooms()

