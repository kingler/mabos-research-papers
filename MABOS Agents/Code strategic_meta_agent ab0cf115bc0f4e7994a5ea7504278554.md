# Code: strategic_meta_agent

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class StrategicMetaAgent(Agent):
    def __init__(self, aid):
        super(StrategicMetaAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up StrategicMetaAgent")
        self.add_goal(Goal("DevelopLongTermStrategy", "Achieve"))
        self.add_plan(Plan("AnalyzeEnvironmentPlan", self.analyze_environment))
        self.add_plan(Plan("FormulateStrategyPlan", self.formulate_strategy))
        self.add_plan(Plan("CommunicateStrategyPlan", self.communicate_strategy))

    def act(self):
        display_message(self.aid.name, "Acting in StrategicMetaAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.INFORM:
            self.handle_environmental_update(message)

    def analyze_environment(self):
        display_message(self.aid.name, "Analyzing business environment")
        # Logic to analyze environment
        environmental_factors = self.gather_environmental_data()
        self.add_belief(Belief("EnvironmentalFactors", environmental_factors))

    def formulate_strategy(self):
        display_message(self.aid.name, "Formulating long-term strategy")
        # Logic to formulate strategy
        strategy = self.develop_strategy()
        self.add_belief(Belief("LongTermStrategy", strategy))

    def communicate_strategy(self):
        display_message(self.aid.name, "Communicating strategy to other agents")
        strategy = self.get_belief("LongTermStrategy")
        if strategy:
            self.send_strategy_to_tactical_agents(strategy)

    def handle_environmental_update(self, message):
        content = message.content
        self.add_belief(Belief("EnvironmentalUpdate", content))
        self.add_goal(Goal("ReassessStrategy", "Achieve"))

    def gather_environmental_data(self):
        # Simulated environmental data gathering
        return {"MarketTrends": "Growth", "CompetitorActions": "Expansion", "TechnologicalChanges": "AI Adoption"}

    def develop_strategy(self):
        # Simulated strategy development
        return {"Focus": "Innovation", "Expansion": "Global Markets", "Investment": "R&D"}

    def send_strategy_to_tactical_agents(self, strategy):
        # Logic to communicate strategy to TacticalMetaAgents
        pass

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```