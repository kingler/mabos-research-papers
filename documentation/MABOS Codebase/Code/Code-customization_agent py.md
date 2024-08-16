# Code: customization_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class CustomizationAgent(Agent):
    def __init__(self, aid):
        super(CustomizationAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up CustomizationAgent")
        self.add_goal(Goal("EnableUICustomization", "Maintain"))
        self.add_plan(Plan("CollectUserPreferencesPlan", self.collect_user_preferences))
        self.add_plan(Plan("ApplyCustomizationsPlan", self.apply_customizations))

    def act(self):
        display_message(self.aid.name, "Acting in CustomizationAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_customization_request(message)

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

    def collect_user_preferences(self):
        display_message(self.aid.name, "Collecting user preferences")
        # Logic to collect user preferences
        user_preferences = self.gather_user_preferences()
        self.add_belief(Belief("UserPreferences", user_preferences))

    def apply_customizations(self):
        display_message(self.aid.name, "Applying customizations")
        user_preferences = self.get_belief("UserPreferences")
        if user_preferences:
            self.customize_ui(user_preferences)

    def handle_customization_request(self, message):
        content = message.content
        self.add_belief(Belief("CustomizationRequest", content))
        self.add_goal(Goal("ProcessCustomizationRequest", "Achieve"))

    def gather_user_preferences(self):
        # Simulated user preferences collection
        return {"Theme": "Dark", "Layout": "Compact"}

    def customize_ui(self, preferences):
        # Simulated UI customization
        display_message(self.aid.name, f"Applying customizations: {preferences}")

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```