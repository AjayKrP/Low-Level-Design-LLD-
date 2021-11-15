from abc import ABC, abstractmethod


class SearchManager(ABC):
    @abstractmethod
    def get_movie_by_name(self, movie_name):
        pass
