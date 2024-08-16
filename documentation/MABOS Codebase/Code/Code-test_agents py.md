# Code: test_agents.py

```python
# test_agents.py
import unittest
from unittest.mock import Mock, patch
from mas.mas_manager import MASManager
from mas.agent import Agent
from api.schemas.agent_schemas import AgentCreate, AgentUpdate, AgentType

class TestAgents(unittest.TestCase):

    def setUp(self):
        self.mas_manager = MASManager()

    @patch('mas.mas_manager.MASManager.create_agent')
    async def test_create_agent(self, mock_create_agent):
        agent_data = AgentCreate(name="TestAgent", agent_type=AgentType.REACTIVE, description="Test agent")
        mock_create_agent.return_value = Agent(id="test_id", **agent_data.dict())
        
        agent = await self.mas_manager.create_agent(agent_data)
        
        self.assertEqual(agent.name, "TestAgent")
        self.assertEqual(agent.agent_type, AgentType.REACTIVE)
        self.assertEqual(agent.description, "Test agent")
        mock_create_agent.assert_called_once_with(agent_data)

    @patch('mas.mas_manager.MASManager.get_agent')
    async def test_get_agent(self, mock_get_agent):
        mock_agent = Mock(spec=Agent)
        mock_agent.id = "test_id"
        mock_get_agent.return_value = mock_agent
        
        agent = await self.mas_manager.get_agent("test_id")
        
        self.assertEqual(agent.id, "test_id")
        mock_get_agent.assert_called_once_with("test_id")

    @patch('mas.mas_manager.MASManager.update_agent')
    async def test_update_agent(self, mock_update_agent):
        update_data = AgentUpdate(name="UpdatedAgent", description="Updated description")
        mock_updated_agent = Mock(spec=Agent)
        mock_updated_agent.name = "UpdatedAgent"
        mock_updated_agent.description = "Updated description"
        mock_update_agent.return_value = mock_updated_agent
        
        updated_agent = await self.mas_manager.update_agent("test_id", update_data)
        
        self.assertEqual(updated_agent.name, "UpdatedAgent")
        self.assertEqual(updated_agent.description, "Updated description")
        mock_update_agent.assert_called_once_with("test_id", update_data)

    @patch('mas.mas_manager.MASManager.delete_agent')
    async def test_delete_agent(self, mock_delete_agent):
        mock_delete_agent.return_value = True
        
        result = await self.mas_manager.delete_agent("test_id")
        
        self.assertTrue(result)
        mock_delete_agent.assert_called_once_with("test_id")

    @patch('mas.agent.Agent.update_beliefs')
    async def test_agent_belief_update(self, mock_update_beliefs):
        agent = Agent(id="test_id", name="TestAgent", agent_type=AgentType.BDI)
        new_belief = {"resource": "CPU", "usage": 80}
        
        await agent.update_beliefs([new_belief])
        
        mock_update_beliefs.assert_called_once_with([new_belief])

    @patch('mas.agent.Agent.pursue_goals')
    async def test_agent_goal_pursuit(self, mock_pursue_goals):
        agent = Agent(id="test_id", name="TestAgent", agent_type=AgentType.PROACTIVE)
        
        await agent.pursue_goals()
        
        mock_pursue_goals.assert_called_once()

    # Add more tests as needed for other agent functionalities

if __name__ == '__main__':
    unittest.main()
```