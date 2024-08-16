# Docs: Goal Modeler

## 1. Overall Description and Purpose

This code implements a Goal Modeler system, which is used for creating, managing, and visualizing hierarchical goal structures. It consists of two main classes:

1. `Goal`: Represents individual goals within the hierarchy.
2. `GoalModeler`: Manages the overall goal structure and provides methods for visualization and export.

The purpose of this code is to provide a flexible and extensible framework for modeling complex goal hierarchies. It can be used in various applications such as:

- Project management
- Strategic planning
- Requirements engineering
- AI planning and reasoning systems
- Any domain where hierarchical goal structures need to be represented, visualized, and analyzed

## 2. PlantUML Class Diagram

The following PlantUML diagram illustrates the structure of the Goal Modeler system:

```
@startuml
class Goal {
  - name: str
  - description: str
  - parent: Optional[Goal]
  - subgoals: List[Goal]
  + add_subgoal(subgoal: Goal)
  + __str__(): str
}

class GoalModeler {
  - root_goals: List[Goal]
  + add_goal(goal: Goal, parent: Optional[Goal])
  + get_goal_hierarchy(): nx.DiGraph
  + visualize_goals(output_file: str)
  + export_to_json(): dict
}

Goal "0..*" --o "0..1" Goal : parent
GoalModeler o-- "0..*" Goal : root_goals
@enduml

```

## 3. Data Schema Description

1. `Goal` (Class):
    - `name` (str): The name of the goal
    - `description` (str): A description of the goal
    - `parent` (Optional[Goal]): The parent goal, if any
    - `subgoals` (List[Goal]): A list of subgoals
2. `GoalModeler` (Class):
    - `root_goals` (List[Goal]): A list of top-level goals in the hierarchy

## 4. Breakdown of Functions/Methods

### Goal Class

### `__init__(self, name: str, description: str, parent: Optional['Goal'] = None)`

- Purpose: Initialize a new Goal object
- Parameters:
    - `name` (str): The name of the goal
    - `description` (str): A description of the goal
    - `parent` (Optional[Goal]): The parent goal, if any
- Return value: None
- Key logic: Initializes the goal with the given name, description, and parent

### `add_subgoal(self, subgoal: 'Goal')`

- Purpose: Add a subgoal to the current goal
- Parameters:
    - `subgoal` (Goal): The goal to add as a subgoal
- Return value: None
- Key logic: Sets the parent of the subgoal and appends it to the subgoals list

### `__str__(self)`

- Purpose: Provide a string representation of the Goal
- Parameters: None
- Return value: str - A string representation of the goal
- Key logic: Returns a string containing the goal's name

### GoalModeler Class

### `__init__(self)`

- Purpose: Initialize a new GoalModeler object
- Parameters: None
- Return value: None
- Key logic: Initializes an empty list to store root goals

### `add_goal(self, goal: Goal, parent: Optional[Goal] = None)`

- Purpose: Add a goal to the hierarchy
- Parameters:
    - `goal` (Goal): The goal to add
    - `parent` (Optional[Goal]): The parent goal, if any
- Return value: None
- Key logic: Adds the goal as a subgoal if a parent is specified, otherwise adds it as a root goal

### `get_goal_hierarchy(self) -> nx.DiGraph`

- Purpose: Generate a NetworkX DiGraph representing the goal hierarchy
- Parameters: None
- Return value: nx.DiGraph - A directed graph representing the goal hierarchy
- Key logic: Recursively builds a graph structure from the goal hierarchy

### `visualize_goals(self, output_file: str = "goal_hierarchy.png")`

- Purpose: Visualize the goal hierarchy and save it as an image
- Parameters:
    - `output_file` (str, optional): Path to save the output image (default: "goal_hierarchy.png")
- Return value: None
- Key logic: Uses NetworkX and Matplotlib to create a visual representation of the goal hierarchy and save it as an image

### `export_to_json(self) -> dict`

- Purpose: Export the goal hierarchy to a JSON-compatible dictionary structure
- Parameters: None
- Return value: dict - A dictionary representing the goal hierarchy
- Key logic: Recursively converts the goal hierarchy into a nested dictionary structure

## 5. Key Python Libraries Used

1. `networkx`: Used for creating and manipulating the graph structure of the goal hierarchy.
2. `matplotlib`: Used for visualizing the goal hierarchy.
3. `typing`: Used for type hinting, improving code readability and enabling better static type checking.
4. `json`: Used for exporting the goal hierarchy to JSON format (in the example usage).

## 6. Other Class Imports and Their Relationships

This code doesn't import any other custom classes. It relies on the NetworkX library for graph functionality and Matplotlib for visualization.

## 7. Important Notes on Usage, Limitations, and Future Improvements

Usage:

- Create a `GoalModeler` instance to start building your goal hierarchy.
- Use `Goal` class to create individual goals.
- Use `add_goal()` to add goals to the hierarchy, specifying parent goals when necessary.
- Use `visualize_goals()` to create a visual representation of the goal hierarchy.
- Use `export_to_json()` to export the hierarchy for storage or further processing.

Limitations:

- The current implementation doesn't support goal attributes beyond name and description.
- Visualization may become cluttered for very large or complex goal hierarchies.
- There's no built-in mechanism for goal analysis or evaluation.

Potential future improvements:

1. Implement support for additional goal attributes (e.g., priority, status, deadline).
2. Add mechanisms for goal conflict detection and resolution.
3. Implement goal decomposition patterns (e.g., AND/OR decomposition).
4. Add support for goal dependencies and cross-hierarchy relationships.
5. Implement more sophisticated visualization options, possibly with interactive capabilities.
6. Add support for importing goal hierarchies from various formats (e.g., XML, YAML).
7. Implement goal achievement tracking and progress visualization.
8. Add support for attaching resources or tasks to goals.
9. Implement goal analysis algorithms (e.g., impact analysis, criticality analysis).
10. Add support for collaborative goal modeling with multi-user capabilities.

Example Usage:

```python
modeler = GoalModeler()

# Create goals
main_goal = Goal("Improve System", "Enhance overall system performance")
optimize_goal = Goal("Optimize Resources", "Improve resource utilization")
security_goal = Goal("Enhance Security", "Strengthen system security measures")

modeler.add_goal(main_goal)
modeler.add_goal(optimize_goal, main_goal)
modeler.add_goal(security_goal, main_goal)

# Add subgoals
modeler.add_goal(Goal("Reduce CPU Usage", "Minimize CPU consumption"), optimize_goal)
modeler.add_goal(Goal("Optimize Memory", "Improve memory management"), optimize_goal)
modeler.add_goal(Goal("Implement Firewall", "Set up robust firewall"), security_goal)
modeler.add_goal(Goal("Enhance Encryption", "Upgrade encryption protocols"), security_goal)

# Visualize the goal hierarchy
modeler.visualize_goals()

# Export to JSON
import json
with open("goal_hierarchy.json", "w") as f:
    json.dump(modeler.export_to_json(), f, indent=2)

print("Goal hierarchy visualization and JSON export completed.")

```

This example demonstrates how to create a goal hierarchy, add goals and subgoals, visualize the hierarchy, and export it to JSON format. It shows the basic usage of the GoalModeler and Goal classes to represent and manipulate a hierarchical goal structure.