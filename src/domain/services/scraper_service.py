from abc import ABC, abstractmethod
from typing import List
from ..entities.flight import Flight

class ScraperService(ABC):
    @abstractmethod
    async def scrape_flights(self, url: str) -> List[Flight]:
        pass
    
    @abstractmethod
    def build_url(self, departure: str, destination: str, departure_date: str) -> str:
        pass