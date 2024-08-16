# message.py

```python
# mas/message.py

from dataclasses import dataclass
from datetime import datetime
from typing import Any
from mas.protocols import MessageType

@dataclass
class Message:
    sender: str
    receiver: str
    type: MessageType
    content: Any
    timestamp: datetime = datetime.now()

```