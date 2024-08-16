# Code: environment_visualization_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class EnvironmentVisualizationAgent(Agent):
    def __init__(self, aid):
        super(EnvironmentVisualizationAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up EnvironmentVisualizationAgent")
        self.add_goal(Goal("VisualizeEnvironment", "Maintain"))
        self.add_plan(Plan("CollectEnvironmentalDataPlan", self.collect_environmental_data))
        self.add_plan(Plan("VisualizeEnvironmentalDataPlan", self.visualize_environmental_data))

    def act(self):
        display_message(self.aid.name, "Acting in EnvironmentVisualizationAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_visualization_request(message)

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

    def visualize_environmental_data(self):
        display_message(self.aid.name, "Visualizing environmental data")
        environmental_data = self.get_belief("EnvironmentalData")
        if environmental_data:
            self.display_environmental_data(environmental_data)

    def handle_visualization_request(self, message):
        content = message.content
        self.add_belief(Belief("VisualizationRequest", content))
        self.add_goal(Goal("ProcessVisualizationRequest", "Achieve"))

    def gather_environmental_data(self):
        # Simulated environmental data collection
        return {"Temperature": 25, "Humidity": 60, "AirQuality": "Good"}

    def display_environmental_data(self, data):
        # Simulated environmental data visualization
        display_message(self.aid.name, f"Displaying environmental data: {data}")

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```