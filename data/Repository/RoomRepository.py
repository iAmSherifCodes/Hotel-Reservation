import abc

from data.model.Room import Room


class RoomRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def save(self, room: Room) -> Room:
        pass

    @abc.abstractmethod
    def find_by_id(self, room_id: str) -> Room:
        pass

    @abc.abstractmethod
    def get_all_rooms(self) -> list[Room]:
        pass
