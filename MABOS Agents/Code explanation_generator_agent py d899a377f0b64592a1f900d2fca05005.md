# Code: explanation_generator_agent.py

```python
# explanation_generator_agent.py
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class ExplanationGeneratorAgent(Agent):
    def __init__(self, aid):
        super(ExplanationGeneratorAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up ExplanationGeneratorAgent")
        self.add_goal(Goal("GenerateExplanations", "Maintain"))
        self.add_plan(Plan("CollectActionDataPlan", self.collect_action_data))
        self.add_plan(Plan("GenerateExplanationPlan", self.generate_explanation))

    def act(self):
        display_message(self.aid.name, "Acting in ExplanationGeneratorAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_explanation_request(message)

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

    def collect_action_data(self):
        display_message(self.aid.name, "Collecting data for explanation")
        # Logic to collect action data
        action_data = self.gather_action_data()
        self.add_belief(Belief("ActionData", action_data))

    def generate_explanation(self):
        display_message(self.aid.name, "Generating explanation")
        action_data = self.get_belief("ActionData")
        if action_data:
            explanation = self.create_explanation(action_data)
            self.add_belief(Belief("GeneratedExplanation", explanation))

    def handle_explanation_request(self, message):
        content = message.content
        self.add_belief(Belief("ExplanationRequest", content))
        self.add_goal(Goal("ProcessExplanationRequest", "Achieve"))

    def gather_action_data(self):
        # Simulated action data collection
        return {"Action1": "Reason1", "Action2": "Reason2"}

    def create_explanation(self, action_data):
        # Simulated explanation generation
        return {"Action1": "Explanation for Action1", "Action2": "Explanation for Action2"}

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```