from typing import List
from ...domain.entities.flight import Flight
from ...domain.repositories.flight_repository import FlightRepository
from ..factories.scraper_factory import ScraperFactory, ScraperType
from ...infrastructure.config.settings import BrowserConfig

class ScrapeFlightsUseCase:
    def __init__(self, repository: FlightRepository = None):
        self.repository = repository or ScraperFactory.create_repository()
    
    async def execute(
        self,
        departure: str,
        destination: str,
        departure_date: str,
        scraper_type: ScraperType,
        output_filename: str = "flight_data.csv",
        browser_config: BrowserConfig = None
    ) -> List[Flight]:
        
        # Create scraper and URL builder
        scraper = ScraperFactory.create_scraper(scraper_type, browser_config)
        url_builder = ScraperFactory.create_url_builder(scraper_type)
        
        # Build URL
        url = url_builder.build_url(departure, destination, departure_date)
        print(f"Scraping URL: {url}")
        
        # Scrape flights
        flights = await scraper.scrape_flights(url)
        
        # Add metadata to flights
        for flight in flights:
            flight.departure_airport = departure
            flight.destination_airport = destination
            flight.departure_date = departure_date
        
        # Save flights
        await self.repository.save_flights(flights, output_filename)
        
        return flights