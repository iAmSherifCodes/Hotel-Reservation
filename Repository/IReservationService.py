import abc

from model.Room import Room


class IReservationService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_room(self, room) -> list[Room]:
        pass

    @abc.abstractmethod
    def get_room(self, room_id) -> Room:
        pass

    @abc.abstractmethod
    def reserve_a_room(self, customer, room, check_in_date, check_out_date):
        pass

    @abc.abstractmethod
    def find_rooms(self, check_in_date, check_out_date):
        pass

    @abc.abstractmethod
    def get_customers_reservation(self, customer):
        pass

    @abc.abstractmethod
    def print_reservation(self):
        pass
