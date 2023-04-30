from data.model.Customer import Customer
from data.model.Room import Room
from datetime import date


class Reservation:

    def __init__(self):
        self.room: Room = Room()
        self.customer: Customer = Customer()
        self.check_in_date: date = date(1, 1, 1)
        self.check_out_date: date = date(2, 1, 1)
        self.reservation_id = 0

    def set_check_in_date(self, year: int, month: int, day: int) -> None:
        self.check_in_date = date(year, month, day)

    def get_check_in_date(self) -> date:
        return self.check_in_date

    def set_check_out_date(self, year: int, month: int, day: int) -> None:
        self.check_out_date = date(year, month, day)

    def get_check_out_date(self) -> date:
        return self.check_out_date

    def set_reservation_id(self, reservation_id: int) -> None:
        self.reservation_id = reservation_id

    def get_reservation_id(self) -> int:
        return self.reservation_id

    def __str__(self):
        return f"""
        ---Reservation---
        Reservation ID = {self.get_reservation_id()}
        Customer First Name= {self.customer.get_first_name()}
        Customer Last Name= {self.customer.get_last_name()}
        Customer Email= {self.customer.get_email()}
        Room Type: {self.room.get_room_type()}
        Room Number: {self.room.get_room_number()}
        Room Price: {self.room.get_room_price()}
        Check in date : {self.check_in_date}
        Check out date = {self.check_out_date}
        """
