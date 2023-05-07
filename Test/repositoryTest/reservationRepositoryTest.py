from datetime import date
from unittest import TestCase

from data.Repository.ReservationRepositoryImpl import ReservationRepositoryImpl
from data.model.Customer import Customer
from data.model.Reservation import Reservation
from data.model.Room import Room


class test(TestCase):

    def setUp(self) -> None:
        self.reservation_repo = ReservationRepositoryImpl()
        self.room = Room()
        self.room.set_room_type("douBle")
        self.customer = Customer()
        self.customer.set_first_name("John")
        self.customer.set_last_name("Doe")
        self.customer.set_email("myemail@gmail.com")
        self.reservation = Reservation()
        reservation_data = {"room": self.reservation.set_room_to_reserve(self.room),
                            "Customer": self.reservation.set_who_to_reserve(self.customer),
                            "Check-in-date": self.reservation.set_check_in_date(date.today()),
                            "Check-out-date": self.reservation.set_check_out_date(2023, 5, 4)
                            }

    def test_that_when_reservation_is_saved_the_length_of_list_increases(self):
        self.reservation_repo.save(self.reservation)
        # print(self.reservation_repo.get_all_reservations())
        self.assertEqual(1, self.reservation_repo.get_number_of_all_reservations())

    def test_that_when_delete_reservation_reservation_does_not_exist(self):
        self.reservation_repo.save(self.reservation)
        self.reservation_repo.delete(self.reservation)
        self.assertEqual(0, self.reservation_repo.get_number_of_all_reservations())

    def test_that_when_delete_reservation_by_id_reservation_does_not_exist(self):
        self.reservation_repo.save(self.reservation)
        self.reservation_repo.delete_by_id(1)
        self.assertEqual(0, self.reservation_repo.get_number_of_all_reservations())
