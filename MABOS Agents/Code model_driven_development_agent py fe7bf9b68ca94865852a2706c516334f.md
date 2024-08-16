# Code: model_driven_development_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class ModelDrivenDevelopmentAgent(Agent):
    def __init__(self, aid):
        super(ModelDrivenDevelopmentAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up ModelDrivenDevelopmentAgent")
        self.add_goal(Goal("TransformModels", "Achieve"))
        self.add_plan(Plan("TransformModelsPlan", self.transform_models))
        self.add_plan(Plan("ValidateTransformationPlan", self.validate_transformation))

    def act(self):
        display_message(self.aid.name, "Acting in ModelDrivenDevelopmentAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_transformation_request(message)

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

    def transform_models(self):
        display_message(self.aid.name, "Transforming models into executable code")
        # Logic to transform models into code
        transformed_code = {"Model1": "Code1", "Model2": "Code2"}
        self.add_belief(Belief("TransformedCode", transformed_code))
        self.add_goal(Goal("ValidateTransformation", "Achieve"))

    def validate_transformation(self):
        display_message(self.aid.name, "Validating transformed code")
        # Logic to validate transformed code
        validation_results = {"Code1": "Valid", "Code2": "Invalid"}
        self.add_belief(Belief("ValidationResults", validation_results))

    def handle_transformation_request(self, message):
        content = message.content
        # Logic to handle transformation requests
        self.add_belief(Belief("TransformationRequest", content))
        self.add_goal(Goal("ProcessTransformationRequest", "Achieve"))

```