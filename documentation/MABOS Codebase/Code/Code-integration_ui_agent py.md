# Code: integration_ui_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class IntegrationUIAgent(Agent):
    def __init__(self, aid):
        super(IntegrationUIAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up IntegrationUIAgent")
        self.add_goal(Goal("ManageExternalIntegrations", "Maintain"))
        self.add_plan(Plan("ConnectExternalSystemPlan", self.connect_external_system))
        self.add_plan(Plan("SynchronizeDataPlan", self.synchronize_data))

    def act(self):
        display_message(self.aid.name, "Acting in IntegrationUIAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_integration_request(message)

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

    def connect_external_system(self):
        display_message(self.aid.name, "Connecting to external system")
        # Logic to connect to an external system
        connection_info = self.establish_connection()
        self.add_belief(Belief("ExternalSystemConnection", connection_info))

    def synchronize_data(self):
        display_message(self.aid.name, "Synchronizing data with external system")
        connection_info = self.get_belief("ExternalSystemConnection")
        if connection_info:
            synchronized_data = self.perform_data_sync(connection_info)
            self.add_belief(Belief("SynchronizedData", synchronized_data))

    def handle_integration_request(self, message):
        content = message.content
        self.add_belief(Belief("IntegrationRequest", content))
        self.add_goal(Goal("ProcessIntegrationRequest", "Achieve"))

    def establish_connection(self):
        # Simulated connection establishment
        return {"SystemID": "ExternalSystem1", "Status": "Connected"}

    def perform_data_sync(self, connection_info):
        # Simulated data synchronization
        return {"SyncedData": "Data from " + connection_info["SystemID"]}

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```