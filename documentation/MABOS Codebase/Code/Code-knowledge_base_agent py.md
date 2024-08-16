# Code: knowledge_base_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class KnowledgeBaseAgent(Agent):
    def __init__(self, aid):
        super(KnowledgeBaseAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up KnowledgeBaseAgent")
        self.add_goal(Goal("MaintainKnowledgeBase", "Maintain"))
        self.add_plan(Plan("UpdateKnowledgeBasePlan", self.update_knowledge_base))
        self.add_plan(Plan("ProvideKnowledgePlan", self.provide_knowledge))

    def act(self):
        display_message(self.aid.name, "Acting in KnowledgeBaseAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_knowledge_request(message)

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

    def update_knowledge_base(self):
        display_message(self.aid.name, "Updating knowledge base")
        # Logic to update knowledge base
        updated_knowledge = self.fetch_latest_knowledge()
        self.add_belief(Belief("KnowledgeBase", updated_knowledge))

    def provide_knowledge(self):
        display_message(self.aid.name, "Providing knowledge to other agents")
        knowledge_request = self.get_belief("KnowledgeRequest")
        if knowledge_request:
            knowledge = self.retrieve_knowledge(knowledge_request)
            self.send_knowledge_response(knowledge)

    def handle_knowledge_request(self, message):
        content = message.content
        self.add_belief(Belief("KnowledgeRequest", content))
        self.add_goal(Goal("ProcessKnowledgeRequest", "Achieve"))

    def fetch_latest_knowledge(self):
        # Simulated knowledge fetching
        return {"Topic1": "Information1", "Topic2": "Information2"}

    def retrieve_knowledge(self, request):
        # Simulated knowledge retrieval
        knowledge_base = self.get_belief("KnowledgeBase")
        return knowledge_base.get(request, "No Information Available")

    def send_knowledge_response(self, knowledge):
        # Logic to send knowledge response to requesting agent
        pass

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```