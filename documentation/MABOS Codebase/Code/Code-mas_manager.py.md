# mas/mas_manager.py

```python
class MASManager:
    def __init__(self):
        self.agents = {}
        self.shared_resources = {}

    def create_agent(self, agent_type, agent_id, name, **kwargs):
        agent = AgentFactory.create_agent(agent_type, agent_id, name, **kwargs)
        self.agents[agent_id] = agent
        return agent

    def remove_agent(self, agent_id):
        if agent_id in self.agents:
            del self.agents[agent_id]

    def get_agent(self, agent_id):
        return self.agents.get(agent_id)

    def create_shared_resource(self, resource_name):
        self.shared_resources[resource_name] = SharedResource()

    async def get_shared_resource(self, resource_name):
        if resource_name in self.shared_resources:
            return await self.shared_resources[resource_name].get()
        raise KeyError(f"Shared resource not found: {resource_name}")

```
