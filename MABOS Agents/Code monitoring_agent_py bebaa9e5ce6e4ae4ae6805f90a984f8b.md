# Code: monitoring_agent_py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class MonitoringAgent(Agent):
    def __init__(self, aid):
        super(MonitoringAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up MonitoringAgent")
        self.add_goal(Goal("MonitorSystem", "Maintain"))
        self.add_plan(Plan("MonitorSystemPlan", self.monitor_system))
        self.add_plan(Plan("HandleAlertsPlan", self.handle_alerts))

    def act(self):
        display_message(self.aid.name, "Acting in MonitoringAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.INFORM:
            self.handle_system_update(message)

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

    def monitor_system(self):
        display_message(self.aid.name, "Monitoring system performance and health")
        # Logic to monitor system
        system_status = self.check_system_status()
        self.add_belief(Belief("SystemStatus", system_status))
        if system_status["Alerts"]:
            self.add_goal(Goal("HandleAlerts", "Achieve"))

    def handle_alerts(self):
        display_message(self.aid.name, "Handling system alerts")
        # Logic to handle alerts
        alerts = self.get_belief("SystemStatus")["Alerts"]
        for alert in alerts:
            self.process_alert(alert)

    def handle_system_update(self, message):
        content = message.content
        # Logic to handle system updates
        self.add_belief(Belief("SystemUpdate", content))
        self.add_goal(Goal("ProcessSystemUpdate", "Achieve"))

    def check_system_status(self):
        # Simulated system status check
        return {
            "Performance": "Good",
            "Health": "Stable",
            "Alerts": ["Low disk space on Server1"]
        }

    def process_alert(self, alert):
        display_message(self.aid.name, f"Processing alert: {alert}")
        # Logic to process and respond to alerts

```