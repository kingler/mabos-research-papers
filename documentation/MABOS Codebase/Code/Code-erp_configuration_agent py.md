# Code: erp_configuration_agent.py

```python
#erp_configuration_agent.py
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class ERPConfigurationAgent(Agent):
    def __init__(self, aid):
        super(ERPConfigurationAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up ERPConfigurationAgent")
        self.add_goal(Goal("ManageERPConfiguration", "Maintain"))
        self.add_plan(Plan("InitializeERPConfigurationPlan", self.initialize_erp_configuration))
        self.add_plan(Plan("UpdateERPConfigurationPlan", self.update_erp_configuration))
        self.add_plan(Plan("VisualizeERPConfigurationPlan", self.visualize_erp_configuration))

    def act(self):
        display_message(self.aid.name, "Acting in ERPConfigurationAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_erp_request(message)

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

    def initialize_erp_configuration(self):
        display_message(self.aid.name, "Initializing ERP configuration")
        # Logic to initialize ERP configuration
        erp_configuration = self.setup_erp_configuration()
        self.add_belief(Belief("ERPConfiguration", erp_configuration))

    def update_erp_configuration(self):
        display_message(self.aid.name, "Updating ERP configuration")
        erp_configuration = self.get_belief("ERPConfiguration")
        if erp_configuration:
            updated_configuration = self.modify_erp_configuration(erp_configuration)
            self.add_belief(Belief("UpdatedERPConfiguration", updated_configuration))

    def visualize_erp_configuration(self):
        display_message(self.aid.name, "Visualizing ERP configuration")
        updated_configuration = self.get_belief("UpdatedERPConfiguration")
        if updated_configuration:
            self.display_erp_configuration(updated_configuration)

    def handle_erp_request(self, message):
        content = message.content
        self.add_belief(Belief("ERPRequest", content))
        self.add_goal(Goal("ProcessERPRequest", "Achieve"))

    def setup_erp_configuration(self):
        # Simulated ERP configuration setup
        return {"Modules": ["Finance", "HR", "Sales"], "Settings": {"Finance": "Configured", "HR": "Not Configured", "Sales": "Configured"}}

    def modify_erp_configuration(self, erp_configuration):
        # Simulated ERP configuration modification
        erp_configuration["Settings"]["HR"] = "Configured"
        return erp_configuration

    def display_erp_configuration(self, erp_configuration):
        # Simulated ERP configuration display
        display_message(self.aid.name, f"Displaying ERP configuration: {erp_configuration}")

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```