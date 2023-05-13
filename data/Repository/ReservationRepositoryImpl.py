# ToDo
#  - write the logic for reservation Repo
from multipledispatch import dispatch

from Utils.AppUtils import AppUtils
from data.Repository.ReservationRepository import ReservationRepository
from data.model.Reservation import Reservation


class NoReservationFound(Exception):
    def __str__(self):
        return "No Reservation Found"


class ReservationRepositoryImpl(ReservationRepository):
    def __init__(self):
        self._reservations: list[Reservation] = []
        # self._reservation_id: int = AppUtils.generate_id()  # 0

    def save(self, reservation: Reservation) -> Reservation:
        reservation.set_reservation_id(AppUtils.generate_id())
        self._reservations.append(reservation)
        # self._reservation_id += 1
        return reservation

    def delete(self, reservation_to_delete: Reservation) -> None:
        self._get_reservation(reservation_to_delete)
        # raise NoReservationFound

    def delete_by_id(self, reservation_id: int) -> None:
        self._get_reservation(reservation_id)
        # for reservation in self.reservations:
        #     if reservation.get_reservation_id() == reservation_id:
        #         self.reservations.remove(reservation)
        # raise NoReservationFound

    @dispatch(Reservation)
    def _get_reservation(self, reservation_to_delete: Reservation):
        for reservation in self._reservations:
            if reservation == reservation_to_delete:
                self._reservations.remove(reservation)

    @dispatch(int)
    def _get_reservation(self, reservation_id: int):
        self._reservations.remove(self.find_by_id(reservation_id))

    def find_by_id(self, reservation_id: int) -> Reservation:
        for reservation in self._reservations:
            if reservation.get_reservation_id() == reservation_id:
                return reservation
        raise NoReservationFound

    def get_all_reservations(self) -> list[Reservation]:
        return self._reservations

    def get_number_of_all_reservations(self) -> int:
        return len(self._reservations)
