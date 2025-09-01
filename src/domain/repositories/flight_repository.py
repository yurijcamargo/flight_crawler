from abc import ABC, abstractmethod
from typing import List
from ..entities.flight import Flight

class FlightRepository(ABC):
    @abstractmethod
    async def save_flights(self, flights: List[Flight], filename: str = None) -> None:
        pass
    
    @abstractmethod
    async def load_flights(self, filename: str) -> List[Flight]:
        pass