# Code: data_visualization_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class DataVisualizationAgent(Agent):
    def __init__(self, aid):
        super(DataVisualizationAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up DataVisualizationAgent")
        self.add_goal(Goal("VisualizeData", "Maintain"))
        self.add_plan(Plan("PrepareDataPlan", self.prepare_data))
        self.add_plan(Plan("GenerateVisualizationPlan", self.generate_visualization))

    def act(self):
        display_message(self.aid.name, "Acting in DataVisualizationAgent")
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

    def prepare_data(self):
        display_message(self.aid.name, "Preparing data for visualization")
        # Logic to prepare data for visualization
        raw_data = self.get_belief("RawData")
        if raw_data:
            prepared_data = self.process_raw_data(raw_data)
            self.add_belief(Belief("PreparedData", prepared_data))

    def generate_visualization(self):
        display_message(self.aid.name, "Generating data visualization")
        prepared_data = self.get_belief("PreparedData")
        if prepared_data:
            visualization = self.create_visualization(prepared_data)
            self.add_belief(Belief("Visualization", visualization))

    def handle_visualization_request(self, message):
        content = message.content
        self.add_belief(Belief("RawData", content))
        self.add_goal(Goal("ProcessVisualizationRequest", "Achieve"))

    def process_raw_data(self, raw_data):
        # Simulated data processing
        return {"ProcessedData": "Cleaned and formatted " + raw_data}

    def create_visualization(self, prepared_data):
        # Simulated visualization creation
        return {"VisualizationType": "BarChart", "Data": prepared_data["ProcessedData"]}

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```