# Code: optimization_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class OptimizationAgent(AgentBase):
    def __init__(self, agent_id, name):
        super(OptimizationAgent, self).__init__(agent_id, name)
        self.beliefs = []
        self.goals = []
        self.plans = []
        self.system_state = {}

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

    async def update_system_state(self, new_state):
        self.system_state.update(new_state)
        await self.optimize_system()

    async def optimize_system(self):
        # Use self.system_state to perform optimization
        optimized_state = self.perform_optimization(self.system_state)
        await self.apply_optimized_state(optimized_state)

    def perform_optimization(self, current_state):
        # Optimization logic here
        optimized_state = current_state.copy()
        
        # CPU Optimization
        if current_state.get("CPU_Usage", 0) > 80:
            optimized_state["CPU_Usage"] = max(current_state["CPU_Usage"] - 15, 65)
            optimized_state["CPU_Action"] = "Scale up CPU resources"
        
        # Memory Optimization
        if current_state.get("Memory_Usage", 0) > 70:
            optimized_state["Memory_Usage"] = max(current_state["Memory_Usage"] - 10, 60)
            optimized_state["Memory_Action"] = "Increase available memory"
        
        # Network Optimization
        if current_state.get("Network_Latency", 0) > 100:
            optimized_state["Network_Latency"] = max(current_state["Network_Latency"] - 20, 80)
            optimized_state["Network_Action"] = "Implement load balancing"
        
        # Resource Allocation Optimization
        total_resources = sum(current_state.get(key, 0) for key in ["CPU_Usage", "Memory_Usage", "Network_Latency"])
        if total_resources > 200:
            for key in ["CPU_Usage", "Memory_Usage", "Network_Latency"]:
                optimized_state[key] = max(current_state.get(key, 0) * 0.9, 50)
            optimized_state["Resource_Action"] = "Redistribute resources evenly"
        
        # Performance Monitoring
        optimized_state["Performance_Metric"] = (
            optimized_state.get("CPU_Usage", 0) * 0.4 +
            optimized_state.get("Memory_Usage", 0) * 0.3 +
            optimized_state.get("Network_Latency", 0) * 0.3
        )
        
        return optimized_state

    async def apply_optimized_state(self, optimized_state):
        # Apply the optimized state to the system
        for key, value in optimized_state.items():
            if key.endswith('_Action'):
                # Execute the optimization action
                await self.execute_optimization_action(key, value)
            else:
                # Update the system state
                self.system_state[key] = value
        
        # Notify other agents about the optimization
        await self.notify_agents_of_optimization(optimized_state)
        
        # Log the optimization
        logging.info(f"Applied optimized state: {optimized_state}")
        
        # Update beliefs based on the new state
        self.update_beliefs(optimized_state)
        
        # Check if any new goals need to be set based on the optimized state
        self.set_new_goals(optimized_state)
```