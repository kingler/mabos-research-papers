# Code: business_plan_agent.py

```python
# business_plan_agent.py
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class BusinessPlanAgent(Agent):
    def __init__(self, aid):
        super(BusinessPlanAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up BusinessPlanAgent")
        self.add_goal(Goal("DevelopBusinessPlans", "Achieve"))
        self.add_plan(Plan("CreateBusinessPlanPlan", self.create_business_plan))
        self.add_plan(Plan("ReviewBusinessPlanPlan", self.review_business_plan))

    def act(self):
        display_message(self.aid.name, "Acting in BusinessPlanAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_plan_request(message)

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

    def create_business_plan(self):
        display_message(self.aid.name, "Creating business plan")
        # Logic to create business plan
        business_plan = self.develop_plan()
        self.add_belief(Belief("BusinessPlan", business_plan))

    def review_business_plan(self):
        display_message(self.aid.name, "Reviewing business plan")
        business_plan = self.get_belief("BusinessPlan")
        if business_plan:
            review_result = self.evaluate_plan(business_plan)
            self.add_belief(Belief("ReviewResult", review_result))

    def handle_plan_request(self, message):
        content = message.content
        self.add_belief(Belief("PlanRequest", content))
        self.add_goal(Goal("ProcessPlanRequest", "Achieve"))

    def develop_plan(self):
        # Simulated business plan development
        return {"Objective1": "Strategy1", "Objective2": "Strategy2"}

    def evaluate_plan(self, plan):
        # Simulated plan evaluation
        return {"Objective1": "Feasible", "Objective2": "Needs Improvement"}

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```