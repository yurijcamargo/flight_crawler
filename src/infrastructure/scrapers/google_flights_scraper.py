from typing import List, Optional
from ...domain.entities.flight import Flight
from .base_scraper import BaseScraper

class GoogleFlightsScraper(BaseScraper):
    async def extract_element_text(self, flight, selector: str, aria_label: Optional[str] = None) -> str:
        if aria_label:
            element = await flight.query_selector(f'{selector}[aria-label*="{aria_label}"]')
        else:
            element = await flight.query_selector(selector)
        return await element.inner_text() if element else "N/A"
    
    async def extract_flight_data(self, flight_element) -> Flight:
        departure_time = await self.extract_element_text(flight_element, 'span', "Departure time")
        arrival_time = await self.extract_element_text(flight_element, 'span', "Arrival time")
        airline = await self.extract_element_text(flight_element, ".sSHqwe")
        duration = await self.extract_element_text(flight_element, "div.gvkrdb")
        stops = await self.extract_element_text(flight_element, "div.EfT7Ae span.ogfYpf")
        price = await self.extract_element_text(flight_element, "div.FpEdX span")
        co2_emissions = await self.extract_element_text(flight_element, "div.O7CXue")
        emissions_variation = await self.extract_element_text(flight_element, "div.N6PNV")
        
        return Flight(
            departure_time=departure_time,
            arrival_time=arrival_time,
            airline=airline,
            duration=duration,
            stops=stops,
            price=price,
            co2_emissions=co2_emissions,
            emissions_variation=emissions_variation
        )
    
    async def scrape_flights(self, url: str) -> List[Flight]:
        flights = []
        playwright, browser, page = await self.setup_browser()
        
        try:
            await page.goto(url)
            await page.wait_for_selector(".pIav2d")
            
            flight_elements = await page.query_selector_all(".pIav2d")
            for flight_element in flight_elements:
                flight = await self.extract_flight_data(flight_element)
                flights.append(flight)
                
        finally:
            await browser.close()
            await playwright.stop()
        
        return flights