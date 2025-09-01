import base64
from .base_url_builder import BaseURLBuilder

class GoogleFlightsURLBuilder(BaseURLBuilder):
    def _create_one_way_bytes(self, departure: str, destination: str, date: str) -> bytes:
        return (
            b'\x08\x1c\x10\x02\x1a\x1e\x12\n' + date.encode() +
            b'j\x07\x08\x01\x12\x03' + departure.encode() +
            b'r\x07\x08\x01\x12\x03' + destination.encode() +
            b'@\x01H\x01p\x01\x82\x01\x0b\x08\xfc\x06`\x04\x08'
        )
    
    def _modify_base64(self, encoded_str: str) -> str:
        insert_index = len(encoded_str) - 6
        return encoded_str[:insert_index] + '_' * 7 + encoded_str[insert_index:]
    
    def build_url(self, departure: str, destination: str, departure_date: str) -> str:
        flight_bytes = self._create_one_way_bytes(departure, destination, departure_date)
        base64_str = base64.b64encode(flight_bytes).decode('utf-8')
        modified_str = self._modify_base64(base64_str)
        return f'https://www.google.com/travel/flights/search?tfs={modified_str}'