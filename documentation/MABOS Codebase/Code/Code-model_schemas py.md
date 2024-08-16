# Code: model_schemas.py

```python
# model_schemas.py
from pydantic import BaseModel, Field
from typing import List, Optional, Any
from enum import Enum

class ModelType(str, Enum):
    GOAL = "goal"
    BELIEF = "belief"
    DOMAIN = "domain"
    PLAN = "plan"
    ONTOLOGY = "ontology"

class ModelBase(BaseModel):
    name: str = Field(..., description="The name of the model")
    type: ModelType = Field(..., description="The type of the model")
    description: Optional[str] = Field(None, description="A brief description of the model's purpose")

class ModelCreate(ModelBase):
    content: dict = Field(..., description="The content of the model")

class ModelUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Updated name of the model")
    description: Optional[str] = Field(None, description="Updated description of the model")
    content: Optional[dict] = Field(None, description="Updated content of the model")

class Model(ModelBase):
    id: str = Field(..., description="The unique identifier of the model")
    version: int = Field(..., description="The version number of the model")
    content: dict = Field(..., description="The content of the model")
    created_at: str = Field(..., description="The creation timestamp of the model")
    updated_at: str = Field(..., description="The last update timestamp of the model")
    is_active: bool = Field(..., description="Whether the model is currently active in the system")

    class Config:
        schema_extra = {
            "example": {
                "id": "model_456",
                "name": "ResourceMonitoringGoals",
                "type": "goal",
                "description": "Goal model for resource monitoring agents",
                "version": 1,
                "content": {
                    "root_goal": "maintain_system_stability",
                    "subgoals": [
                        {"id": "monitor_cpu", "type": "achieve"},
                        {"id": "monitor_memory", "type": "achieve"},
                        {"id": "respond_to_anomalies", "type": "perform"}
                    ]
                },
                "created_at": "2023-06-15T10:00:00Z",
                "updated_at": "2023-06-15T10:00:00Z",
                "is_active": True
            }
        }

class ModelValidationResult(BaseModel):
    is_valid: bool = Field(..., description="Whether the model is valid")
    errors: Optional[List[str]] = Field(None, description="List of validation errors, if any")
    warnings: Optional[List[str]] = Field(None, description="List of validation warnings, if any")

class ModelDeploymentResult(BaseModel):
    success: bool = Field(..., description="Whether the model was successfully deployed")
    message: str = Field(..., description="Deployment result message")
    affected_agents: Optional[List[str]] = Field(None, description="List of agent IDs affected by the deployment")

```