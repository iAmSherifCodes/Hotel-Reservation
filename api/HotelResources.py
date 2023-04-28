from datetime import datetime
from data.model.Customer import Customer
from data.model import RoomType


class HotelResources:
    def add_customer(self, email: str, first_name: str, last_name: str) -> None:
        pass

    def create_customer(self, email: str, first_name: str, last_name: str) -> None:
        pass

    def get_customer(self, customer_email: str) -> Customer:
        pass

    def get_all_customers(self) -> Customer:
        pass

    def get_room(self, room_number: int) -> RoomType:
        pass

    def book_a_room(self, customer_email: str, room: RoomType, check_in_date: datetime, check_out_date: datetime) -> RoomType:
        pass

    def get_customer_reservations(self, customer_email: str) -> Customer:
        pass

    def find_a_room(self, check_in_date: datetime, check_out_date: datetime) -> None:
        pass
