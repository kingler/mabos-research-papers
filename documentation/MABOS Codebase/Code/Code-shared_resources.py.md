# mas/shared_resources.py

```python
# mas/shared_resources.py

import asyncio

class SharedResource:
    def __init__(self):
        self._resource = None
        self._lock = asyncio.Lock()

    async def get(self):
        async with self._lock:
            return self._resource

    async def set(self, value):
        async with self._lock:
            self._resource = value

```
