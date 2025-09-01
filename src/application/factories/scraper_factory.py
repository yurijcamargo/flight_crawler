from enum import Enum
from ...infrastructure.scrapers.google_flights_scraper import GoogleFlightsScraper
from ...infrastructure.url_builders.google_flights_url_builder import GoogleFlightsURLBuilder
from ...infrastructure.repositories.csv_flight_repository import CSVFlightRepository
from ...infrastructure.config.settings import BrowserConfig

class ScraperType(Enum):
    GOOGLE_FLIGHTS = "google_flights"


class ScraperFactory:
    @staticmethod
    def create_scraper(scraper_type: ScraperType, browser_config: BrowserConfig = None):
        if scraper_type == ScraperType.GOOGLE_FLIGHTS:
            return GoogleFlightsScraper(browser_config)
        else:
            raise ValueError(f"Unsupported scraper type: {scraper_type}")
    
    @staticmethod
    def create_url_builder(scraper_type: ScraperType):
        if scraper_type == ScraperType.GOOGLE_FLIGHTS:
            return GoogleFlightsURLBuilder()
        else:
            raise ValueError(f"Unsupported URL builder type: {scraper_type}")
    
    @staticmethod
    def create_repository():
        return CSVFlightRepository()