from datetime import datetime
from typing import Any

from dto.Customer import Customer
from dto.Room import Room
from Repository.IReservationService import IReservationService


class ReservationService(IReservationService):

    def __init__(self):
        self.rooms = []
        self.last_room_number_generated = 0

    def add_room(self, room: Room):
        room.set_room_number(self.last_room_number_generated + 1)
        self.last_room_number_generated += 1
        self.rooms.append(room)

    def get_room(self, room_id: int) -> Room | None:
        for room in self.rooms:
            if room.get_room_number() == room_id:
                return room
        for room in self.rooms:
            if room.get_room_number() != room_id:
                return None

    def reserve_a_room(self, customer: Customer, room: Room, check_in_date: datetime, check_out_date: datetime):
        if room in self.rooms:
            room.set_is_reserved(True)
            if check_in_date == check_out_date:
                room.set_is_reserved(False)



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
