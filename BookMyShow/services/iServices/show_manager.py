from abc import ABC, abstractmethod


class ShowManager(ABC):
    def get_show_by_id(self, show_id) -> Show:
        pass

    def add_show(self, show):
        pass
