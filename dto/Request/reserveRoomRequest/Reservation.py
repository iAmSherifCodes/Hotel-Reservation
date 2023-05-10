from data.model.Customer import Customer
from data.Repository.RoomRepository import RoomRepository
from datetime import date

from data.model.Room import Room
from data.model.RoomType import RoomType


class Reservation:
    def __init__(self, room: RoomRepository, customer: Customer, check_in: date, check_out: date):
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


roomd = Room(10, 10, True)
roomd.set_room_type(RoomType.DOUBLE)
c = Customer("Sherif", "Olanrewaju", "sherif04@gmail.com")
d = date(2002,12,12)
dt = date(2012,11,11)
reservation = Reservation(roomd, c, d, dt)
print(reservation)

