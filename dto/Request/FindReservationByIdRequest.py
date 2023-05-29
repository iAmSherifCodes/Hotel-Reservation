class FindReservationByIdRequest:
    def __init__(self):
        self._id = None

    def set_id(self, reservation_id: str) -> None:
        self._id = reservation_id

    def get_id(self) -> str:
        return self._id
