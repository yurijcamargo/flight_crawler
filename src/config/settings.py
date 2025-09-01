import os
import logging
from dotenv import load_dotenv
from src.domain.entities.proxy_settings import ProxySettings

# Load environment variables
load_dotenv()

class Config:
    """Configuration management."""
    
    # Proxy settings
    @staticmethod
    def load_proxy_settings() -> ProxySettings:
        """Load proxy settings from environment variables."""
        return ProxySettings(
            server=os.getenv('PROXY_SERVER'),
            username=os.getenv('PROXY_USERNAME'),
            password=os.getenv('PROXY_PASSWORD'),
            bypass=os.getenv('PROXY_BYPASS')
        )

    # Output settings
    @staticmethod
    def get_output_dir() -> str:
        """Get output directory."""
        return os.getenv('OUTPUT_DIR', 'data/output')

    # Browser settings
    @staticmethod
    def get_headless_mode() -> bool:
        """Get headless browser mode."""
        return os.getenv('DEFAULT_HEADLESS', 'false').lower() == 'true'

    @staticmethod
    def get_timeout() -> int:
        """Get default timeout."""
        return int(os.getenv('DEFAULT_TIMEOUT', '30000'))

    @staticmethod
    def get_retry_attempts() -> int:
        """Get retry attempts."""
        return int(os.getenv('RETRY_ATTEMPTS', '3'))

    # Logging configuration
    @staticmethod
    def setup_logging(level: str = 'INFO') -> None:
        """Setup logging configuration."""
        logging.basicConfig(
            level=getattr(logging, level.upper()),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler('flight_scraper.log')
            ]
        )