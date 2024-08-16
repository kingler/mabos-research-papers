# Code: ontology_engineering_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class OntologyEngineeringAgent(Agent):
    def __init__(self, aid):
        super(OntologyEngineeringAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up OntologyEngineeringAgent")
        self.add_goal(Goal("MaintainOntology", "Maintain"))
        self.add_plan(Plan("DevelopOntologyPlan", self.develop_ontology))
        self.add_plan(Plan("UpdateOntologyPlan", self.update_ontology))

    def act(self):
        display_message(self.aid.name, "Acting in OntologyEngineeringAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.INFORM:
            self.handle_ontology_update(message)

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

    def develop_ontology(self):
        display_message(self.aid.name, "Developing new ontology")
        # Logic to develop a new ontology
        new_ontology = self.create_new_ontology()
        self.add_belief(Belief("NewOntology", new_ontology))
        self.add_goal(Goal("IntegrateNewOntology", "Achieve"))

    def update_ontology(self):
        display_message(self.aid.name, "Updating existing ontology")
        # Logic to update existing ontology
        updated_ontology = self.perform_ontology_update()
        self.add_belief(Belief("UpdatedOntology", updated_ontology))

    def handle_ontology_update(self, message):
        content = message.content
        # Logic to handle ontology update requests
        self.add_belief(Belief("OntologyUpdateRequest", content))
        self.add_goal(Goal("ProcessOntologyUpdate", "Achieve"))

    def create_new_ontology(self):
        # Simulated ontology creation
        return {
            "Concepts": ["Agent", "Task", "Resource"],
            "Relations": ["performs", "uses"],
            "Axioms": ["Every Agent performs at least one Task"]
        }

    def perform_ontology_update(self):
        # Simulated ontology update process
        current_ontology = self.get_belief("CurrentOntology")
        if current_ontology:
            current_ontology["Concepts"].append("Goal")
            current_ontology["Relations"].append("achieves")
        return current_ontology

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```