# Code: objective_evaluator.py

```python
# objective_evaluator.py
from typing import Callable, Dict, List

class Objective:
    def __init__(self, name: str, evaluation_function: Callable[[Dict], float], weight: float = 1.0):
        self.name = name
        self.evaluation_function = evaluation_function
        self.weight = weight

class ObjectiveEvaluator:
    def __init__(self):
        self.objectives: List[Objective] = []

    def add_objective(self, objective: Objective):
        """Add an objective to the evaluator."""
        self.objectives.append(objective)

    def evaluate(self, plan: Dict) -> float:
        """
        Evaluate a plan based on all objectives.
        Returns a weighted sum of all objective evaluations.
        """
        total_score = 0.0
        total_weight = sum(obj.weight for obj in self.objectives)

        for objective in self.objectives:
            score = objective.evaluation_function(plan)
            weighted_score = score * (objective.weight / total_weight)
            total_score += weighted_score

        return total_score

    def evaluate_multiple(self, plans: List[Dict]) -> List[tuple[Dict, float]]:
        """
        Evaluate multiple plans and return them sorted by their scores.
        """
        evaluated_plans = [(plan, self.evaluate(plan)) for plan in plans]
        return sorted(evaluated_plans, key=lambda x: x[1], reverse=True)

# Example usage:
def cost_objective(plan: Dict) -> float:
    return -plan.get('cost', 0)  # Negative because lower cost is better

def time_objective(plan: Dict) -> float:
    return -plan.get('time', 0)  # Negative because lower time is better

def quality_objective(plan: Dict) -> float:
    return plan.get('quality', 0)

# Create an ObjectiveEvaluator
evaluator = ObjectiveEvaluator()

# Add objectives
evaluator.add_objective(Objective("Cost", cost_objective, weight=2.0))
evaluator.add_objective(Objective("Time", time_objective, weight=1.0))
evaluator.add_objective(Objective("Quality", quality_objective, weight=1.5))

# Example plans
plans = [
    {'name': 'Plan A', 'cost': 100, 'time': 5, 'quality': 8},
    {'name': 'Plan B', 'cost': 150, 'time': 3, 'quality': 9},
    {'name': 'Plan C', 'cost': 80, 'time': 7, 'quality': 7},
]

# Evaluate plans
results = evaluator.evaluate_multiple(plans)

print("Evaluated plans:")
for plan, score in results:
    print(f"{plan['name']}: Score = {score:.2f}")

```