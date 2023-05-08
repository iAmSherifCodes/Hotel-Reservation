from datetime import date

from multipledispatch import dispatch

from data.Repository import ReservationRepository
from data.Repository.ReservationRepositoryImpl import ReservationRepositoryImpl

from data.model.Customer import Customer
from data.model.Reservation import Reservation
from data.model.Room import Room
from service.IReservationService import IReservationService


class NoAvailableRoomForReservation(Exception):
    def __repr__(self):
        return "No Room Available For Reservation"


class RoomIsReserved(Exception):
    def __repr__(self):
        return "Room Is Reserved"


class ReservationServiceImpl(IReservationService):

    def __init__(self):
        self.reservation_repository: ReservationRepository = ReservationRepositoryImpl()
        self.last_room_number_generated = 0

    @staticmethod
    def _room_is_found(x: Room, y: Room) -> bool:
        return x == y

    @staticmethod
    def _set_room_availability(room: Room):
        if not room.get_is_reserved():
            room.set_is_reserved(True)
        else:
            raise RoomNotAvailableForReservation()

    def _reservation_exist(self, room) -> bool:
        status = False
        for _ in self.reservation_repository.get_all_reservations():
            if _.get_reserved_room().get_room_number() == room.get_room_number():
                status = True
        return status

    def reserve_a_room(self, customer: Customer, room: Room, check_in_date: date, check_out_date: date):
        if self._reservation_exist(room):
            pass


    # RoomIsReserved()

        # if self._room_is_found(_, room):
        #     self._set_room_availability(room)
        # else:
        # raise RoomNotAvailableForReservation()
        # tion

    # @dispatch()
    # def search_for_available_rooms(self):
    #     available_rooms: list[Room] = []
    #     for room in self.get_all_rooms():
    #         if not room.get_is_reserved():
    #             available_rooms.append(room)
    #
    #     return available_rooms

    @dispatch(date, date)
    def search_for_available_rooms(self, check_in: date, check_out: date):
        available_rooms: list[Room] = []
        for reservation in self.reservation_repository.get_all_reservations():
            if not reservation.get_check_in_date() == check_in:
                available_rooms.append(reservation.get_reserved_room())

        if len(available_rooms) == 0:
            raise NoAvailableRoomForReservation()
        return available_rooms
        # else:
        # if room.
        # m
        # if self.get_check_in_date() == self.get_check_out_date():
        # return not self._is_reserved

    def find_rooms(self, check_in_date, check_out_date):
        pass

    def get_customers_reservation(self, customer):
        pass

    def print_reservation(self):
        pass

    def get_last_id_generated(self):
        return self.last_room_number_generated

    # def get_length_of_rooms(self) -> int:
    #     return len(self.reservation_repository.get_all_reservations())

    # def get_all_rooms(self) -> list[Room]:
    #     return self.reservation_repository.get_all_rooms()

    def find_reservations_by_customer_first_name(self, customer_email: str) -> list[Reservation]:
        pass

    def display_reservations(self) -> list[Reservation]:
        pass

    def find_reservation_by_id(self, reservation_id: int) -> Reservation:
        pass


class RoomNotAvailableForReservation(Exception):
    def __str__(self):
        return "Room Not Available For Reservation"
