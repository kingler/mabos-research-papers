# Docs: BDIEngine

## 1. Overall Description and Purpose

This code defines a `BDIEngine` class, which implements the core functionality of a Belief-Desire-Intention (BDI) agent. The BDI model is a popular framework for designing intelligent agents in artificial intelligence and cognitive science. The purpose of this code is to provide a complete, functional implementation of a BDI agent that can:

- Maintain beliefs about the world
- Manage desires (goals)
- Generate intentions (plans to achieve goals)
- Execute plans
- Continuously reason about its environment and goals

The `BDIEngine` class encapsulates the entire BDI reasoning cycle, including belief updates, goal selection, plan selection, and plan execution. It's designed to run asynchronously, allowing for non-blocking operation in complex environments.

## 2. PlantUML Class Diagram

The following PlantUML diagram illustrates the structure of the BDI Engine:

```
@startuml
class BDIEngine {
  - name: str
  - beliefs: BeliefSet
  - desires: List[Goal]
  - intentions: List[Plan]
  - plan_library: PlanLibrary
  + update_beliefs(new_beliefs: Dict[str, bool])
  + generate_options(): List[Goal]
  + filter_options(options: List[Goal]): Goal
  + plan(goal: Goal): Plan
  + execute_intention(plan: Plan)
  + bdi_loop()
  + add_goal(goal: Goal)
  + add_plan(plan: Plan)
  + run()
}

class BeliefSet
class Goal
class Plan
class PlanLibrary

BDIEngine o-- BeliefSet
BDIEngine o-- "0..*" Goal
BDIEngine o-- "0..*" Plan
BDIEngine o-- PlanLibrary
@enduml

```

## 3. Data Schema Description

`BDIEngine` (Class):

- `name` (str): The name of the agent
- `beliefs` (BeliefSet): The agent's current beliefs about the world
- `desires` (List[Goal]): The agent's current goals or desires
- `intentions` (List[Plan]): The agent's current intentions (selected plans)
- `plan_library` (PlanLibrary): A library of plans available to the agent

## 4. Breakdown of Functions/Methods

### `__init__(self, name: str)`

- Purpose: Initialize a new BDIEngine object
- Parameters:
    - `name` (str): The name of the agent
- Return value: None
- Key logic: Initializes the agent with the given name and empty beliefs, desires, intentions, and plan library

### `async def update_beliefs(self, new_beliefs: Dict[str, bool])`

- Purpose: Update the agent's beliefs based on new information
- Parameters:
    - `new_beliefs` (Dict[str, bool]): A dictionary of new beliefs (predicate-value pairs)
- Return value: None
- Key logic: Adds each new belief to the agent's belief set

### `def generate_options(self) -> List[Goal]`

- Purpose: Generate possible goals based on current beliefs and desires
- Parameters: None
- Return value: List[Goal] - A list of achievable goals
- Key logic: Filters the agent's desires to only include those that are achievable given current beliefs

### `def filter_options(self, options: List[Goal]) -> Goal`

- Purpose: Select the most appropriate goal from the options
- Parameters:
    - `options` (List[Goal]): A list of achievable goals
- Return value: Goal or None - The selected goal, or None if no options are available
- Key logic: Currently implements a simple selection strategy of choosing the first achievable goal

### `def plan(self, goal: Goal) -> Plan`

- Purpose: Find a suitable plan for the given goal
- Parameters:
    - `goal` (Goal): The goal to plan for
- Return value: Plan or None - A suitable plan, or None if no applicable plan is found
- Key logic: Filters the plans in the plan library to find those applicable to the goal and current beliefs

### `async def execute_intention(self, plan: Plan)`

- Purpose: Execute the selected plan
- Parameters:
    - `plan` (Plan): The plan to execute
- Return value: None
- Key logic: Asynchronously executes the plan and prints the result

### `async def bdi_loop(self)`

- Purpose: Main BDI reasoning loop
- Parameters: None
- Return value: None
- Key logic: Continuously updates beliefs, generates options, selects goals, plans, and executes intentions

### `def add_goal(self, goal: Goal)`

- Purpose: Add a new goal to the agent's desires
- Parameters:
    - `goal` (Goal): The goal to add
- Return value: None
- Key logic: Appends the new goal to the agent's desires list

### `def add_plan(self, plan: Plan)`

- Purpose: Add a new plan to the agent's plan library
- Parameters:
    - `plan` (Plan): The plan to add
- Return value: None
- Key logic: Adds the new plan to the agent's plan library

### `async def run(self)`

- Purpose: Run the BDI agent
- Parameters: None
- Return value: None
- Key logic: Prints a start message and initiates the BDI loop

## 5. Key Python Libraries Used

1. `asyncio`: Used for asynchronous programming, allowing the agent to perform non-blocking operations.
2. `typing`: Used for type hinting, improving code readability and enabling better static type checking.

## 6. Other Class Imports and Their Relationships

1. `Goal` (from `models.goal_model`): Represents a desire or objective of the agent.
2. `BeliefSet` (from `models.belief_model`): Represents the agent's beliefs about the world.
3. `Plan` and `PlanLibrary` (from `models.plan_model`): Represent individual plans and the collection of available plans, respectively.

These imported classes are core components of the BDI model and are used extensively throughout the `BDIEngine` class.

## 7. Important Notes on Usage, Limitations, and Future Improvements

Usage:

- Create an instance of `BDIEngine` with a unique name.
- Add goals and plans to the agent using `add_goal()` and `add_plan()`.
- Run the agent using the `run()` method, which will start the BDI loop.
- The agent operates asynchronously, so it should be run in an asyncio event loop.

Limitations:

- The current implementation uses a simple strategy for goal selection (first achievable goal).
- There's no mechanism for handling conflicting goals or plans.
- The belief update process is simplistic and may not handle complex reasoning about beliefs.
- The agent doesn't have a sophisticated method for interacting with its environment.

Potential future improvements:

1. Implement a more sophisticated goal selection mechanism, possibly using utility functions or priority levels.
2. Add support for handling conflicting goals and plans.
3. Enhance the belief system to support more complex reasoning, such as belief revision and uncertain beliefs.
4. Implement a more robust plan execution mechanism with error handling and recovery strategies.
5. Add support for learning from experience, allowing the agent to improve its decision-making over time.
6. Implement inter-agent communication for multi-agent systems.
7. Create a visualization tool for monitoring the agent's internal state and decision-making process.
8. Optimize performance for large-scale applications with many goals and plans.
9. Implement a more sophisticated environment interaction model, possibly including sensors and actuators.
10. Add support for meta-level reasoning, allowing the agent to reason about its own reasoning process.