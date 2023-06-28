from Utils.Exceptions.RoomNotFound import RoomNotFound
from data.Repository.RoomRepository import RoomRepository
from data.Repository.RoomRepositoryImpl import RoomRepositoryImpl
from data.model.Room import Room
from dto.Request.AddRoomRequest import AddRoomRequest
from dto.Response.AddRoomResponse import AddRoomResponse
from service.IRoom import IRoom


class RoomServiceImpl(IRoom):

    def __init__(self):
        self._room_repository: RoomRepository = RoomRepositoryImpl()

    def add_room(self, request: AddRoomRequest) -> AddRoomResponse:
        room: Room = Room()
        room.set_room_type(request.get_room_type())

        saved_room: Room = self._room_repository.save(room)

        response = AddRoomResponse()

        response.set_room_type(saved_room.get_room_type())


        return self._room_repository.save(room)

    def get_room_by_id(self, room_id: str) -> Room:
        response = self._search_for_room_in_repository(room_id=room_id)
        found_room = response is not None
        if found_room: return response
        raise RoomNotFound()

    def _search_for_room_in_repository(self, room_id: str) -> Room | None:
        for room in self._room_repository.get_all_rooms():
            if room.get_room_id() == room_id:
                return room
        return None

    def get_all_rooms(self) -> list[Room]:
        return self._room_repository.get_all_rooms()
