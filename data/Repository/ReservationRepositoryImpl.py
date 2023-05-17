# ToDo
#  - write the logic for reservation Repo

from multipledispatch import dispatch
from Utils.AppUtils import AppUtils
from data.Repository.CustomerRepositoryImpl import CustomerRepositoryImpl
from data.Repository.ReservationRepository import ReservationRepository
from data.Repository.RoomRepositoryImpl import RoomRepositoryImpl
from data.model.Customer import Customer
from data.model.Reservation import Reservation
from data.model.Room import Room


class NoReservationFound(Exception):
    def __str__(self):
        return "No Reservation Found"


class ReservationRepositoryImpl(ReservationRepository):
    def __init__(self):
        self._reservations: list[dict] = []
        self._rooms = RoomRepositoryImpl()
        self._customers = CustomerRepositoryImpl()
        # self._reservation_id: int = AppUtils.generate_id()  # 0

    def save(self, reservation: Reservation) -> Reservation:
        # for room in self._rooms.get_all_rooms():
        #     if room.get_room_id() == reservation.get_reserved_room().get_room_id():
        #         if not room.get_is_reserved():
        #             self._rooms.save(reservation.get_reserved_room())
        #         else:
        #             raise RoomNotAvailableForReservation()

        new_reserve = self._save_who_reserve_room(reservation)

        # set_of_reservation = self._save_reservation(reservation)
        self._reservations.append(new_reserve)
        return new_reserve

    def _save_reservation(self, reservation):
        return {
            "reservation_id": reservation.set_reservation_id(AppUtils.generate_id()),
            "check-in-date": reservation.get_check_in_date(),
            "check-out-date": reservation.get_check_out_date(),
            "customer": reservation.get_who_reserved_room(),
            "room": reservation.get_reserved_room(),
        }

    def _save_who_reserve_room(self, reservation):
        self._customers.save(reservation.get_who_reserved_room())

    # def delete(self, reservation_to_delete: Reservation) -> None:
    #     self._delete_reservation(reservation_to_delete)
    # raise NoReservationFound

    def delete_by_id(self, reservation_id: int) -> None:
        for reservation in self._reservations:
            if reservation["reservation_id"] == reservation_id:
                self._reservations.remove(reservation)
                # self._reservations.remove(reservation)
        # self._reservations.remove(self.find_by_id(reservation_id))
        # for reservation in self.reservations:
        #     if reservation.get_reservation_id() == reservation_id:
        #         self.reservations.remove(reservation)
        # raise NoReservationFound

    #
    # @dispatch(Reservation)
    # def _delete_reservation(self, reservation_to_delete: Reservation):
    #     for reservation_set in self._reservations:
    #         if reservation_set == reservation_to_delete:
    #             self._reservations.remove(reservation_set)

    @dispatch(int)
    def _delete_reservation(self, reservation_id: int):
        self._reservations.remove(self.find_by_id(reservation_id))

    def find_by_id(self, reservation_id: int) -> dict:
        for reservation in self._reservations:
            if reservation["reservation_id"] == reservation_id:
                return reservation
        # raise NoReservationFound

    def get_all_reservations(self) -> list[dict]:
        return self._reservations

    def get_number_of_all_reservations(self) -> int:
        return len(self._reservations)
