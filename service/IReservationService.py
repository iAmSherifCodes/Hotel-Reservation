import abc
from datetime import date

from data.model.Customer import Customer
from data.model.Reservation import Reservation
from data.model.Room import Room
from dto.Request.FindReservationByCustomerEmailRequest import FindReservationByCustomerEmailRequest
from dto.Request.FindReservationByIdRequest import FindReservationByIdRequest
from dto.Response.FindReservationByCustomerEmailResponse import FindReservationByCustomerEmailResponse
from dto.Response.FindReservationByIdResponse import FindReservationByIdResponse


class IReservationService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def search_for_available_rooms(self, check_in: date, check_out: date):
        pass

    @abc.abstractmethod
    def reserve_a_room(self, customer: Customer, room: Room, check_in_date: date, check_out_date: date) -> Reservation:
        pass

    @abc.abstractmethod
    def display_reservations(self) -> list[Reservation]:
        pass

    @abc.abstractmethod
    def find_reservation_by_id(self, reservation_id: FindReservationByIdRequest) -> FindReservationByIdResponse:
        pass

    @abc.abstractmethod
    def find_reservations_by_customer_email(self, customer_email_request: FindReservationByCustomerEmailRequest) -> FindReservationByCustomerEmailResponse:
        pass
