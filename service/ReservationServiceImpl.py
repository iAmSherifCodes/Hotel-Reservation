from datetime import date, timedelta

from Utils.Exceptions.NoReservationFound import NoReservationFound
from Utils.Exceptions.RoomNotAvailableForReservation import RoomNotAvailableForReservation
from data.Repository import ReservationRepository
from data.Repository.ReservationRepositoryImpl import ReservationRepositoryImpl
from data.model.Customer import Customer
from data.model.Reservation import Reservation
from data.model.Room import Room
from dto.Request.FindReservationByCustomerEmailRequest import FindReservationByCustomerEmailRequest
from dto.Request.FindReservationByIdRequest import FindReservationByIdRequest
from dto.Response.FindReservationByCustomerEmailResponse import FindReservationByCustomerEmailResponse
from dto.Response.FindReservationByIdResponse import FindReservationByIdResponse
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
            return self._reservation_repository.save(reservation)
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

        return available_rooms

    def find_reservations_by_customer_email(self, customer_email_request: FindReservationByCustomerEmailRequest) -> FindReservationByCustomerEmailResponse:
        new_email_request = customer_email_request.get_customer_email()

        response: FindReservationByCustomerEmailResponse = FindReservationByCustomerEmailResponse()
        for reservation in self._reservation_repository.get_all_reservations():
            if reservation.get_who_reserved_room().get_email() == new_email_request:
                response.set_reservation_id(reservation.get_reservation_id())
                response.set_room_to_reserve(reservation.get_reserved_room())
                response.set_who_to_reserve(reservation.get_who_reserved_room())
                response.set_check_in_date(reservation.get_check_in_date())
                response.set_check_out_date(reservation.get_check_out_date())
                # response.set_customer_reservations(reservation)
        return response

    def display_reservations(self) -> list[Reservation]:
        return self._reservation_repository.get_all_reservations()

    def find_reservation_by_id(self, reservation_id_request: FindReservationByIdRequest) -> FindReservationByIdResponse | None:
        new_reservation_id_response = reservation_id_request.get_id()
        response: FindReservationByIdResponse = FindReservationByIdResponse()
        found_reservation = self._search_for_reservation_in_repository(new_reservation_id_response)
        if found_reservation is not None:
            response.set_reservation(found_reservation)
            return response

        raise NoReservationFound

    def _search_for_reservation_in_repository(self, reservation_id: str):
        for reservation in self._reservation_repository.get_all_reservations():
            if reservation.get_reservation_id() == reservation_id:
                return reservation

        return None


