import abc
from datetime import date

from data.model.Customer import Customer
from data.model.Reservation import Reservation
from data.model.Room import Room


class IReservationService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def reserve_a_room(self, customer: Customer, room: Room, check_in_date: date, check_out_date: date) -> Reservation:
        pass

    @abc.abstractmethod
    def get_customers_reservation(self, customer: Customer) -> list[Reservation]:
        pass

    @abc.abstractmethod
    def display_reservations(self) -> list[Reservation]:
        pass

    @abc.abstractmethod
    def find_reservation_by_id(self, reservation_id: int) -> Reservation:
        pass

    @abc.abstractmethod
    def find_reservation_by_customer_first_name(self, customer_first_name: str) -> list[Reservation]:
        pass
