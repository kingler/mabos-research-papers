# Code: agent_schemas.py
```python
# api/schemas/agent_schemas.py
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class AgentType(str, Enum):
    REACTIVE = "reactive"
    PROACTIVE = "proactive"
    BDI = "bdi"
    HYBRID = "hybrid"

class AgentStatus(str, Enum):
    IDLE = "idle"
    ACTIVE = "active"
    PAUSED = "paused"
    ERROR = "error"

class AgentBase(BaseModel):
    name: str = Field(..., description="The name of the agent")
    type: AgentType = Field(..., description="The type of the agent")
    description: Optional[str] = Field(None, description="A brief description of the agent's purpose")

class AgentCreate(AgentBase):
    initial_beliefs: Optional[List[dict]] = Field(None, description="Initial beliefs of the agent")
    initial_goals: Optional[List[dict]] = Field(None, description="Initial goals of the agent")

class AgentUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Updated name of the agent")
    description: Optional[str] = Field(None, description="Updated description of the agent")
    beliefs: Optional[List[dict]] = Field(None, description="Updated beliefs of the agent")
    goals: Optional[List[dict]] = Field(None, description="Updated goals of the agent")

class Agent(AgentBase):
    id: str = Field(..., description="The unique identifier of the agent")
    status: AgentStatus = Field(..., description="The current status of the agent")
    beliefs: List[dict] = Field([], description="Current beliefs of the agent")
    goals: List[dict] = Field([], description="Current goals of the agent")
    performance_metrics: Optional[dict] = Field(None, description="Performance metrics of the agent")

    class Config:
        schema_extra = {
            "example": {
                "id": "agent_123",
                "name": "ResourceMonitorAgent",
                "type": "proactive",
                "description": "Monitors system resources and reports anomalies",
                "status": "active",
                "beliefs": [{"resource": "CPU", "usage": 70}, {"resource": "Memory", "usage": 80}],
                "goals": [{"type": "maintain", "condition": "system_stability"}],
                "performance_metrics": {"tasks_completed": 150, "anomalies_detected": 5}
            }
        }

```