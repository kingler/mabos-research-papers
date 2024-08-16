# Code: external_system_interface.py

```python
# external_system_interface.py
import asyncio
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class ExternalSystemInterface(ABC):
    def __init__(self, system_name: str, connection_details: Dict[str, Any]):
        self.system_name = system_name
        self.connection_details = connection_details
        self.is_connected = False

    @abstractmethod
    async def connect(self) -> bool:
        """Establish a connection to the external system."""
        pass

    @abstractmethod
    async def disconnect(self):
        """Disconnect from the external system."""
        pass

    @abstractmethod
    async def send_data(self, data: Any) -> bool:
        """Send data to the external system."""
        pass

    @abstractmethod
    async def receive_data(self) -> Optional[Any]:
        """Receive data from the external system."""
        pass

class MockExternalSystem(ExternalSystemInterface):
    def __init__(self, system_name: str, connection_details: Dict[str, Any]):
        super().__init__(system_name, connection_details)
        self.mock_data_queue = asyncio.Queue()

    async def connect(self) -> bool:
        print(f"Connecting to mock system: {self.system_name}")
        await asyncio.sleep(1)  # Simulate connection time
        self.is_connected = True
        return True

    async def disconnect(self):
        print(f"Disconnecting from mock system: {self.system_name}")
        await asyncio.sleep(0.5)  # Simulate disconnection time
        self.is_connected = False

    async def send_data(self, data: Any) -> bool:
        if not self.is_connected:
            print("Not connected. Cannot send data.")
            return False
        print(f"Sending data to {self.system_name}: {data}")
        await asyncio.sleep(0.1)  # Simulate sending time
        return True

    async def receive_data(self) -> Optional[Any]:
        if not self.is_connected:
            print("Not connected. Cannot receive data.")
            return None
        try:
            data = await asyncio.wait_for(self.mock_data_queue.get(), timeout=1.0)
            print(f"Received data from {self.system_name}: {data}")
            return data
        except asyncio.TimeoutError:
            print("No data received within timeout period.")
            return None

    async def mock_incoming_data(self, data: Any):
        """Method to simulate incoming data for testing purposes."""
        await self.mock_data_queue.put(data)

class ExternalSystemManager:
    def __init__(self):
        self.systems: Dict[str, ExternalSystemInterface] = {}

    def register_system(self, system: ExternalSystemInterface):
        self.systems[system.system_name] = system

    async def connect_all(self):
        connection_results = await asyncio.gather(
            *[system.connect() for system in self.systems.values()],
            return_exceptions=True
        )
        for system_name, result in zip(self.systems.keys(), connection_results):
            if isinstance(result, Exception):
                print(f"Failed to connect to {system_name}: {result}")
            elif result:
                print(f"Successfully connected to {system_name}")
            else:
                print(f"Connection to {system_name} failed")

    async def disconnect_all(self):
        await asyncio.gather(*[system.disconnect() for system in self.systems.values()])

    async def send_data_to_system(self, system_name: str, data: Any) -> bool:
        system = self.systems.get(system_name)
        if not system:
            print(f"System {system_name} not found.")
            return False
        return await system.send_data(data)

    async def receive_data_from_system(self, system_name: str) -> Optional[Any]:
        system = self.systems.get(system_name)
        if not system:
            print(f"System {system_name} not found.")
            return None
        return await system.receive_data()

# Example usage
async def main():
    manager = ExternalSystemManager()

    # Register mock external systems
    system1 = MockExternalSystem("System1", {"host": "mock1.example.com", "port": 8080})
    system2 = MockExternalSystem("System2", {"host": "mock2.example.com", "port": 9090})
    manager.register_system(system1)
    manager.register_system(system2)

    # Connect to all systems
    await manager.connect_all()

    # Send and receive data
    await manager.send_data_to_system("System1", "Hello, System1!")
    await system1.mock_incoming_data("Response from System1")
    received_data = await manager.receive_data_from_system("System1")
    print(f"Main received: {received_data}")

    # Disconnect from all systems
    await manager.disconnect_all()

if __name__ == "__main__":
    asyncio.run(main())
```