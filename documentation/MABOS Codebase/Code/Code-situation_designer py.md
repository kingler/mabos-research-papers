# Code: situation_designer.py

```python
# situation_designer.py
from typing import List, Dict, Any, Callable
import json

class Condition:
    def __init__(self, name: str, check_function: Callable[[Dict[str, Any]], bool]):
        self.name = name
        self.check_function = check_function

    def evaluate(self, context: Dict[str, Any]) -> bool:
        return self.check_function(context)

    def __str__(self):
        return f"Condition({self.name})"

class Action:
    def __init__(self, name: str, execute_function: Callable[[Dict[str, Any]], None]):
        self.name = name
        self.execute_function = execute_function

    def execute(self, context: Dict[str, Any]):
        self.execute_function(context)

    def __str__(self):
        return f"Action({self.name})"

class Situation:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.conditions: List[Condition] = []
        self.actions: List[Action] = []

    def add_condition(self, condition: Condition):
        self.conditions.append(condition)

    def add_action(self, action: Action):
        self.actions.append(action)

    def is_applicable(self, context: Dict[str, Any]) -> bool:
        return all(condition.evaluate(context) for condition in self.conditions)

    def apply(self, context: Dict[str, Any]):
        if self.is_applicable(context):
            for action in self.actions:
                action.execute(context)

    def __str__(self):
        return f"Situation({self.name})"

class SituationDesigner:
    def __init__(self):
        self.situations: List[Situation] = []

    def create_situation(self, name: str, description: str) -> Situation:
        situation = Situation(name, description)
        self.situations.append(situation)
        return situation

    def get_applicable_situations(self, context: Dict[str, Any]) -> List[Situation]:
        return [situation for situation in self.situations if situation.is_applicable(context)]

    def apply_situations(self, context: Dict[str, Any]):
        applicable_situations = self.get_applicable_situations(context)
        for situation in applicable_situations:
            situation.apply(context)

    def export_to_json(self, filename: str):
        data = {
            "situations": [
                {
                    "name": situation.name,
                    "description": situation.description,
                    "conditions": [condition.name for condition in situation.conditions],
                    "actions": [action.name for action in situation.actions]
                }
                for situation in self.situations
            ]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def import_from_json(self, filename: str, condition_map: Dict[str, Condition], action_map: Dict[str, Action]):
        with open(filename, 'r') as f:
            data = json.load(f)

        self.situations = []
        for situation_data in data["situations"]:
            situation = self.create_situation(situation_data["name"], situation_data["description"])
            for condition_name in situation_data["conditions"]:
                if condition_name in condition_map:
                    situation.add_condition(condition_map[condition_name])
            for action_name in situation_data["actions"]:
                if action_name in action_map:
                    situation.add_action(action_map[action_name])

# Example usage
if __name__ == "__main__":
    designer = SituationDesigner()

    # Define conditions
    high_cpu_condition = Condition("HighCPU", lambda context: context.get("cpu_usage", 0) > 80)
    low_memory_condition = Condition("LowMemory", lambda context: context.get("available_memory", 100) < 20)

    # Define actions
    optimize_cpu_action = Action("OptimizeCPU", lambda context: print("Optimizing CPU usage..."))
    free_memory_action = Action("FreeMemory", lambda context: print("Freeing up memory..."))

    # Create situations
    high_load_situation = designer.create_situation("HighLoad", "System is under high load")
    high_load_situation.add_condition(high_cpu_condition)
    high_load_situation.add_action(optimize_cpu_action)

    low_resources_situation = designer.create_situation("LowResources", "System resources are running low")
    low_resources_situation.add_condition(low_memory_condition)
    low_resources_situation.add_action(free_memory_action)

    # Export situations to JSON
    designer.export_to_json("situations.json")

    # Simulate context
    context = {"cpu_usage": 90, "available_memory": 15}

    # Apply situations
    designer.apply_situations(context)

    # Import situations from JSON
    new_designer = SituationDesigner()
    condition_map = {"HighCPU": high_cpu_condition, "LowMemory": low_memory_condition}
    action_map = {"OptimizeCPU": optimize_cpu_action, "FreeMemory": free_memory_action}
    new_designer.import_from_json("situations.json", condition_map, action_map)

    print("Imported situations:")
    for situation in new_designer.situations:
        print(f"- {situation.name}: {situation.description}")

```