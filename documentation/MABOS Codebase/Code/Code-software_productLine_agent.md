# Code: software_productLine_agent

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class SoftwareProductLineAgent(Agent):
    def __init__(self, aid):
        super(SoftwareProductLineAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up SoftwareProductLineAgent")
        self.add_goal(Goal("ManageProductLine", "Achieve"))
        self.add_plan(Plan("DefineProductVariantsPlan", self.define_product_variants))
        self.add_plan(Plan("ReuseComponentsPlan", self.reuse_components))

    def act(self):
        display_message(self.aid.name, "Acting in SoftwareProductLineAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_product_line_request(message)

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

    def define_product_variants(self):
        display_message(self.aid.name, "Defining product variants")
        # Logic to define product variants
        product_variants = {"Variant1": "Features1", "Variant2": "Features2"}
        self.add_belief(Belief("ProductVariants", product_variants))
        self.add_goal(Goal("ReuseComponents", "Achieve"))

    def reuse_components(self):
        display_message(self.aid.name, "Reusing components across product variants")
        # Logic to reuse components
        reused_components = {"Component1": "UsedInVariant1And2", "Component2": "UsedInVariant1"}
        self.add_belief(Belief("ReusedComponents", reused_components))

    def handle_product_line_request(self, message):
        content = message.content
        # Logic to handle product line requests
        self.add_belief(Belief("ProductLineRequest", content))
        self.add_goal(Goal("ProcessProductLineRequest", "Achieve"))

```