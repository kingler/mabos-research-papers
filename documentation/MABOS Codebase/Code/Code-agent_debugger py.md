# Code: agent_debugger.py

```python
# tools/agent_debugger.py
import time
from typing import List, Dict, Any
import matplotlib.pyplot as plt
from collections import defaultdict

class AgentDebugger:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.action_log: List[Dict[str, Any]] = []
        self.belief_history: Dict[str, List[Any]] = defaultdict(list)
        self.goal_history: List[Dict[str, Any]] = []
        self.performance_metrics: Dict[str, List[float]] = defaultdict(list)

    def log_action(self, action: str, details: Dict[str, Any] = None):
        """Log an action performed by the agent."""
        log_entry = {
            "timestamp": time.time(),
            "action": action,
            "details": details or {}
        }
        self.action_log.append(log_entry)

    def log_belief_update(self, belief_name: str, value: Any):
        """Log updates to the agent's beliefs."""
        self.belief_history[belief_name].append((time.time(), value))

    def log_goal_update(self, goal_name: str, status: str):
        """Log updates to the agent's goals."""
        self.goal_history.append({
            "timestamp": time.time(),
            "goal": goal_name,
            "status": status
        })

    def log_performance_metric(self, metric_name: str, value: float):
        """Log a performance metric."""
        self.performance_metrics[metric_name].append((time.time(), value))

    def get_action_log(self) -> List[Dict[str, Any]]:
        """Retrieve the full action log."""
        return self.action_log

    def get_belief_history(self, belief_name: str) -> List[Any]:
        """Retrieve the history of a specific belief."""
        return self.belief_history.get(belief_name, [])

    def get_goal_history(self) -> List[Dict[str, Any]]:
        """Retrieve the full goal history."""
        return self.goal_history

    def get_performance_metrics(self, metric_name: str) -> List[float]:
        """Retrieve the history of a specific performance metric."""
        return self.performance_metrics.get(metric_name, [])

    def analyze_performance(self, metric_name: str):
        """Analyze and visualize a performance metric over time."""
        metric_data = self.get_performance_metrics(metric_name)
        if not metric_data:
            print(f"No data available for metric: {metric_name}")
            return

        timestamps, values = zip(*metric_data)
        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, values)
        plt.title(f"{metric_name} Over Time")
        plt.xlabel("Timestamp")
        plt.ylabel(metric_name)
        plt.grid(True)
        plt.show()

    def generate_summary_report(self) -> str:
        """Generate a summary report of the agent's activities."""
        report = f"Agent Debug Summary for {self.agent_id}\\n"
        report += "=" * 40 + "\\n\\n"

        report += f"Total Actions Logged: {len(self.action_log)}\\n"
        report += f"Beliefs Tracked: {', '.join(self.belief_history.keys())}\\n"
        report += f"Goals Updated: {len(self.goal_history)}\\n"
        report += f"Performance Metrics: {', '.join(self.performance_metrics.keys())}\\n\\n"

        report += "Recent Actions:\\n"
        for action in self.action_log[-5:]:
            report += f"  - {action['action']} at {time.ctime(action['timestamp'])}\\n"

        report += "\\nRecent Goal Updates:\\n"
        for goal in self.goal_history[-5:]:
            report += f"  - {goal['goal']}: {goal['status']} at {time.ctime(goal['timestamp'])}\\n"

        return report

# Example usage
if __name__ == "__main__":
    debugger = AgentDebugger("Agent001")

    # Simulate agent activities
    debugger.log_action("InitializeAgent", {"status": "success"})
    debugger.log_belief_update("battery_level", 100)
    debugger.log_goal_update("ExploreEnvironment", "active")
    debugger.log_performance_metric("task_completion_rate", 0.8)

    time.sleep(1)  # Simulate time passing

    debugger.log_action("MoveTo", {"location": "Point A"})
    debugger.log_belief_update("battery_level", 95)
    debugger.log_performance_metric("task_completion_rate", 0.85)

    time.sleep(1)  # Simulate time passing

    debugger.log_action("CollectData", {"data_points": 10})
    debugger.log_belief_update("battery_level", 90)
    debugger.log_goal_update("ExploreEnvironment", "completed")
    debugger.log_performance_metric("task_completion_rate", 0.9)

    # Generate and print summary report
    print(debugger.generate_summary_report())

    # Analyze performance
    debugger.analyze_performance("task_completion_rate")

```