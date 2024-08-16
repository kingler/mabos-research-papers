# Code: constraint_solver.py

```python
from typing import List, Dict, Any, Callable

class Constraint:
    def __init__(self, variables: List[str], constraint_func: Callable[[Dict[str, Any]], bool]):
        self.variables = variables
        self.constraint_func = constraint_func

    def is_satisfied(self, assignment: Dict[str, Any]) -> bool:
        return self.constraint_func(assignment)

class ConstraintSolver:
    def __init__(self):
        self.constraints: List[Constraint] = []
        self.variables: Dict[str, List[Any]] = {}

    def add_constraint(self, constraint: Constraint) -> None:
        self.constraints.append(constraint)
        for var in constraint.variables:
            if var not in self.variables:
                self.variables[var] = []

    def add_variable(self, variable: str, domain: List[Any]) -> None:
        self.variables[variable] = domain

    def solve(self) -> Dict[str, Any]:
        return self._backtrack({})

    def _backtrack(self, assignment: Dict[str, Any]) -> Dict[str, Any]:
        if len(assignment) == len(self.variables):
            return assignment

        var = next(var for var in self.variables if var not in assignment)
        for value in self.variables[var]:
            new_assignment = assignment.copy()
            new_assignment[var] = value
            if self._is_consistent(new_assignment):
                result = self._backtrack(new_assignment)
                if result is not None:
                    return result
        return None

    def _is_consistent(self, assignment: Dict[str, Any]) -> bool:
        return all(
            constraint.is_satisfied(assignment)
            for constraint in self.constraints
            if set(constraint.variables).issubset(set(assignment.keys()))
        )
```