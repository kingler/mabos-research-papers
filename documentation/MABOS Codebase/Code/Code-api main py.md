# Code: api/main.py

```python
# api/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import agent_routes, model_routes, system_routes
from .dependencies import get_mas_manager

app = FastAPI(title="MABOS SaaS Platform API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(agent_routes.router, prefix="/api/agents", tags=["agents"])
app.include_router(model_routes.router, prefix="/api/models", tags=["models"])
app.include_router(system_routes.router, prefix="/api/system", tags=["system"])

@app.on_event("startup")
async def startup_event():
    mas_manager = await get_mas_manager()
    await mas_manager.initialize()

@app.on_event("shutdown")
async def shutdown_event():
    mas_manager = await get_mas_manager()
    await mas_manager.shutdown()

@app.get("/")
async def root():
    return {"message": "Welcome to the MABOS SaaS Platform API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

```