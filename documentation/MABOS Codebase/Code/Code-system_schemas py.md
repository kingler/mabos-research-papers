# Code: system_schemas.py

```python
# system_schemas.py
from pydantic import BaseModel, Field
from typing import List, Dict, Any

class SystemConfig(BaseModel):
    max_agents: int = Field(..., description="Maximum number of agents allowed in the system")
    default_agent_type: str = Field(..., description="Default type for new agents")
    logging_level: str = Field(..., description="System-wide logging level")
    performance_tracking_interval: int = Field(..., description="Interval for tracking performance metrics (in seconds)")

class SystemStatus(BaseModel):
    status: str = Field(..., description="Overall system status (e.g., 'running', 'paused', 'error')")
    agent_count: int = Field(..., description="Current number of agents in the system")
    active_models_count: int = Field(..., description="Number of active models in the system")
    uptime: float = Field(..., description="System uptime in seconds")
    current_load: float = Field(..., description="Current system load (0.0 to 1.0)")

class SystemMetrics(BaseModel):
    cpu_usage: float = Field(..., description="Current CPU usage as a percentage")
    memory_usage: float = Field(..., description="Current memory usage as a percentage")
    active_connections: int = Field(..., description="Number of active connections")
    messages_processed: int = Field(..., description="Total number of messages processed")
    average_response_time: float = Field(..., description="Average response time for message processing (in milliseconds)")

class SystemBackup(BaseModel):
    backup_id: str = Field(..., description="Unique identifier for the backup")
    timestamp: str = Field(..., description="Timestamp of when the backup was created")
    size: int = Field(..., description="Size of the backup in bytes")
    description: str = Field(..., description="Brief description or notes about the backup")

class SystemRestore(BaseModel):
    backup_id: str = Field(..., description="ID of the backup to restore from")
    restore_options: Dict[str, Any] = Field(..., description="Options for the restore operation")

    class Config:
        schema_extra = {
            "example": {
                "backup_id": "backup_20230615_120000",
                "restore_options": {
                    "include_agents": True,
                    "include_models": True,
                    "reset_performance_metrics": False
                }
            }
        }
```