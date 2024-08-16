# Code: reasoning_engine_agent.py

```python
# reasoning_engine_agent.py

from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class ReasoningEngineAgent(Agent):
    def __init__(self, aid):
        super(ReasoningEngineAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []
        self.inference_rules = []

    def setup(self):
        display_message(self.aid.name, "Setting up ReasoningEngineAgent")
        self.add_goal(Goal("PerformReasoning", "Maintain"))
        self.add_plan(Plan("ProcessInferenceRequestPlan", self.process_inference_request))
        self.add_plan(Plan("UpdateKnowledgeBasePlan", self.update_knowledge_base))

    def act(self):
        display_message(self.aid.name, "Acting in ReasoningEngineAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_reasoning_request(message)

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

    def process_inference_request(self):
        display_message(self.aid.name, "Processing inference request")
        request = self.get_belief("InferenceRequest")
        if request:
            result = self.apply_inference_rules(request)
            self.add_belief(Belief("InferenceResult", result))

    def update_knowledge_base(self):
        display_message(self.aid.name, "Updating knowledge base")
        new_knowledge = self.get_belief("NewKnowledge")
        if new_knowledge:
            self.integrate_new_knowledge(new_knowledge)

    def handle_reasoning_request(self, message):
        content = message.content
        self.add_belief(Belief("InferenceRequest", content))
        self.add_goal(Goal("ProcessInferenceRequest", "Achieve"))

    def apply_inference_rules(self, request):
        # Simulated inference process
        return f"Inference result for {request}"

    def integrate_new_knowledge(self, new_knowledge):
        # Logic to integrate new knowledge into the existing knowledge base
        pass

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```