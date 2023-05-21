class RoomIsReserved(Exception):
    def __repr__(self):
        return "Room Is Reserved"
