# Code: capability_model.py

```python
#models/capability_model.py
from typing import List, Dict, Any, Callable

class Capability:
    def __init__(self, name: str, required_resources: List[str], 
                 action: Callable[[Dict[str, Any]], None]):
        self.name = name
        self.required_resources = required_resources
        self.action = action

    def can_perform(self, available_resources: List[str]) -> bool:
        return all(resource in available_resources for resource in self.required_resources)

    def perform(self, context: Dict[str, Any]) -> None:
        self.action(context)

    def __str__(self):
        return f"Capability(name={self.name}, required_resources={self.required_resources})"
```