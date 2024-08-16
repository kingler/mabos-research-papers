# mas/agent_factory.py
```python
# mas/agent_factory.py

from mas.agent_base import AgentBase
# Import other agent types

class AgentFactory:
    @staticmethod
    def create_agent(agent_type, agent_id, name, **kwargs):
        if agent_type == "base":
            return AgentBase(agent_id, name)
        # Add other agent types here
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")

```
