# Code: web_service_adapter.py

```python
# web_service_adapter.py
import aiohttp
import asyncio
from typing import Dict, Any, Optional

class WebServiceAdapter:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def close(self):
        if self.session:
            await self.session.close()
            self.session = None

    async def get(self, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Perform a GET request to the web service."""
        url = f"{self.base_url}/{endpoint}"
        async with self.session.get(url, params=params) as response:
            response.raise_for_status()
            return await response.json()

    async def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform a POST request to the web service."""
        url = f"{self.base_url}/{endpoint}"
        async with self.session.post(url, json=data) as response:
            response.raise_for_status()
            return await response.json()

    async def put(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform a PUT request to the web service."""
        url = f"{self.base_url}/{endpoint}"
        async with self.session.put(url, json=data) as response:
            response.raise_for_status()
            return await response.json()

    async def delete(self, endpoint: str) -> Dict[str, Any]:
        """Perform a DELETE request to the web service."""
        url = f"{self.base_url}/{endpoint}"
        async with self.session.delete(url) as response:
            response.raise_for_status()
            return await response.json()

class WebServiceManager:
    def __init__(self):
        self.adapters: Dict[str, WebServiceAdapter] = {}

    async def create_adapter(self, service_name: str, base_url: str):
        adapter = WebServiceAdapter(base_url)
        await adapter.__aenter__()
        self.adapters[service_name] = adapter

    async def close_all_adapters(self):
        for adapter in self.adapters.values():
            await adapter.close()
        self.adapters.clear()

    async def call_service(self, service_name: str, method: str, endpoint: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
        adapter = self.adapters.get(service_name)
        if not adapter:
            raise ValueError(f"No adapter found for service: {service_name}")

        if method.lower() == 'get':
            return await adapter.get(endpoint, params=data)
        elif method.lower() == 'post':
            return await adapter.post(endpoint, data=data)
        elif method.lower() == 'put':
            return await adapter.put(endpoint, data=data)
        elif method.lower() == 'delete':
            return await adapter.delete(endpoint)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

# Example usage
async def main():
    manager = WebServiceManager()

    # Create adapters for different web services
    await manager.create_adapter("weather_service", "<https://api.weatherapi.com/v1>")
    await manager.create_adapter("news_service", "<https://api.newsapi.org/v2>")

    try:
        # Make calls to different web services
        weather_data = await manager.call_service("weather_service", "GET", "current.json", {"key": "YOUR_API_KEY", "q": "London"})
        print("Weather data:", weather_data)

        news_data = await manager.call_service("news_service", "GET", "top-headlines", {"apiKey": "YOUR_API_KEY", "country": "us"})
        print("News data:", news_data)

    except aiohttp.ClientError as e:
        print(f"An error occurred while calling the web service: {e}")

    finally:
        # Close all adapters
        await manager.close_all_adapters()

if __name__ == "__main__":
    asyncio.run(main())

```