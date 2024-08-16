# Code: agent_management_ui_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class AgentManagementUIAgent(Agent):
    def __init__(self, aid):
        super(AgentManagementUIAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up AgentManagementUIAgent")
        self.add_goal(Goal("ManageAgents", "Maintain"))
        self.add_plan(Plan("ConfigureAgentPlan", self.configure_agent))
        self.add_plan(Plan("MonitorAgentsPlan", self.monitor_agents))

    def act(self):
        display_message(self.aid.name, "Acting in AgentManagementUIAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_management_request(message)

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

    def configure_agent(self):
        display_message(self.aid.name, "Configuring agent")
        # Logic to configure an agent
        agent_configuration = self.get_agent_configuration()
        self.apply_agent_configuration(agent_configuration)

    def monitor_agents(self):
        display_message(self.aid.name, "Monitoring agents")
        # Logic to monitor agents
        agent_status = self.get_belief("AgentStatus")
        if agent_status:
            self.display_agent_status(agent_status)

    def handle_management_request(self, message):
        content = message.content
        self.add_belief(Belief("ManagementRequest", content))
        self.add_goal(Goal("ProcessManagementRequest", "Achieve"))

    def get_agent_configuration(self):
        # Simulated agent configuration retrieval
        return {"Agent1": {"Config1": "Value1", "Config2": "Value2"}}

    def apply_agent_configuration(self, configuration):
        # Simulated agent configuration application
        for agent, config in configuration.items():
            display_message(self.aid.name, f"Applying configuration for {agent}: {config}")

    def display_agent_status(self, status):
        # Simulated agent status display
        for agent, state in status.items():
            display_message(self.aid.name, f"Agent {agent} status: {state}")

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```