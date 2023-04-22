import datetime

from model.Customer import Customer
from model.IRoom import IRoom
from datetime import date

from model.Room import Room
from model.RoomType import RoomType


class Reservation:
    def __init__(self, room: IRoom, customer: Customer, check_in: date, check_out: date):
        self.room = room
        self.customer = customer
        self.check_in_date = check_in
        self.check_out_date = check_out

    def __str__(self):
        return f"""
        ---Reservation---
        Customer First Name= {self.customer.get_first_name()}
        Customer Last Name= {self.customer.get_last_name()}
        Customer Email= {self.customer.get_email()}
        Room Type: {self.room.get_room_type()}
        Room Number: {self.room.get_room_number()}
        Room Price: {self.room.get_room_price()}
        Check in date : {self.check_in_date}
        Check out date = {self.check_out_date}
        """

