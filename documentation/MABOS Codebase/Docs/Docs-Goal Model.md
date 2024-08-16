# Docs: Goal Model

## 1. Overall Description and Purpose

This code defines a `Goal` class and a `GoalType` enumeration, which are crucial components of a Belief-Desire-Intention (BDI) agent system. The purpose of this code is to provide a flexible and extensible way to represent and manage goals within a BDI agent architecture.

The `Goal` class encapsulates the concept of a goal or desire that an agent might pursue. It includes various attributes and methods to define, evaluate, and manage the goal's lifecycle. The `GoalType` enumeration provides a way to categorize different types of goals, which can influence how they are processed by the agent.

## 2. PlantUML State Machine Diagram

The following PlantUML diagram illustrates the key states and transitions of a Goal:

```
@startuml
[*] --> Inactive : Creation

state Inactive
state Active
state Completed

Inactive --> Active : activate()
Active --> Completed : complete()
Active --> Inactive : should_drop() == True
Completed --> [*]

@enduml

```

## 3. Data Schema Description

The code defines two main data structures:

1. `GoalType` (Enum):
    - `ACHIEVE`: Represents a goal to achieve a specific state
    - `MAINTAIN`: Represents a goal to maintain a specific state
    - `PERFORM`: Represents a goal to perform a specific action
2. `Goal` (Class):
    - `name` (str): The name of the goal
    - `goal_type` (GoalType): The type of the goal
    - `creation_condition` (function, optional): A condition for goal creation
    - `context_condition` (function, optional): A condition for goal applicability
    - `drop_condition` (function, optional): A condition for dropping the goal
    - `status` (str): The current status of the goal ("inactive", "active", or "completed")

## 4. Breakdown of Functions/Methods

### `__init__(self, name, goal_type, creation_condition=None, context_condition=None, drop_condition=None)`

- Purpose: Initialize a new Goal object
- Parameters:
    - `name` (str): The name of the goal
    - `goal_type` (str or GoalType): The type of the goal
    - `creation_condition` (function, optional): A function that determines if the goal should be created
    - `context_condition` (function, optional): A function that determines if the goal is applicable in the current context
    - `drop_condition` (function, optional): A function that determines if the goal should be dropped
- Return value: None
- Key logic: Initializes the goal attributes and sets the initial status to "inactive"

### `is_achievable(self, agent_beliefs)`

- Purpose: Check if the goal is achievable given the agent's current beliefs
- Parameters:
    - `agent_beliefs` (object): The agent's current belief set
- Return value: bool - True if the goal is achievable, False otherwise
- Key logic: If a context condition is defined, it evaluates it; otherwise, it returns True

### `should_drop(self, agent_beliefs)`

- Purpose: Check if the goal should be dropped based on the agent's current beliefs
- Parameters:
    - `agent_beliefs` (object): The agent's current belief set
- Return value: bool - True if the goal should be dropped, False otherwise
- Key logic: If a drop condition is defined, it evaluates it; otherwise, it returns False

### `activate(self)`

- Purpose: Activate the goal
- Parameters: None
- Return value: None
- Key logic: Sets the goal's status to "active"

### `complete(self)`

- Purpose: Mark the goal as completed
- Parameters: None
- Return value: None
- Key logic: Sets the goal's status to "completed"

### `__str__(self)`

- Purpose: Provide a string representation of the Goal object
- Parameters: None
- Return value: str - A string describing the goal
- Key logic: Returns a formatted string containing the goal's name, type, and status

## 5. Key Python Libraries Used

1. `enum`: Used for creating the `GoalType` enumeration, providing a set of named constants for goal types.

## 6. Other Class Imports and Their Relationships

This code doesn't import any other custom classes. It is self-contained but designed to be used within a larger BDI agent system. The `Goal` class would typically be used by:

1. A goal management system within the BDI agent
2. A planning system that selects and pursues goals
3. A belief revision system that updates the agent's beliefs and triggers goal evaluation

## 7. Important Notes on Usage, Limitations, and Future Improvements

Usage:

- Create `Goal` instances with appropriate names, types, and optional conditions.
- Use the `is_achievable()` method to check if a goal is currently achievable.
- Use the `should_drop()` method to determine if a goal should be abandoned.
- Use `activate()` and `complete()` methods to manage the goal's lifecycle.

Limitations:

- The current implementation assumes that the agent's beliefs can be passed as a single object to the condition methods.
- There's no built-in mechanism for goal priorities or conflicts between goals.
- The `creation_condition` is stored but not used within the class methods.

Potential future improvements:

1. Implement a priority system for goals to help resolve conflicts.
2. Add a method to evaluate the `creation_condition` and potentially auto-create goals.
3. Implement a more sophisticated goal lifecycle with additional states (e.g., "suspended", "failed").
4. Add support for subgoals or goal decomposition.
5. Implement a mechanism for tracking progress towards goal achievement.
6. Add support for goal deadlines or time constraints.
7. Implement a system for handling interdependencies between goals.
8. Add methods for estimating the cost or utility of achieving a goal.
9. Implement a mechanism for learning and adapting goal conditions based on experience.
10. Add support for goal persistence across agent sessions or restarts.