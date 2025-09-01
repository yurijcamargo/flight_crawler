import asyncio
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.infrastructure.scrapers.google_flights_scraper import GoogleScraper

async def main():
    scraper = GoogleScraper()
    url = "https://www.google.com/flights?hl=en#flt=GRU.JFK.2024-12-01"
    flights = await scraper.scrape_flights(url)

    print(f"\nTotal flights found: {len(flights)}")
    for i, flight in enumerate(flights):
        print(f"{i + 1}. {flight.airline} | {flight.departure_time} → {flight.arrival_time} | {flight.price}")

if __name__ == "__main__":
    asyncio.run(main())
