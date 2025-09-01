import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

@dataclass
class ProxyConfig:
    server: Optional[str]
    username: Optional[str]
    password: Optional[str]
    bypass: Optional[str]
    
    @classmethod
    def from_env(cls) -> 'ProxyConfig':
        return cls(
            server=os.getenv('PROXY_SERVER'),
            username=os.getenv('PROXY_USERNAME'),
            password=os.getenv('PROXY_PASSWORD'),
            bypass=os.getenv('PROXY_BYPASS')
        )
    
    def to_playwright_format(self) -> Optional[dict]:
        if not self.server:
            return None
        
        proxy_settings = {"server": self.server}
        
        if self.username and self.password:
            proxy_settings.update({
                "username": self.username,
                "password": self.password
            })
        
        if self.bypass:
            proxy_settings["bypass"] = self.bypass
            
        return proxy_settings
    
    @property
    def is_configured(self) -> bool:
        return bool(self.server)

@dataclass
class BrowserConfig:
    headless: bool = False
    proxy_config: Optional[ProxyConfig] = None
    
    @classmethod
    def default(cls) -> 'BrowserConfig':
        return cls(
            headless=False,
            proxy_config=ProxyConfig.from_env()
        )