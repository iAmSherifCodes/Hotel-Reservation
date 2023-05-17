from Utils.AppUtils import AppUtils
from data.Repository.RoomRepository import RoomRepository
from data.model.Room import Room


# TODO
#  REFACTOR THE IDS OF EACH REPOSITORY WITH THEIR TEST


class RoomRepositoryImpl(RoomRepository):
    def __init__(self):
        self._rooms = []

    def save(self, room: Room) -> Room:
        room.set_room_id(str(AppUtils.generate_id()))
        self._rooms.append(room)
        return room

    def find_by_id(self, room_id: str) -> Room | None:
        for room in self._rooms:
            if room.get_room_id() == room_id:
                return room
        return None

    def get_all_rooms(self) -> list[Room]:
        return self._rooms

    def length_of_rooms(self):
        return len(self._rooms)
