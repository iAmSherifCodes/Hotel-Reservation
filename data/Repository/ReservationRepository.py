import abc

from data.model.Reservation import Reservation


class ReservationRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, reservation: Reservation) -> Reservation:
        pass

    @abc.abstractmethod
    def find_by_id(self, reservation_id: int) -> Reservation:
        pass

    @abc.abstractmethod
    def get_all_reservations(self) -> list[Reservation]:
        pass
