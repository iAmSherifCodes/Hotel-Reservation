from data.model.Reservation import Reservation


class FindReservationByIdResponse:
    def __init__(self):
        self._reservation = None

    def set_reservation(self, reservation: Reservation) -> None:
        self._reservation = reservation

    def get_reservation(self) -> Reservation:
        return self._reservation

    def __repr__(self):
        return f"""
        ====== Reservation ======
        
        {self.get_reservation()}
        
        =========================
        """
