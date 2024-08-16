# Code: environmental_agent.py

```python
# environmental_agent.py
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class EnvironmentalAgent(Agent):
    def __init__(self, aid):
        super(EnvironmentalAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up EnvironmentalAgent")
        self.add_goal(Goal("MonitorEnvironment", "Maintain"))
        self.add_plan(Plan("CollectEnvironmentalDataPlan", self.collect_environmental_data))
        self.add_plan(Plan("RespondToEnvironmentalChangesPlan", self.respond_to_environmental_changes))

    def act(self):
        display_message(self.aid.name, "Acting in EnvironmentalAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.INFORM:
            self.handle_environmental_update(message)

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

    def collect_environmental_data(self):
        display_message(self.aid.name, "Collecting environmental data")
        # Logic to collect environmental data
        environmental_data = self.gather_environmental_data()
        self.add_belief(Belief("EnvironmentalData", environmental_data))

    def respond_to_environmental_changes(self):
        display_message(self.aid.name, "Responding to environmental changes")
        environmental_data = self.get_belief("EnvironmentalData")
        if environmental_data:
            response = self.determine_response(environmental_data)
            self.execute_response(response)

    def handle_environmental_update(self, message):
        content = message.content
        self.add_belief(Belief("EnvironmentalUpdate", content))
        self.add_goal(Goal("ProcessEnvironmentalUpdate", "Achieve"))

    def gather_environmental_data(self):
        # Simulated environmental data collection
        return {"Temperature": 25, "Humidity": 60, "AirQuality": "Good"}

    def determine_response(self, data):
        # Simulated response determination
        return {"Action": "AdjustHVAC", "Parameters": {"Temperature": 22}}

    def execute_response(self, response):
        display_message(self.aid.name, f"Executing response: {response}")
        # Logic to execute the response

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```