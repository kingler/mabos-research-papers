# Code: goal_modeler.py

```python
# tools/goal_modeler.py
from typing import List, Optional
import networkx as nx
import matplotlib.pyplot as plt

class Goal:
    def __init__(self, name: str, description: str, parent: Optional['Goal'] = None):
        self.name = name
        self.description = description
        self.parent = parent
        self.subgoals: List[Goal] = []

    def add_subgoal(self, subgoal: 'Goal'):
        subgoal.parent = self
        self.subgoals.append(subgoal)

    def __str__(self):
        return f"Goal({self.name})"

class GoalModeler:
    def __init__(self):
        self.root_goals: List[Goal] = []

    def add_goal(self, goal: Goal, parent: Optional[Goal] = None):
        if parent:
            parent.add_subgoal(goal)
        else:
            self.root_goals.append(goal)

    def get_goal_hierarchy(self) -> nx.DiGraph:
        G = nx.DiGraph()

        def add_goal_to_graph(goal: Goal):
            G.add_node(goal.name, description=goal.description)
            for subgoal in goal.subgoals:
                G.add_edge(goal.name, subgoal.name)
                add_goal_to_graph(subgoal)

        for root_goal in self.root_goals:
            add_goal_to_graph(root_goal)

        return G

    def visualize_goals(self, output_file: str = "goal_hierarchy.png"):
        G = self.get_goal_hierarchy()
        pos = nx.spring_layout(G, k=0.9, iterations=50)

        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=3000, font_size=8, font_weight='bold')

        # Add labels with descriptions
        labels = {node: f"{node}\\n{data['description']}" for node, data in G.nodes(data=True)}
        nx.draw_networkx_labels(G, pos, labels, font_size=6)

        plt.title("Goal Hierarchy")
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()

    def export_to_json(self) -> dict:
        def goal_to_dict(goal: Goal) -> dict:
            return {
                "name": goal.name,
                "description": goal.description,
                "subgoals": [goal_to_dict(subgoal) for subgoal in goal.subgoals]
            }

        return {
            "goals": [goal_to_dict(goal) for goal in self.root_goals]
        }

# Example usage
if __name__ == "__main__":
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