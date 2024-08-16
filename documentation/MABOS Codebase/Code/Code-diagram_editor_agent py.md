# Code: diagram_editor_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class DiagramEditorAgent(Agent):
    def __init__(self, aid):
        super(DiagramEditorAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up DiagramEditorAgent")
        self.add_goal(Goal("ProvideDiagramTools", "Achieve"))
        self.add_plan(Plan("CreateDiagramPlan", self.create_diagram))
        self.add_plan(Plan("EditDiagramPlan", self.edit_diagram))

    def act(self):
        display_message(self.aid.name, "Acting in DiagramEditorAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_diagram_request(message)

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

    def create_diagram(self):
        display_message(self.aid.name, "Creating diagram")
        # Logic to create a new diagram
        diagram_data = self.initialize_diagram()
        self.add_belief(Belief("DiagramData", diagram_data))

    def edit_diagram(self):
        display_message(self.aid.name, "Editing diagram")
        diagram_data = self.get_belief("DiagramData")
        if diagram_data:
            updated_diagram = self.modify_diagram(diagram_data)
            self.add_belief(Belief("UpdatedDiagram", updated_diagram))

    def handle_diagram_request(self, message):
        content = message.content
        self.add_belief(Belief("DiagramRequest", content))
        self.add_goal(Goal("ProcessDiagramRequest", "Achieve"))

    def initialize_diagram(self):
        # Simulated diagram initialization
        return {"Nodes": [], "Edges": []}

    def modify_diagram(self, diagram_data):
        # Simulated diagram modification
        diagram_data["Nodes"].append("NewNode")
        return diagram_data

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```