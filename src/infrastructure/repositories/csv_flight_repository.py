import csv
import pandas as pd
from typing import List
from ...domain.entities.flight import Flight
from ...domain.repositories.flight_repository import FlightRepository

class CSVFlightRepository(FlightRepository):
    def _clean_text(self, value):
        if isinstance(value, str):
            return value.replace('Â', '').replace(' ', ' ').replace('Ã', '').replace('¶', '').strip()
        return value
    
    def _clean_csv(self, filename: str):
        data = pd.read_csv(filename, encoding="utf-8")
        cleaned_data = data.applymap(self._clean_text)
        cleaned_data.to_csv(filename, index=False)
        print(f"Cleaned CSV saved to: {filename}")
    
    async def save_flights(self, flights: List[Flight], filename: str = "flight_data.csv") -> None:
        if not flights:
            return
        
        headers = list(flights[0].to_dict().keys())
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for flight in flights:
                writer.writerow(flight.to_dict())
        
        self._clean_csv(filename)
    
    async def load_flights(self, filename: str) -> List[Flight]:
        flights = []
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                flight = Flight(
                    departure_time=row.get("Departure Time", ""),
                    arrival_time=row.get("Arrival Time", ""),
                    airline=row.get("Airline Company", ""),
                    duration=row.get("Flight Duration", ""),
                    stops=row.get("Stops", ""),
                    price=row.get("Price", ""),
                    co2_emissions=row.get("CO2 Emissions", ""),
                    emissions_variation=row.get("Emissions Variation", ""),
                    departure_airport=row.get("Departure Airport"),
                    destination_airport=row.get("Destination Airport"),
                    departure_date=row.get("Departure Date")
                )
                flights.append(flight)
        return flights