import asyncio
from ...application.use_cases.scrape_flights_use_case import ScrapeFlightsUseCase
from ...application.factories.scraper_factory import ScraperType
from ...infrastructure.config.settings import BrowserConfig

async def main():
    use_case = ScrapeFlightsUseCase()
    
    # Configure browser settings
    browser_config = BrowserConfig.default()
    
    # Execute scraping with different sites

    google_flights = await use_case.execute(
        departure="SFO",
        destination="LAX", 
        departure_date="2025-12-25",
        scraper_type=ScraperType.GOOGLE_FLIGHTS,
        output_filename="google_flights.csv",
        browser_config=browser_config
    )
    

    if google_flights:
        for flight in google_flights[:2]:
            print(f"  - {flight.airline}: {flight.departure_time} -> {flight.arrival_time} ({flight.price})")
    


if __name__ == "__main__":
    asyncio.run(main())