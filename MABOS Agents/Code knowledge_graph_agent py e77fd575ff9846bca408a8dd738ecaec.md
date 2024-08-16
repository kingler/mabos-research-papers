# Code: knowledge_graph_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class KnowledgeGraphAgent(Agent):
    def __init__(self, aid):
        super(KnowledgeGraphAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up KnowledgeGraphAgent")
        self.add_goal(Goal("MaintainKnowledgeGraph", "Maintain"))
        self.add_plan(Plan("CreateKnowledgeGraphPlan", self.create_knowledge_graph))
        self.add_plan(Plan("UpdateKnowledgeGraphPlan", self.update_knowledge_graph))
        self.add_plan(Plan("QueryKnowledgeGraphPlan", self.query_knowledge_graph))

    def act(self):
        display_message(self.aid.name, "Acting in KnowledgeGraphAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_knowledge_graph_request(message)

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

    def create_knowledge_graph(self):
        display_message(self.aid.name, "Creating new knowledge graph")
        # Logic to create a new knowledge graph
        new_graph = self.initialize_knowledge_graph()
        self.add_belief(Belief("KnowledgeGraph", new_graph))

    def update_knowledge_graph(self):
        display_message(self.aid.name, "Updating knowledge graph")
        # Logic to update existing knowledge graph
        updated_graph = self.perform_graph_update()
        self.add_belief(Belief("UpdatedKnowledgeGraph", updated_graph))

    def query_knowledge_graph(self):
        display_message(self.aid.name, "Querying knowledge graph")
        # Logic to query the knowledge graph
        query_result = self.execute_graph_query()
        self.add_belief(Belief("QueryResult", query_result))

    def handle_knowledge_graph_request(self, message):
        content = message.content
        # Logic to handle knowledge graph requests from other agents
        self.add_belief(Belief("KnowledgeGraphRequest", content))
        self.add_goal(Goal("ProcessGraphRequest", "Achieve"))

    def initialize_knowledge_graph(self):
        # Simulated knowledge graph creation
        return {
            "Nodes": ["Agent1", "Task1", "Resource1"],
            "Edges": [("Agent1", "performs", "Task1"), ("Task1", "uses", "Resource1")]
        }

    def perform_graph_update(self):
        # Simulated knowledge graph update process
        current_graph = self.get_belief("KnowledgeGraph")
        if current_graph:
            current_graph["Nodes"].append("Goal1")
            current_graph["Edges"].append(("Agent1", "achieves", "Goal1"))
        return current_graph

    def execute_graph_query(self):
        # Simulated knowledge graph query
        return {
            "Query": "What tasks does Agent1 perform?",
            "Result": ["Task1"]
        }

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```