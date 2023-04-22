import abc

from model.RoomType import RoomType


class IRoom(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_room_number(self) -> int:
        pass

    @abc.abstractmethod
    def get_room_price(self) -> int:
        pass

    @abc.abstractmethod
    def get_room_type(self) -> RoomType:
        pass

    @abc.abstractmethod
    def get_is_free(self):
        pass
