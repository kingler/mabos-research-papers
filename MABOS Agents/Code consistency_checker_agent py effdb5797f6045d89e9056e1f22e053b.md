# Code: consistency_checker_agent.py

```python
# consistency_checker_agent.py
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class ConsistencyCheckerAgent(Agent):
    def __init__(self, aid):
        super(ConsistencyCheckerAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up ConsistencyCheckerAgent")
        self.add_goal(Goal("EnsureDataConsistency", "Maintain"))
        self.add_plan(Plan("ValidateDataPlan", self.validate_data))
        self.add_plan(Plan("ReconcileDiscrepanciesPlan", self.reconcile_discrepancies))

    def act(self):
        display_message(self.aid.name, "Acting in ConsistencyCheckerAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_consistency_check_request(message)

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

    def validate_data(self):
        display_message(self.aid.name, "Validating data consistency")
        # Logic to validate data consistency
        inconsistencies = self.check_for_inconsistencies()
        self.add_belief(Belief("Inconsistencies", inconsistencies))
        if inconsistencies:
            self.add_goal(Goal("ReconcileInconsistencies", "Achieve"))

    def reconcile_discrepancies(self):
        display_message(self.aid.name, "Reconciling discrepancies")
        inconsistencies = self.get_belief("Inconsistencies")
        if inconsistencies:
            reconciliation_result = self.perform_reconciliation(inconsistencies)
            self.add_belief(Belief("ReconciliationResult", reconciliation_result))

    def handle_consistency_check_request(self, message):
        content = message.content
        self.add_belief(Belief("ConsistencyCheckRequest", content))
        self.add_goal(Goal("ProcessConsistencyCheckRequest", "Achieve"))

    def check_for_inconsistencies(self):
        # Simulated inconsistency check
        return ["Inconsistency1", "Inconsistency2"]

    def perform_reconciliation(self, inconsistencies):
        # Simulated reconciliation process
        return {"Inconsistency1": "Resolved", "Inconsistency2": "Resolved"}

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```