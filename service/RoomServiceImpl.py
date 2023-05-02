from data.Repository.RoomRepository import RoomRepository
from data.Repository.RoomRepositoryImpl import RoomRepositoryImpl, RoomNotFound
from data.model.Room import Room
from service.IRoom import IRoom


class RoomServiceImpl(IRoom):

    def __init__(self):
        self._room_repository: RoomRepository = RoomRepositoryImpl()

    def add_room(self, room: Room) -> Room:
        return self._room_repository.save(room)

    def get_room(self, room_id: int) -> Room:
        for room in self._room_repository.get_all_rooms():
            if room.get_room_number() == room_id:
                return room
        raise RoomNotFound()
