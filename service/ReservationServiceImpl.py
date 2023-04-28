from datetime import date

from dto.createNewCustomerRequest.Customer import Customer
from data.model.Room import Room
from service.IReservationService import IReservationService


class RoomNotFound(Exception):
    def __str__(self):
        return "Room Not found"


class RoomNotAvailableForReservation(Exception):
    def __str__(self):
        return "Room Not Available For Reservation"


class ReservationService(IReservationService):

    def __init__(self):
        self.rooms = []
        self.last_room_number_generated = 0

    def add_room(self, room: Room):
        room.set_room_number(self.last_room_number_generated + 1)
        self.last_room_number_generated += 1
        self.rooms.append(room)

    def get_room(self, room_id: int) -> Room:
        for room in self.rooms:
            if room.get_room_number() == room_id:
                return room
        raise RoomNotFound()

    @staticmethod
    def _room_is_found(x: Room, y: Room) -> bool:
        return x == y

    @staticmethod
    def _set_room_availability(room: Room):
        if not room.is_reserved():
            room.set_is_reserved(True)
        else:
            raise RoomNotAvailableForReservation()

    def reserve_a_room(self, customer: Customer, room: Room, check_in_date: date, check_out_date: date):
        for _ in self.rooms:
            if self._room_is_found(_, room):
                self._set_room_availability(room)
            # else:
        # raise RoomNotAvailableForReservation

    def find_rooms(self, check_in_date, check_out_date):
        pass

    def get_customers_reservation(self, customer):
        pass

    def print_reservation(self):
        pass

    def get_last_id_generated(self):
        return self.last_room_number_generated

    def get_length_of_rooms(self) -> int:
        return len(self.rooms)

    def get_all_rooms(self) -> list[Room]:
        return self.rooms


# ToDo
#  - Look to refactor the logic in service layer
