# Code: architecture_design_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class ArchitectureDesignAgent(Agent):
    def __init__(self, aid):
        super(ArchitectureDesignAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up ArchitectureDesignAgent")
        self.add_goal(Goal("DesignArchitecture", "Achieve"))
        self.add_plan(Plan("DesignArchitecturePlan", self.design_architecture))

    def act(self):
        display_message(self.aid.name, "Acting in ArchitectureDesignAgent")
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

    def design_architecture(self):
        display_message(self.aid.name, "Designing system architecture")
        # Logic to design architecture
        architecture = {"Component1": "Details1", "Component2": "Details2"}
        self.add_belief(Belief("Architecture", architecture))
        self.add_goal(Goal("ValidateArchitecture", "Achieve"))

    def handle_inform(self, message):
        content = message.content
        # Logic to handle received information
        self.add_belief(Belief("ReceivedInformation", content))

```