# Code: main.py

```python
# main.py
import asyncio
import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from api.main import app
from config import active_config
from mas.mas_manager import MASManager
from mas.database.models import Base
from mas.message_broker import MessageBroker

# Initialize database
engine = create_async_engine(active_config.get_database_url(), echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Initialize message broker
message_broker = MessageBroker(active_config.MESSAGE_BROKER_URL)

# Initialize MAS Manager
mas_manager = MASManager(async_session, message_broker)

@app.on_event("startup")
async def startup_event():
    # Create database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # Initialize MAS Manager
    await mas_manager.initialize()
    
    # Start background tasks
    asyncio.create_task(background_tasks())

@app.on_event("shutdown")
async def shutdown_event():
    # Shutdown MAS Manager
    await mas_manager.shutdown()
    
    # Close database connections
    await engine.dispose()

async def background_tasks():
    while True:
        # Perform regular system maintenance
        await mas_manager.perform_maintenance()
        
        # Update system metrics
        await mas_manager.update_metrics()
        
        # Wait for the next cycle
        await asyncio.sleep(active_config.PERFORMANCE_TRACKING_INTERVAL)

# Make MAS Manager available to API routes
app.state.mas_manager = mas_manager

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=active_config.API_HOST,
        port=active_config.API_PORT,
        reload=active_config.API_DEBUG
    )
```