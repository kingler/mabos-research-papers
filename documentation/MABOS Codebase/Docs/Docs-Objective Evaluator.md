# Docs: Objective Evaluator

## 1. Overall Description and Purpose

This code defines an objective evaluation system, which is crucial for decision-making processes in various domains such as planning, optimization, and multi-criteria decision analysis. The implementation includes two main classes:

1. `Objective`: Represents a single objective or criterion for evaluation.
2. `ObjectiveEvaluator`: Manages multiple objectives and performs evaluations of plans or solutions based on these objectives.

The purpose of this code is to provide a flexible and extensible framework for evaluating plans or solutions against multiple, potentially conflicting objectives. It can be used in various applications, such as project management, resource allocation, or any scenario where decisions need to be made based on multiple criteria.

## 2. PlantUML Class Diagram

The following PlantUML diagram illustrates the structure of the Objective Evaluator:

```
@startuml
class Objective {
  - name: str
  - evaluation_function: Callable[[Dict], float]
  - weight: float
}

class ObjectiveEvaluator {
  - objectives: List[Objective]
  + add_objective(objective: Objective)
  + evaluate(plan: Dict): float
  + evaluate_multiple(plans: List[Dict]): List[tuple[Dict, float]]
}

ObjectiveEvaluator o-- "0..*" Objective
@enduml

```

## 3. Data Schema Description

1. `Objective` (Class):
    - `name` (str): The name of the objective
    - `evaluation_function` (Callable[[Dict], float]): A function that evaluates a plan against this objective
    - `weight` (float): The weight of this objective in the overall evaluation
2. `ObjectiveEvaluator` (Class):
    - `objectives` (List[Objective]): List of all objectives used in the evaluation

## 4. Breakdown of Functions/Methods

### Objective Class

### `__init__(self, name: str, evaluation_function: Callable[[Dict], float], weight: float = 1.0)`

- Purpose: Initialize a new Objective object
- Parameters:
    - `name` (str): The name of the objective
    - `evaluation_function` (Callable[[Dict], float]): Function that evaluates a plan for this objective
    - `weight` (float, optional): The weight of this objective (default is 1.0)
- Return value: None
- Key logic: Stores the name, evaluation function, and weight of the objective

### ObjectiveEvaluator Class

### `__init__(self)`

- Purpose: Initialize a new ObjectiveEvaluator object
- Parameters: None
- Return value: None
- Key logic: Initializes an empty list to store objectives

### `add_objective(self, objective: Objective)`

- Purpose: Add a new objective to the evaluator
- Parameters:
    - `objective` (Objective): The objective to add
- Return value: None
- Key logic: Appends the objective to the list of objectives

### `evaluate(self, plan: Dict) -> float`

- Purpose: Evaluate a single plan based on all objectives
- Parameters:
    - `plan` (Dict): The plan to evaluate
- Return value: float - The weighted sum of all objective evaluations
- Key logic:
    1. Calculates the total weight of all objectives
    2. Evaluates the plan against each objective
    3. Calculates a weighted score for each objective
    4. Returns the sum of all weighted scores

### `evaluate_multiple(self, plans: List[Dict]) -> List[tuple[Dict, float]]`

- Purpose: Evaluate multiple plans and return them sorted by their scores
- Parameters:
    - `plans` (List[Dict]): A list of plans to evaluate
- Return value: List[tuple[Dict, float]] - A list of tuples, each containing a plan and its score, sorted in descending order by score
- Key logic:
    1. Evaluates each plan using the `evaluate` method
    2. Creates a list of (plan, score) tuples
    3. Sorts the list based on scores in descending order

## 5. Key Python Libraries Used

The code primarily uses Python's built-in features and the `typing` module for type hinting:

1. `typing`: Used for type hinting, improving code readability and enabling better static type checking. Specifically, it uses `Callable`, `Dict`, and `List`.

## 6. Other Class Imports and Their Relationships

This code doesn't import any other custom classes. It is self-contained but designed to be used within a larger system that needs to evaluate plans or solutions based on multiple objectives.

## 7. Important Notes on Usage, Limitations, and Future Improvements

Usage:

- Create an instance of `ObjectiveEvaluator`.
- Create `Objective` objects with appropriate evaluation functions and weights.
- Add objectives to the evaluator using `add_objective()`.
- Use `evaluate()` to evaluate a single plan or `evaluate_multiple()` to evaluate and rank multiple plans.

Limitations:

- The current implementation assumes that higher scores are better for all objectives.
- There's no built-in mechanism for handling conflicting objectives beyond weighting.
- The evaluation functions must return float values, which may not be suitable for all types of objectives.

Potential future improvements:

1. Implement support for minimization objectives (where lower scores are better).
2. Add support for non-linear aggregation of objective scores (e.g., multiplicative or lexicographic methods).
3. Implement sensitivity analysis to understand the impact of weight changes on the final rankings.
4. Add support for hierarchical objective structures.
5. Implement visualization tools for comparing plans across multiple objectives.
6. Add support for fuzzy or interval-based evaluations to handle uncertainty.
7. Implement Pareto optimization for multi-objective problems.
8. Add support for dynamic or adaptive weighting of objectives.
9. Implement constraint handling within the objective evaluation framework.
10. Add support for objective normalization to handle different scales across objectives.

Example Usage:

```python
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

# Print results
print("Evaluated plans:")
for plan, score in results:
    print(f"{plan['name']}: Score = {score:.2f}")

```

This example demonstrates how to create objectives, add them to an evaluator, and use the evaluator to rank multiple plans based on their performance across all objectives.