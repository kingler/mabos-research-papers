# bdi_components.py

```python
# mas/bdi_components.py

from dataclasses import dataclass

@dataclass
class Belief:
    name: str
    value: Any

@dataclass
class Desire:
    name: str
    priority: int

@dataclass
class Intention:
    name: str
    plan: Any

# Update AgentBase to use these components
class AgentBase:
    def __init__(self, agent_id, name):
        # ... (previous init code) ...
        self.beliefs = set()
        self.desires = set()
        self.intentions = set()

    def add_belief(self, name, value):
        self.beliefs.add(Belief(name, value))

    def add_desire(self, name, priority):
        self.desires.add(Desire(name, priority))

    def add_intention(self, name, plan):
        self.intentions.add(Intention(name, plan))
```
