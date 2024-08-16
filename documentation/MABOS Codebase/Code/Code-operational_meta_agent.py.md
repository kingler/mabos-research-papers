# Code: operational_meta_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class OperationalMetaAgent(Agent):
    def __init__(self, aid):
        super(OperationalMetaAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up OperationalMetaAgent")
        self.add_goal(Goal("ExecuteTasks", "Achieve"))
        self.add_plan(Plan("ProcessTasksPlan", self.process_tasks))
        self.add_plan(Plan("AllocateResourcesPlan", self.allocate_resources))
        self.add_plan(Plan("MonitorProgressPlan", self.monitor_progress))

    def act(self):
        display_message(self.aid.name, "Acting in OperationalMetaAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_task_assignment(message)

    def process_tasks(self):
        display_message(self.aid.name, "Processing assigned tasks")
        tasks = self.get_belief("AssignedTasks")
        if tasks:
            processed_tasks = self.break_down_tasks(tasks)
            self.add_belief(Belief("ProcessedTasks", processed_tasks))

    def allocate_resources(self):
        display_message(self.aid.name, "Allocating resources to tasks")
        processed_tasks = self.get_belief("ProcessedTasks")
        if processed_tasks:
            resource_allocation = self.assign_resources_to_tasks(processed_tasks)
            self.add_belief(Belief("ResourceAllocation", resource_allocation))

    def monitor_progress(self):
        display_message(self.aid.name, "Monitoring task progress")
        resource_allocation = self.get_belief("ResourceAllocation")
        if resource_allocation:
            progress_report = self.check_task_progress(resource_allocation)
            self.add_belief(Belief("ProgressReport", progress_report))
            self.report_progress_to_tactical_agent(progress_report)

    def handle_task_assignment(self, message):
        content = message.content
        self.add_belief(Belief("AssignedTasks", content))
        self.add_goal(Goal("ProcessNewTasks", "Achieve"))

    def break_down_tasks(self, tasks):
        # Simulated task breakdown
        return {"Task1": ["Subtask1A", "Subtask1B"], "Task2": ["Subtask2A", "Subtask2B", "Subtask2C"]}

    def assign_resources_to_tasks(self, processed_tasks):
        # Simulated resource allocation
        return {"Subtask1A": "Team A", "Subtask1B": "Team B", "Subtask2A": "Team C", "Subtask2B": "Team A", "Subtask2C": "Team D"}

    def check_task_progress(self, resource_allocation):
        # Simulated progress checking
        return {"Subtask1A": "80%", "Subtask1B": "60%", "Subtask2A": "100%", "Subtask2B": "40%", "Subtask2C": "20%"}

    def report_progress_to_tactical_agent(self, progress_report):
        # Logic to send progress report to TacticalMetaAgent
        pass

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None
```