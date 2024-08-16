# Code: bdi_engine.py
```python
# mas/bdi_engine.py
import asyncio
from typing import List, Dict
from models.goal_model import Goal
from models.belief_model import BeliefSet
from models.plan_model import Plan, PlanLibrary
from mas.exceptions import TaskExecutionError

class BDIEngine:
    def __init__(self, name: str):
        self.name = name
        self.beliefs = BeliefSet()
        self.desires: List[Goal] = []
        self.intentions: List[Plan] = []
        self.plan_library = PlanLibrary()

    async def update_beliefs(self, new_beliefs: Dict[str, bool]):
        """Update the agent's beliefs based on new information."""
        for predicate, value in new_beliefs.items():
            self.beliefs.add(predicate, value)

    def generate_options(self) -> List[Goal]:
        """Generate possible goals based on current beliefs and desires."""
        return [goal for goal in self.desires if goal.is_achievable(self.beliefs)]

    def filter_options(self, options: List[Goal]) -> Goal:
        """Select the most appropriate goal from the options."""
        # Simple selection strategy: choose the first achievable goal
        return options[0] if options else None

    def plan(self, goal: Goal) -> Plan:
        """Find a suitable plan for the given goal."""
        applicable_plans = [
            plan for plan in self.plan_library.get_plans_for_goal(goal.name)
            if plan.is_applicable(self.beliefs)
        ]
        return applicable_plans[0] if applicable_plans else None

    async def execute_intention(self, plan: Plan):
        """Execute the selected plan."""
        success = await plan.execute(self)
        if success:
            print(f"Agent {self.name}: Successfully executed plan {plan.name}")
        else:
            print(f"Agent {self.name}: Failed to execute plan {plan.name}")

    async def bdi_loop(self):
        """Main BDI reasoning loop."""
        while True:
            # Perception: update beliefs (this could be done by receiving messages or sensing the environment)
            # For simulation, we'll just wait a bit
            await asyncio.sleep(1)

            # Generate options (possible goals)
            options = self.generate_options()

            # Filter options to select a goal
            selected_goal = self.filter_options(options)

            if selected_goal:
                # Find a plan for the selected goal
                selected_plan = self.plan(selected_goal)

                if selected_plan:
                    # Execute the plan
                    await self.execute_intention(selected_plan)
                else:
                    print(f"Agent {self.name}: No applicable plan found for goal {selected_goal.name}")
            else:
                print(f"Agent {self.name}: No achievable goals at the moment")

    def add_goal(self, goal: Goal):
        """Add a new goal to the agent's desires."""
        self.desires.append(goal)

    def add_plan(self, plan: Plan):
        """Add a new plan to the agent's plan library."""
        self.plan_library.add_plan(plan)

    async def run(self):
        """Run the BDI agent."""
        print(f"Agent {self.name} starting...")
        await self.bdi_loop()

    def add_belief(self, belief):
        self.beliefs.add(belief)

    def remove_belief(self, belief):
        self.beliefs.discard(belief)

    def add_desire(self, desire):
        self.desires.add(desire)

    def remove_desire(self, desire):
        self.desires.discard(desire)

    def generate_options(self):
        return [desire for desire in self.desires if self.is_achievable(desire)]

    def filter_options(self, options):
        return max(options, key=lambda x: self.utility(x))

    def execute_intention(self, intention):
        try:
            plan = self.agent.plan_for(intention)
            return plan.execute()
        except Exception as e:
            raise TaskExecutionError(f"Failed to execute intention {intention}: {str(e)}")

    def utility(self, option):
        # Implement utility calculation
        pass

    def is_achievable(self, desire):
        # Implement achievability check
        pass

```