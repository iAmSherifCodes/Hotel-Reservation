from datetime import date, timedelta

from multipledispatch import dispatch

from Utils.Exceptions.RoomNotAvailableForReservation import RoomNotAvailableForReservation
from data.Repository import ReservationRepository
from data.Repository.ReservationRepositoryImpl import ReservationRepositoryImpl
from data.Repository.ReservationRepositoryImpl import ReservationRepositoryImpl
#
from data.model.Customer import Customer
from data.model.Reservation import Reservation
from data.model.Room import Room
from dto.Request.FindRoomsRequest import FindRoomRequest
from dto.Response.FindRoomResponse import FindRoomResponse
from service.IReservationService import IReservationService
from service.IRoom import IRoom
from service.RoomServiceImpl import RoomServiceImpl


class ReservationServiceImpl(IReservationService):
    _reservation_repository: ReservationRepository = ReservationRepositoryImpl()
    _rooms: IRoom = RoomServiceImpl()

    def __init__(self):
        pass

    def reserve_a_room(self, customer: Customer, room: Room, check_in_date: date,
                       check_out_date: date):
        if not room.get_is_reserved():
            room.set_is_reserved(True)
            reservation: Reservation = Reservation()
            reservation.set_who_to_reserve(customer)
            reservation.set_room_to_reserve(room)
            reservation.set_check_in_date(check_in_date)
            reservation.set_check_out_date(check_out_date)
            self._reservation_repository.save(reservation)
        else:
            raise RoomNotAvailableForReservation

    def search_for_available_rooms(self, check_in, check_out) -> list[Room]:
        available_rooms: list[Room] = []
        for room in self._rooms.get_all_rooms():
            if not room.get_is_reserved():
                available_rooms.append(room)

        if len(available_rooms) == 0:
            add_two_days = timedelta(2)
            check_in += add_two_days
            for reservation in self._reservation_repository.get_all_reservations():
                if reservation.get_check_out_date() < check_in:
                    available_rooms.append(reservation.get_reserved_room())
        print(available_rooms)

        return available_rooms

    # TODO
    #   Search for recommended rooms. If there are no available rooms for the
    #   customer's date range, a search will be performed that displays recommended
    #   rooms on alternative dates. The recommended room search will add seven days to
    #   the original check-in and check-out dates to see if the hotel has any availabilities
    #   and then display the recommended rooms/dates to the customer.

    def find_reservations_by_customer_email(self, customer_email: str) -> list[Reservation]:
        customer_reserves = []
        for reservation in self._reservation_repository.get_all_reservations():
            if reservation.get_who_reserved_room().get_email() == customer_email:
                customer_reserves.append(reservation)
        return customer_reserves

    def display_reservations(self) -> list[Reservation]:
        return self._reservation_repository.get_all_reservations()

    def find_reservation_by_id(self, reservation_id: int) -> Reservation | None:
        for reservation in self._reservation_repository.get_all_reservations():
            if reservation.get_reservation_id() == reservation_id:
                return reservation
        return None
#
#
