# Code: custom_node_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class CustomNodeAgent(Agent):
    def __init__(self, aid):
        super(CustomNodeAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up CustomNodeAgent")
        self.add_goal(Goal("ManageCustomNodes", "Maintain"))
        self.add_plan(Plan("CreateCustomNodePlan", self.create_custom_node))
        self.add_plan(Plan("EditCustomNodePlan", self.edit_custom_node))

    def act(self):
        display_message(self.aid.name, "Acting in CustomNodeAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_custom_node_request(message)

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

    def create_custom_node(self):
        display_message(self.aid.name, "Creating custom node")
        # Logic to create a new custom node
        custom_node_data = self.initialize_custom_node()
        self.add_belief(Belief("CustomNodeData", custom_node_data))

    def edit_custom_node(self):
        display_message(self.aid.name, "Editing custom node")
        custom_node_data = self.get_belief("CustomNodeData")
        if custom_node_data:
            updated_custom_node = self.modify_custom_node(custom_node_data)
            self.add_belief(Belief("UpdatedCustomNode", updated_custom_node))

    def handle_custom_node_request(self, message):
        content = message.content
        self.add_belief(Belief("CustomNodeRequest", content))
        self.add_goal(Goal("ProcessCustomNodeRequest", "Achieve"))

    def initialize_custom_node(self):
        # Simulated custom node initialization
        return {"NodeType": "Custom", "Properties": {}}

    def modify_custom_node(self, custom_node_data):
        # Simulated custom node modification
        custom_node_data["Properties"]["NewProperty"] = "Value"
        return custom_node_data

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```