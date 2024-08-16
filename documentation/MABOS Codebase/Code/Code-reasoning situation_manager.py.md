# Code: reasoning/situation_manager.py

```python
from typing import Dict, Any, List
from datetime import datetime

class Situation:
    def __init__(self, name: str, conditions: Dict[str, Any]):
        self.name = name
        self.conditions = conditions
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Situation(name={self.name}, conditions={self.conditions}, timestamp={self.timestamp})"

class SituationManager:
    def __init__(self):
        self.current_situation: Situation = None
        self.situation_history: List[Situation] = []

    def update_situation(self, new_situation: Situation) -> None:
        if self.current_situation:
            self.situation_history.append(self.current_situation)
        self.current_situation = new_situation

    def get_current_situation(self) -> Situation:
        return self.current_situation

    def is_situation_active(self, situation_name: str, state: Dict[str, Any]) -> bool:
        if self.current_situation and self.current_situation.name == situation_name:
            return all(state.get(k) == v for k, v in self.current_situation.conditions.items())
        return False

    def get_situation_history(self) -> List[Situation]:
        return self.situation_history

    def clear_history(self) -> None:
        self.situation_history.clear()
```