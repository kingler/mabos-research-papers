# Code: system_routes.py
```python
# system_routes.py
from fastapi import APIRouter, HTTPException, Depends
from ..schemas.system_schemas import SystemStatus, SystemConfig, SystemMetrics
from ..dependencies import get_mas_manager

router = APIRouter()

@router.get("/status", response_model=SystemStatus)
async def get_system_status(mas_manager=Depends(get_mas_manager)):
    """Retrieve the current status of the MAS."""
    try:
        return await mas_manager.get_system_status()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving system status: {str(e)}")

@router.get("/config", response_model=SystemConfig)
async def get_system_config(mas_manager=Depends(get_mas_manager)):
    """Retrieve the current system configuration."""
    try:
        return await mas_manager.get_system_config()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving system configuration: {str(e)}")

@router.put("/config", response_model=SystemConfig)
async def update_system_config(config: SystemConfig, mas_manager=Depends(get_mas_manager)):
    """Update the system configuration."""
    try:
        return await mas_manager.update_system_config(config)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating system configuration: {str(e)}")

@router.get("/metrics", response_model=SystemMetrics)
async def get_system_metrics(mas_manager=Depends(get_mas_manager)):
    """Retrieve current system metrics."""
    try:
        return await mas_manager.get_system_metrics()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving system metrics: {str(e)}")

@router.post("/restart")
async def restart_system(mas_manager=Depends(get_mas_manager)):
    """Restart the entire MAS."""
    try:
        await mas_manager.restart_system()
        return {"message": "System restart initiated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error restarting system: {str(e)}")

@router.post("/backup")
async def create_system_backup(mas_manager=Depends(get_mas_manager)):
    """Create a backup of the current system state."""
    try:
        backup_id = await mas_manager.create_system_backup()
        return {"message": f"System backup created successfully", "backup_id": backup_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating system backup: {str(e)}")

@router.post("/restore/{backup_id}")
async def restore_system_backup(backup_id: str, mas_manager=Depends(get_mas_manager)):
    """Restore the system from a previous backup."""
    try:
        await mas_manager.restore_system_backup(backup_id)
        return {"message": f"System restored successfully from backup {backup_id}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error restoring system from backup: {str(e)}")


```