import abc
from data.model.Reservation import Reservation


class ReservationRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, reservation: Reservation) -> Reservation:
        pass

    @abc.abstractmethod
    def find_by_id(self, reservation_id: str) -> Reservation:
        pass

    @abc.abstractmethod
    def delete_by_id(self, reservation_id: str) -> None:
        pass

    @abc.abstractmethod
    def get_all_reservations(self) -> list[Reservation]:
        pass

    @abc.abstractmethod
    def get_number_of_all_reservations(self) -> int:
        pass
