from abc import ABC, abstractmethod

class BaseURLBuilder(ABC):
    @abstractmethod
    def build_url(self, departure: str, destination: str, departure_date: str) -> str:
        pass