# Code: security_agent.py

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class SecurityAgent(Agent):
    def __init__(self, aid):
        super(SecurityAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up SecurityAgent")
        self.add_goal(Goal("MaintainSystemSecurity", "Maintain"))
        self.add_plan(Plan("MonitorSecurityStatusPlan", self.monitor_security_status))
        self.add_plan(Plan("EnforceSecurityPoliciesPlan", self.enforce_security_policies))
        self.add_plan(Plan("HandleSecurityThreatPlan", self.handle_security_threat))

    def act(self):
        display_message(self.aid.name, "Acting in SecurityAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.INFORM:
            self.handle_security_alert(message)

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

    def monitor_security_status(self):
        display_message(self.aid.name, "Monitoring system security status")
        security_status = self.check_security_status()
        self.add_belief(Belief("SecurityStatus", security_status))
        if security_status["ThreatLevel"] > 2:
            self.add_goal(Goal("AddressSecurityThreats", "Achieve"))

    def enforce_security_policies(self):
        display_message(self.aid.name, "Enforcing security policies")
        policies = self.get_security_policies()
        for policy in policies:
            self.apply_security_policy(policy)

    def handle_security_threat(self):
        display_message(self.aid.name, "Handling security threats")
        threats = self.get_active_threats()
        for threat in threats:
            countermeasure = self.determine_countermeasure(threat)
            self.execute_countermeasure(countermeasure)

    def handle_security_alert(self, message):
        content = message.content
        self.add_belief(Belief("SecurityAlert", content))
        self.add_goal(Goal("ProcessSecurityAlert", "Achieve"))

    def check_security_status(self):
        # Simulated security status check
        return {"ThreatLevel": 3, "ActiveThreats": ["UnauthorizedAccess", "DataBreach"]}

    def get_security_policies(self):
        # Simulated security policies
        return ["PasswordPolicy", "AccessControlPolicy", "EncryptionPolicy"]

    def apply_security_policy(self, policy):
        display_message(self.aid.name, f"Applying security policy: {policy}")
        # Logic to apply the security policy

    def get_active_threats(self):
        security_status = self.get_belief("SecurityStatus")
        return security_status["ActiveThreats"] if security_status else []

    def determine_countermeasure(self, threat):
        # Simulated countermeasure determination
        countermeasures = {
            "UnauthorizedAccess": "LockDownAccess",
            "DataBreach": "ActivateDataEncryption"
        }
        return countermeasures.get(threat, "InvestigateThreat")

    def execute_countermeasure(self, countermeasure):
        display_message(self.aid.name, f"Executing countermeasure: {countermeasure}")
        # Logic to execute the countermeasure

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None
```