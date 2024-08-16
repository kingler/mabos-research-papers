# exceptions.py

```python
# mas/exceptions.py

class MABOSException(Exception):
    """Base exception for MABOS system"""

class AgentCommunicationError(MABOSException):
    """Raised when there's an error in agent communication"""

class TaskExecutionError(MABOSException):
    """Raised when there's an error in task execution"""
```