import abc

from data.model.Room import Room


class IRoom(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def save(self, room: Room) -> Room:
        pass

    @abc.abstractmethod
    def find_by_id(self, room_id: int) -> Room:
        pass

    @abc.abstractmethod
    def get_all_rooms(self) -> list[Room]:
        pass

    # @abc.abstractmethod
    # def get_room_number(self) -> int:
    #     pass
    #
    # @abc.abstractmethod
    # def get_room_price(self) -> int:
    #     pass
    #
    # @abc.abstractmethod
    # def get_room_type(self) -> RoomType:
    #     pass
    #
    # @abc.abstractmethod
    # def is_reserved(self):
    #     pass
