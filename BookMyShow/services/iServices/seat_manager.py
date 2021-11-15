from abc import ABC, abstractmethod


class SeatManager(ABC):
    def get_available_seat(self, seat_id):
        pass

    def get_unavailable_seat(self, seat_id):
        pass
   