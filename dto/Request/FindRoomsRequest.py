class FindRoomRequest:

    def __init__(self):
        self._check_in_date: str = ""
        self._check_out_date: str = ""

    def set_check_in_date(self, check_in: str):
        self._check_in_date = check_in

    def get_check_in_date(self) -> str:
        return self._check_in_date

    def set_check_out_date(self, check_out: str):
        self._check_out_date = check_out

    def get_check_out_date(self) -> str:
        return self._check_out_date

