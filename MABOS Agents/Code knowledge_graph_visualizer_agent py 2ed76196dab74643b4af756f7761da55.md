# Code: knowledge_graph_visualizer_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class KnowledgeGraphVisualizerAgent(Agent):
    def __init__(self, aid):
        super(KnowledgeGraphVisualizerAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up KnowledgeGraphVisualizerAgent")
        self.add_goal(Goal("VisualizeKnowledgeGraph", "Maintain"))
        self.add_plan(Plan("CollectKnowledgeDataPlan", self.collect_knowledge_data))
        self.add_plan(Plan("GenerateKnowledgeGraphPlan", self.generate_knowledge_graph))
        self.add_plan(Plan("DisplayKnowledgeGraphPlan", self.display_knowledge_graph))

    def act(self):
        display_message(self.aid.name, "Acting in KnowledgeGraphVisualizerAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_graph_request(message)

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

    def collect_knowledge_data(self):
        display_message(self.aid.name, "Collecting knowledge data")
        # Logic to collect knowledge data
        knowledge_data = self.gather_knowledge_data()
        self.add_belief(Belief("KnowledgeData", knowledge_data))

    def generate_knowledge_graph(self):
        display_message(self.aid.name, "Generating knowledge graph")
        knowledge_data = self.get_belief("KnowledgeData")
        if knowledge_data:
            knowledge_graph = self.create_knowledge_graph(knowledge_data)
            self.add_belief(Belief("KnowledgeGraph", knowledge_graph))

    def display_knowledge_graph(self):
        display_message(self.aid.name, "Displaying knowledge graph")
        knowledge_graph = self.get_belief("KnowledgeGraph")
        if knowledge_graph:
            self.show_knowledge_graph(knowledge_graph)

    def handle_graph_request(self, message):
        content = message.content
        self.add_belief(Belief("GraphRequest", content))
        self.add_goal(Goal("ProcessGraphRequest", "Achieve"))

    def gather_knowledge_data(self):
        # Simulated knowledge data collection
        return {"Node1": ["Relation1", "Node2"], "Node2": ["Relation2", "Node3"]}

    def create_knowledge_graph(self, knowledge_data):
        # Simulated knowledge graph creation
        return {"Graph": knowledge_data}

    def show_knowledge_graph(self, knowledge_graph):
        # Simulated knowledge graph display
        display_message(self.aid.name, f"Displaying knowledge graph: {knowledge_graph}")

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```