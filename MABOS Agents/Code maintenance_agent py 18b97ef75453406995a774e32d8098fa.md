# Code: maintenance_agent.py

```python
# maintenance_agent.py
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class MaintenanceAgent(Agent):
    def __init__(self, aid):
        super(MaintenanceAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up MaintenanceAgent")
        self.add_goal(Goal("PerformMaintenance", "Maintain"))
        self.add_plan(Plan("ScheduleMaintenancePlan", self.schedule_maintenance))
        self.add_plan(Plan("ExecuteMaintenancePlan", self.execute_maintenance))

    def act(self):
        display_message(self.aid.name, "Acting in MaintenanceAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_maintenance_request(message)

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

    def schedule_maintenance(self):
        display_message(self.aid.name, "Scheduling maintenance tasks")
        # Logic to schedule maintenance tasks
        maintenance_schedule = self.create_maintenance_schedule()
        self.add_belief(Belief("MaintenanceSchedule", maintenance_schedule))

    def execute_maintenance(self):
        display_message(self.aid.name, "Executing maintenance tasks")
        maintenance_schedule = self.get_belief("MaintenanceSchedule")
        if maintenance_schedule:
            self.perform_maintenance(maintenance_schedule)

    def handle_maintenance_request(self, message):
        content = message.content
        self.add_belief(Belief("MaintenanceRequest", content))
        self.add_goal(Goal("ProcessMaintenanceRequest", "Achieve"))

    def create_maintenance_schedule(self):
        # Simulated maintenance schedule creation
        return {"Task1": "Daily", "Task2": "Weekly"}

    def perform_maintenance(self, schedule):
        # Simulated maintenance task execution
        for task, frequency in schedule.items():
            display_message(self.aid.name, f"Performing {task} with frequency {frequency}")

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```