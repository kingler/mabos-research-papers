# Code: agent_routes.py

```python
# api/routes/agent_routes.py
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ..schemas.agent_schemas import AgentCreate, Agent, AgentUpdate
from ..dependencies import get_mas_manager

router = APIRouter()

@router.get("/", response_model=List[Agent])
async def get_agents(mas_manager=Depends(get_mas_manager)):
    """Retrieve all agents in the system."""
    return await mas_manager.get_all_agents()

@router.post("/", response_model=Agent)
async def create_agent(agent_data: AgentCreate, mas_manager=Depends(get_mas_manager)):
    """Create a new agent."""
    try:
        return await mas_manager.create_agent(agent_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{agent_id}", response_model=Agent)
async def get_agent(agent_id: str, mas_manager=Depends(get_mas_manager)):
    """Retrieve a specific agent by ID."""
    agent = await mas_manager.get_agent(agent_id)
    if agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@router.put("/{agent_id}", response_model=Agent)
async def update_agent(agent_id: str, agent_data: AgentUpdate, mas_manager=Depends(get_mas_manager)):
    """Update an existing agent."""
    try:
        updated_agent = await mas_manager.update_agent(agent_id, agent_data)
        if updated_agent is None:
            raise HTTPException(status_code=404, detail="Agent not found")
        return updated_agent
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{agent_id}")
async def delete_agent(agent_id: str, mas_manager=Depends(get_mas_manager)):
    """Delete an agent."""
    success = await mas_manager.delete_agent(agent_id)
    if not success:
        raise HTTPException(status_code=404, detail="Agent not found")
    return {"message": "Agent deleted successfully"}

@router.post("/{agent_id}/start")
async def start_agent(agent_id: str, mas_manager=Depends(get_mas_manager)):
    """Start an agent."""
    try:
        await mas_manager.start_agent(agent_id)
        return {"message": f"Agent {agent_id} started successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{agent_id}/stop")
async def stop_agent(agent_id: str, mas_manager=Depends(get_mas_manager)):
    """Stop an agent."""
    try:
        await mas_manager.stop_agent(agent_id)
        return {"message": f"Agent {agent_id} stopped successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

```