from datetime import date, timedelta

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


class NoRoomFound(Exception):
    def __repr__(self):
        return "No Room Found"


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

    def _conflict_reservation(self) -> bool:
        for _ in self.reservation_repository.get_all_reservations():
            if _.get_reserved_room().get_is_reserved():
                return True

    def _add_seven_days_to_user_check_in(self, check_in_date, check_out_date):
        return self.search_for_available_rooms(check_in_date + timedelta(days=7), check_out_date + timedelta(days=4))

    def _no_rooms_available_for_date_range(self, check_in, check_out) -> int:
        return len(self.search_for_available_rooms(check_in, check_out)) == 0

    @staticmethod
    def _set_reservation(customer: Customer, room: Room, check_in_date: date, check_out_date: date) -> Reservation:
        new_reservation: Reservation = Reservation()
        new_reservation.set_room_to_reserve(room)
        new_reservation.set_who_to_reserve(customer)
        new_reservation.set_check_in_date(check_in_date)
        new_reservation.set_check_out_date(check_out_date)
        return new_reservation

    def reserve_a_room(self, customer: Customer, room: Room, check_in_date: date, check_out_date: date):
        if self._reservation_exist(room) and self._conflict_reservation():
            if self._no_rooms_available_for_date_range(check_in_date, check_out_date):
                return self._add_seven_days_to_user_check_in(check_in_date, check_out_date)


        self.reservation_repository.save(self._set_reservation(customer, room, check_in_date, check_out_date))

    @dispatch(date, date)
    def search_for_available_rooms(self, check_in: date, check_out: date):
        available_rooms: list[Room] = []
        for reservation in self.reservation_repository.get_all_reservations():
            if not (reservation.get_check_in_date() == check_in and reservation.get_check_out_date() == check_out):
                available_rooms.append(reservation.get_reserved_room())
        return available_rooms

    def find_rooms(self, check_in_date, check_out_date):
        pass

    def get_customers_reservation(self):
        customer_reservations = []
        for reservation in self.reservation_repository.get_all_reservations():
            if reservation.get_reservation_id() < 1:
                customer_reservations.append(reservation)
        return customer_reservations

    def print_reservation(self) -> list[ReservationRepository]:
        return self.reservation_repository.get_all_reservations()

    def _get_last_id_generated(self):
        return self.last_room_number_generated

    def find_reservations_by_customer_email(self, customer_email: str) -> list[Reservation]:
        customer_reserves = []
        for reservation in self.reservation_repository.get_all_reservations():
            if reservation.get_who_reserved_room().get_email() == customer_email: customer_reserves.append(reservation)
        return customer_reserves

    def display_reservations(self) -> list[Reservation]:
        return self.reservation_repository.get_all_reservations()

    def find_reservation_by_id(self, reservation_id: int) -> Reservation:
        for reservation in self.reservation_repository.get_all_reservations():
            if reservation.get_reservation_id() == reservation_id:
                return reservation
            else:
                NoRoomFound()


class RoomNotAvailableForReservation(Exception):
    def __str__(self):
        return "Room Not Available For Reservation"
