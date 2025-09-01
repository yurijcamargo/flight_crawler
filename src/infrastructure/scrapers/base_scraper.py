from abc import ABC, abstractmethod
from typing import List
from playwright.async_api import async_playwright, Browser, Page
from ...domain.entities.flight import Flight
from ..config.settings import BrowserConfig

class BaseScraper(ABC):
    def __init__(self, browser_config: BrowserConfig = None):
        self.browser_config = browser_config or BrowserConfig.default()
    
    async def setup_browser(self):
        p = await async_playwright().start()
        
        browser_settings = {"headless": self.browser_config.headless}
        
        if self.browser_config.proxy_config and self.browser_config.proxy_config.is_configured:
            proxy_settings = self.browser_config.proxy_config.to_playwright_format()
            if proxy_settings:
                browser_settings["proxy"] = proxy_settings
        
        browser = await p.chromium.launch(**browser_settings)
        page = await browser.new_page()
        
        return p, browser, page
    
    @abstractmethod
    async def scrape_flights(self, url: str) -> List[Flight]:
        pass
    
    @abstractmethod
    async def extract_flight_data(self, flight_element) -> Flight:
        pass