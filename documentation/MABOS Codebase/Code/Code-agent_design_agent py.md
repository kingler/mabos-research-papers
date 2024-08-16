# Code: agent_design_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class AgentDesignAgent(Agent):
    def __init__(self, aid):
        super(AgentDesignAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up AgentDesignAgent")
        self.add_goal(Goal("DesignAgents", "Achieve"))
        self.add_plan(Plan("DesignAgentsPlan", self.design_agents))

    def act(self):
        display_message(self.aid.name, "Acting in AgentDesignAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.INFORM:
            self.handle_inform(message)

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

    def design_agents(self):
        display_message(self.aid.name, "Designing agents and their interactions")
        # Logic to design agents
        agent_designs = {"Agent1": "Design1", "Agent2": "Design2"}
        self.add_belief(Belief("AgentDesigns", agent_designs))
        self.add_goal(Goal("ValidateAgentDesigns", "Achieve"))

    def handle_inform(self, message):
        content = message.content
        # Logic to handle received information
        self.add_belief(Belief("ReceivedInformation", content))

```