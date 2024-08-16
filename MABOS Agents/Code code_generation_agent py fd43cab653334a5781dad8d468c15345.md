# Code: code_generation_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class CodeGenerationAgent(Agent):
    def __init__(self, aid):
        super(CodeGenerationAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up CodeGenerationAgent")
        self.add_goal(Goal("GenerateCode", "Achieve"))
        self.add_plan(Plan("GenerateCodePlan", self.generate_code))

    def act(self):
        display_message(self.aid.name, "Acting in CodeGenerationAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.INFORM:
            self.handle_inform(message)

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

    def generate_code(self):
        display_message(self.aid.name, "Generating code from design specifications")
        # Logic to generate code
        code_snippets = {"Class1": "Code1", "Class2": "Code2"}
        self.add_belief(Belief("GeneratedCode", code_snippets))
        self.add_goal(Goal("ValidateGeneratedCode", "Achieve"))

    def handle_inform(self, message):
        content = message.content
        # Logic to handle received information
        self.add_belief(Belief("ReceivedInformation", content))

```