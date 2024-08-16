# Code: notification_ui_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class NotificationUIAgent(Agent):
    def __init__(self, aid):
        super(NotificationUIAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up NotificationUIAgent")
        self.add_goal(Goal("ManageNotifications", "Maintain"))
        self.add_plan(Plan("ProcessNotificationPlan", self.process_notification))
        self.add_plan(Plan("DisplayNotificationPlan", self.display_notification))

    def act(self):
        display_message(self.aid.name, "Acting in NotificationUIAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.INFORM:
            self.handle_notification_message(message)

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

    def process_notification(self):
        display_message(self.aid.name, "Processing notification")
        notification = self.get_belief("PendingNotification")
        if notification:
            processed_notification = self.prioritize_notification(notification)
            self.add_belief(Belief("ProcessedNotification", processed_notification))

    def display_notification(self):
        display_message(self.aid.name, "Displaying notification")
        processed_notification = self.get_belief("ProcessedNotification")
        if processed_notification:
            self.show_notification(processed_notification)

    def handle_notification_message(self, message):
        content = message.content
        self.add_belief(Belief("PendingNotification", content))
        self.add_goal(Goal("ProcessNewNotification", "Achieve"))

    def prioritize_notification(self, notification):
        # Simulated notification prioritization
        priority = "High" if "urgent" in notification.lower() else "Normal"
        return {"content": notification, "priority": priority}

    def show_notification(self, notification):
        # Simulated notification display
        display_message(self.aid.name, f"Showing {notification['priority']} priority notification: {notification['content']}")

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None
```