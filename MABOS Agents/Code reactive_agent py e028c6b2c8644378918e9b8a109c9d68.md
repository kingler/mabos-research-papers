# Code: reactive_agent.py

```python
#reactive_agent.py
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class ReactiveAgent(Agent):
    def __init__(self, aid):
        super(ReactiveAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up ReactiveAgent")
        self.add_goal(Goal("RespondToEvents", "Maintain"))
        self.add_plan(Plan("MonitorEventsPlan", self.monitor_events))
        self.add_plan(Plan("HandleEventPlan", self.handle_event))

    def act(self):
        display_message(self.aid.name, "Acting in ReactiveAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.INFORM:
            self.handle_event_notification(message)

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

    def monitor_events(self):
        display_message(self.aid.name, "Monitoring system events")
        events = self.check_for_events()
        if events:
            self.add_belief(Belief("NewEvents", events))
            self.add_goal(Goal("HandleNewEvents", "Achieve"))

    def handle_event(self):
        display_message(self.aid.name, "Handling new events")
        events = self.get_belief("NewEvents")
        for event in events:
            response = self.determine_response(event)
            self.execute_response(response)

    def handle_event_notification(self, message):
        content = message.content
        self.add_belief(Belief("EventNotification", content))
        self.add_goal(Goal("ProcessEventNotification", "Achieve"))

    def check_for_events(self):
        # Simulated event checking
        return ["SystemOverload", "NetworkDisruption"]

    def determine_response(self, event):
        # Simulated response determination
        responses = {
            "SystemOverload": "ActivateLoadBalancing",
            "NetworkDisruption": "SwitchToBackupNetwork"
        }
        return responses.get(event, "LogAndMonitor")

    def execute_response(self, response):
        display_message(self.aid.name, f"Executing response: {response}")
        # Logic to execute the response

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```