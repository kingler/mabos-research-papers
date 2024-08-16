# Code: communication_interface_agent.py
```python
# communication_interface_agent.py
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class CommunicationInterfaceAgent(Agent):
    def __init__(self, aid):
        super(CommunicationInterfaceAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up CommunicationInterfaceAgent")
        self.add_goal(Goal("ManageCommunicationInterfaces", "Maintain"))
        self.add_plan(Plan("InitializeCommunicationInterfacePlan", self.initialize_communication_interface))
        self.add_plan(Plan("HandleUserMessagesPlan", self.handle_user_messages))

    def act(self):
        display_message(self.aid.name, "Acting in CommunicationInterfaceAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_communication_request(message)

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

    def initialize_communication_interface(self):
        display_message(self.aid.name, "Initializing communication interface")
        # Logic to initialize communication interface
        communication_interface = self.setup_communication_interface()
        self.add_belief(Belief("CommunicationInterface", communication_interface))

    def handle_user_messages(self):
        display_message(self.aid.name, "Handling user messages")
        communication_interface = self.get_belief("CommunicationInterface")
        if communication_interface:
            user_messages = self.retrieve_user_messages(communication_interface)
            self.process_user_messages(user_messages)

    def handle_communication_request(self, message):
        content = message.content
        self.add_belief(Belief("CommunicationRequest", content))
        self.add_goal(Goal("ProcessCommunicationRequest", "Achieve"))

    def setup_communication_interface(self):
        # Simulated communication interface setup
        return {"InterfaceType": "Chat", "Status": "Active"}

    def retrieve_user_messages(self, communication_interface):
        # Simulated user message retrieval
        return ["Message1", "Message2"]

    def process_user_messages(self, messages):
        for message in messages:
            display_message(self.aid.name, f"Processing message: {message}")

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```