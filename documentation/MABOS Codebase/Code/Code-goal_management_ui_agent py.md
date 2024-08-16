# Code: goal_management_ui_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class GoalManagementUIAgent(Agent):
    def __init__(self, aid):
        super(GoalManagementUIAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up GoalManagementUIAgent")
        self.add_goal(Goal("ManageGoals", "Maintain"))
        self.add_plan(Plan("CreateGoalPlan", self.create_goal))
        self.add_plan(Plan("TrackGoalsPlan", self.track_goals))
        self.add_plan(Plan("VisualizeGoalsPlan", self.visualize_goals))

    def act(self):
        display_message(self.aid.name, "Acting in GoalManagementUIAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_goal_request(message)

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

    def create_goal(self):
        display_message(self.aid.name, "Creating goal")
        # Logic to create a new goal
        goal_data = self.initialize_goal()
        self.add_belief(Belief("GoalData", goal_data))

    def track_goals(self):
        display_message(self.aid.name, "Tracking goals")
        goal_data = self.get_belief("GoalData")
        if goal_data:
            tracked_goals = self.monitor_goals(goal_data)
            self.add_belief(Belief("TrackedGoals", tracked_goals))

    def visualize_goals(self):
        display_message(self.aid.name, "Visualizing goals")
        tracked_goals = self.get_belief("TrackedGoals")
        if tracked_goals:
            self.display_goals(tracked_goals)

    def handle_goal_request(self, message):
        content = message.content
        self.add_belief(Belief("GoalRequest", content))
        self.add_goal(Goal("ProcessGoalRequest", "Achieve"))

    def initialize_goal(self):
        # Simulated goal initialization
        return {"GoalName": "New Goal", "Status": "Active"}

    def monitor_goals(self, goal_data):
        # Simulated goal tracking
        goal_data["Status"] = "In Progress"
        return goal_data

    def display_goals(self, goals):
        # Simulated goal visualization
        display_message(self.aid.name, f"Displaying goals: {goals}")

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```