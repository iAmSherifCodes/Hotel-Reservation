import abc

from data.model.Room import Room


class IRoom(abc.ABC):
    @abc.abstractmethod
    def add_room(self, room) -> list[Room]:
        pass

    @abc.abstractmethod
    def get_room(self, room_id) -> Room:
        pass

    @abc.abstractmethod
    def find_rooms(self, check_in_date, check_out_date):
        pass
