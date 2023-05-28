from Utils.AppUtils import AppUtils
from data.Repository.ReservationRepository import ReservationRepository
from data.model.Reservation import Reservation


class ReservationRepositoryImpl(ReservationRepository):
    def __init__(self):
        self._reservations: list[Reservation] = []

    def save(self, reservation: Reservation) -> Reservation:
        # new_reservation = []
        reservation.set_reservation_id(str(AppUtils.generate_id()))
        self._reservations.append(reservation)
        return reservation

    def delete_by_id(self, reservation_id: str) -> None:
        found_reservation = self.find_by_id(reservation_id)
        self.get_all_reservations().remove(found_reservation)

    def find_by_id(self, reservation_id: str) -> Reservation | None:
        for reservation in self.get_all_reservations():
            if reservation.get_reservation_id() == reservation_id:
                return reservation
        return None

    def get_all_reservations(self) -> list[Reservation]:
        return self._reservations

    def get_number_of_all_reservations(self) -> int:
        return len(self._reservations)
