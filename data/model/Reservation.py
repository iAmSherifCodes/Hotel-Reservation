from datetime import date

from multipledispatch import dispatch

from data.model.Customer import Customer
from data.model.Room import Room


class Reservation:

    def __init__(self):
        self._room: Room = Room()
        self._customer: Customer = Customer()
        self._check_in_date: date = date(1, 1, 1)
        self._check_out_date: date = date(2, 1, 1)
        self._reservation_id: str = "AppUtils.generate_id()"

    def set_room_to_reserve(self, room: Room) -> None:
        self._room = room

    def get_reserved_room(self) -> Room:
        return self._room

    def set_who_to_reserve(self, customer: Customer) -> None:
        self._customer = customer

    def get_who_reserved_room(self) -> Customer:
        return self._customer

    @dispatch(int, int, int)
    def set_check_in_date(self, year: int, month: int, day: int) -> None:
        self._check_in_date = date(year, month, day)

    @dispatch(date)
    def set_check_in_date(self, new_date: date) -> None:
        self._check_in_date = new_date

    @dispatch(int, int, int)
    def set_check_out_date(self, year: int, month: int, day: int) -> None:
        self._check_out_date = date(year, month, day)

    @dispatch(date)
    def set_check_out_date(self, new_date: date) -> None:
        self._check_out_date = new_date

    def get_check_in_date(self) -> date:
        return self._check_in_date

    def get_check_out_date(self) -> date:
        return self._check_out_date

    def set_reservation_id(self, reservation_id: str) -> None:
        self._reservation_id = reservation_id

    def get_reservation_id(self) -> str:
        return self._reservation_id

    def __str__(self):
        return f"""
        ---Reservation---
        Reservation ID = {self.get_reservation_id()}
        Customer First Name= {self._customer.get_first_name()}
        Customer Last Name= {self._customer.get_last_name()}
        Customer Email= {self._customer.get_email()}
        Room Type: {self._room.get_room_type()}
        Room Is Reserved: {self.get_reserved_room().get_is_reserved()}
        Room Number: {self._room.get_room_id()}
        Room Price: {self._room.get_room_price()}
        Check in date : {self.get_check_in_date()}
        Check out date : {self.get_check_out_date()}
        """
