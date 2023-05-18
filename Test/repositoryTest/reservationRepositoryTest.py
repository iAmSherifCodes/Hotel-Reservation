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
        self.reservation.set_room_to_reserve(self.room)
        self.reservation.set_who_to_reserve(self.customer)
        self.reservation.set_check_in_date(date.today())
        self.reservation.set_check_out_date(2023, 5, 21)

    def test_that_when_reservation_is_saved_the_length_of_list_increases(self):
        self.reservation_repo.save(self.reservation)
        self.assertEqual(1, self.reservation_repo.get_number_of_all_reservations())

    def test_save_reservation(self):
        saved_reserve = self.reservation_repo.save(self.reservation)
        self.assertIsNotNone(saved_reserve)

    def test_find_by_id(self):
        new_customer = Customer()
        new_room = Room()
        new_reservation = Reservation()
        second_saved_reserve = self.reservation_repo.save(new_reservation)
        first_saved_reserve = self.reservation_repo.save(self.reservation)
        found_reservation = self.reservation_repo.find_by_id(first_saved_reserve.get_reservation_id())
        self.assertIsNotNone(found_reservation)

    def test_find_by_id_returns_none_object(self):
        new_customer = Customer()
        new_room = Room()
        new_reservation = Reservation()
        second_saved_reserve = self.reservation_repo.save(new_reservation)
        first_saved_reserve = self.reservation_repo.save(self.reservation)
        found_reservation = self.reservation_repo.find_by_id(first_saved_reserve.get_reservation_id() + "sw")
        self.assertIsNone(found_reservation)

    def test_delete_by_id(self):
        new_customer = Customer()
        new_room = Room()
        new_reservation = Reservation()
        second_saved_reserve = self.reservation_repo.save(new_reservation)
        first_saved_reserve = self.reservation_repo.save(self.reservation)
        self.assertEqual(2, self.reservation_repo.get_number_of_all_reservations())
        self.reservation_repo.delete_by_id(second_saved_reserve.get_reservation_id())
        self.assertEqual(1, self.reservation_repo.get_number_of_all_reservations())
