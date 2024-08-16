# Code: optimization_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class OptimizationAgent(Agent):
    def __init__(self, aid):
        super(OptimizationAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up OptimizationAgent")
        self.add_goal(Goal("OptimizeSystemPerformance", "Maintain"))
        self.add_plan(Plan("AnalyzePerformancePlan", self.analyze_performance))
        self.add_plan(Plan("OptimizeResourcesPlan", self.optimize_resources))

    def act(self):
        display_message(self.aid.name, "Acting in OptimizationAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_optimization_request(message)

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

    def analyze_performance(self):
        display_message(self.aid.name, "Analyzing system performance")
        # Logic to analyze system performance
        performance_metrics = self.collect_performance_metrics()
        self.add_belief(Belief("PerformanceMetrics", performance_metrics))
        if self.needs_optimization(performance_metrics):
            self.add_goal(Goal("OptimizeResources", "Achieve"))

    def optimize_resources(self):
        display_message(self.aid.name, "Optimizing system resources")
        # Logic to optimize resources based on performance metrics
        optimization_result = self.apply_optimization_algorithms()
        self.add_belief(Belief("OptimizationResult", optimization_result))

    def handle_optimization_request(self, message):
        content = message.content
        # Logic to handle optimization requests from other agents
        self.add_belief(Belief("OptimizationRequest", content))
        self.add_goal(Goal("ProcessOptimizationRequest", "Achieve"))

    def collect_performance_metrics(self):
        # Simulated performance metric collection
        return {
            "CPU_Usage": 75,
            "Memory_Usage": 60,
            "Network_Latency": 50
        }

    def needs_optimization(self, metrics):
        # Simple logic to determine if optimization is needed
        return metrics["CPU_Usage"] > 80 or metrics["Memory_Usage"] > 70

    def apply_optimization_algorithms(self):
        # Simulated optimization process
        return {
            "Optimized_CPU_Usage": 65,
            "Optimized_Memory_Usage": 55,
            "Recommendations": ["Scale up resources", "Load balance traffic"]
        }

```