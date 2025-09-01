from dataclasses import dataclass
from typing import Optional

@dataclass
class Flight:
    departure_time: str
    arrival_time: str
    airline: str
    duration: str
    stops: str
    price: str
    co2_emissions: str
    emissions_variation: str
    departure_airport: Optional[str] = None
    destination_airport: Optional[str] = None
    departure_date: Optional[str] = None
    
    def to_dict(self) -> dict:
        return {
            "Departure Time": self.departure_time,
            "Arrival Time": self.arrival_time,
            "Airline Company": self.airline,
            "Flight Duration": self.duration,
            "Stops": self.stops,
            "Price": self.price,
            "CO2 Emissions": self.co2_emissions,
            "Emissions Variation": self.emissions_variation,
            "Departure Airport": self.departure_airport,
            "Destination Airport": self.destination_airport,
            "Departure Date": self.departure_date
        }