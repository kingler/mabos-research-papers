# Code: agent_base.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan
import logging
from mas.bdi_engine import BDIEngine
from mas.exceptions import AgentCommunicationError, TaskExecutionError
from mas.logging_config import setup_logger
from mas.exceptions import MABOSException

logging.basicConfig(level=logging.INFO)

class AgentBase(Agent):
    def __init__(self, agent_id, name):
        super(AgentBase, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = [] 
        self.name = name
        self.bdi_engine = BDIEngine(self)
        self.logger = logging.getLogger(f"Agent-{self.name}")
        self.desires = set()
        self.intentions = set()


    def setup(self):
        display_message(self.aid.name, "Setting up AgentBase")
        # Common setup logic for all agents

    def act(self):
        display_message(self.aid.name, "Acting in AgentBase")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        self.handle_message(message)

    def add_goal(self, goal):
        self.goals.append(goal)

    def add_belief(self, belief):
        self.beliefs.append(belief)

    def add_plan(self, plan):
        self.plans.append(plan)

    def execute_plans(self):
        for plan in self.plans:
            if plan.is_applicable(self.beliefs, self.goals):
                plan.execute()

    def handle_message(self, message):
        # Common message handling logic for all agents
        display_message(self.aid.name, f"Handling message: {message.content}")
        self.add_belief(Belief("ReceivedMessage", message.content))

    async def send_message(self, receiver, message):
        try:
            await receiver.receive_message(message)
        except Exception as e:
            raise AgentCommunicationError(f"Failed to send message to {receiver.name}: {str(e)}")

    async def receive_message(self, message):
        self.logger.info(f"Received message: {message}")
        # Process the message
        self.handle_message(message)
        # Update beliefs based on the message content
        self.add_belief(Belief("LastReceivedMessage", message))
        # Check if the message triggers any goals
        self.update_goals_from_message(message)
        # Notify the BDI engine of the new message
        await self.bdi_engine.process_new_information(message)

    async def execute_task(self, task):
        try:
            result = await self.bdi_engine.execute_intention(task)
            self.logger.info(f"Task executed successfully: {task}")
            return result
        except TaskExecutionError as e:
            self.logger.error(f"Task execution failed: {str(e)}")
            raise
```