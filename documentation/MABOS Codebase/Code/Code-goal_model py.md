# Code: goal_model.py

```python
# goal_model.py
from enum import Enum

class GoalType(Enum):
    ACHIEVE = "achieve"
    MAINTAIN = "maintain"
    PERFORM = "perform"

class Goal:
    def __init__(self, name, goal_type, creation_condition=None, context_condition=None, drop_condition=None):
        self.name = name
        self.goal_type = GoalType(goal_type)
        self.creation_condition = creation_condition
        self.context_condition = context_condition
        self.drop_condition = drop_condition
        self.status = "inactive"

    def is_achievable(self, agent_beliefs):
        """
        Check if the goal is achievable given the agent's current beliefs.
        """
        if self.context_condition:
            return self.context_condition(agent_beliefs)
        return True

    def should_drop(self, agent_beliefs):
        """
        Check if the goal should be dropped based on the agent's current beliefs.
        """
        if self.drop_condition:
            return self.drop_condition(agent_beliefs)
        return False

    def activate(self):
        """
        Activate the goal.
        """
        self.status = "active"

    def complete(self):
        """
        Mark the goal as completed.
        """
        self.status = "completed"

    def __str__(self):
        return f"Goal({self.name}, {self.goal_type.value}, status: {self.status})"

```