# Docs: Agent Schemas

**Explanation:**

This file defines the Pydantic schemas for agent-related data structures used in our Multi-Agent System API. These schemas serve as data models for request/response validation and serialization/deserialization of agent data.

In the context of our MAS, these schemas are crucial for:

1. Ensuring data integrity and consistency when creating or updating agents
2. Providing clear contracts for API requests and responses related to agents
3. Enabling automatic API documentation and client code generation
4. Facilitating data validation and type checking

The schemas defined here correspond to different aspects of agent management, including:

- AgentBase: The base schema with common agent attributes
- AgentCreate: Schema for creating a new agent
- AgentUpdate: Schema for updating an existing agent
- Agent: Full agent representation, including system-generated fields

These schemas align with the agent model in our MAS and ensure that all agent-related operations through the API maintain data consistency and adhere to the expected structure of our agents.

---

## 1. Overall Description and Purpose

This code defines the Pydantic model schemas for agent-related data in the MABOS (Multi-Agent Based Optimization System) SaaS Platform. These schemas are used to validate and serialize/deserialize data related to agents in the system. The purpose of this module is to:

- Define the structure and types of data used for agents
- Provide input validation for API requests and responses
- Ensure consistency in agent data representation across the application
- Facilitate automatic API documentation generation

The schemas cover various aspects of agent management, including agent creation, updating, and retrieval, as well as representing agent states and types.

## 2. Schema Structure Diagram

```
@startuml
enum AgentType {
    REACTIVE
    PROACTIVE
    BDI
    HYBRID
}

enum AgentStatus {
    IDLE
    ACTIVE
    PAUSED
    ERROR
}

class AgentBase {
    +name: str
    +type: AgentType
    +description: Optional[str]
}

class AgentCreate {
    +initial_beliefs: Optional[List[dict]]
    +initial_goals: Optional[List[dict]]
}

class AgentUpdate {
    +name: Optional[str]
    +description: Optional[str]
    +beliefs: Optional[List[dict]]
    +goals: Optional[List[dict]]
}

class Agent {
    +id: str
    +status: AgentStatus
    +beliefs: List[dict]
    +goals: List[dict]
    +performance_metrics: Optional[dict]
}

AgentBase <|-- AgentCreate
AgentBase <|-- Agent
@enduml

```

## 3. Key Components

1. `AgentType` (Enum): Defines the types of agents in the system
2. `AgentStatus` (Enum): Defines the possible statuses of an agent
3. `AgentBase` (BaseModel): Base class for agent-related schemas
4. `AgentCreate` (AgentBase): Schema for creating a new agent
5. `AgentUpdate` (BaseModel): Schema for updating an existing agent
6. `Agent` (AgentBase): Schema for a complete agent representation

## 4. Breakdown of Schemas

### AgentType (Enum)

- Purpose: Define the possible types of agents in the system
- Values:
    - REACTIVE: Represents a reactive agent
    - PROACTIVE: Represents a proactive agent
    - BDI: Represents a Belief-Desire-Intention agent
    - HYBRID: Represents a hybrid agent

### AgentStatus (Enum)

- Purpose: Define the possible statuses of an agent
- Values:
    - IDLE: Agent is idle
    - ACTIVE: Agent is active and operating
    - PAUSED: Agent operation is paused
    - ERROR: Agent is in an error state

### AgentBase (BaseModel)

- Purpose: Serve as a base class for agent-related schemas
- Fields:
    - `name` (str): The name of the agent
    - `type` (AgentType): The type of the agent
    - `description` (Optional[str]): A brief description of the agent's purpose

### AgentCreate (AgentBase)

- Purpose: Define the schema for creating a new agent
- Inherits from: AgentBase
- Additional Fields:
    - `initial_beliefs` (Optional[List[dict]]): Initial beliefs of the agent
    - `initial_goals` (Optional[List[dict]]): Initial goals of the agent

### AgentUpdate (BaseModel)

- Purpose: Define the schema for updating an existing agent
- Fields:
    - `name` (Optional[str]): Updated name of the agent
    - `description` (Optional[str]): Updated description of the agent
    - `beliefs` (Optional[List[dict]]): Updated beliefs of the agent
    - `goals` (Optional[List[dict]]): Updated goals of the agent

### Agent (AgentBase)

- Purpose: Define the schema for a complete agent representation
- Inherits from: AgentBase
- Additional Fields:
    - `id` (str): The unique identifier of the agent
    - `status` (AgentStatus): The current status of the agent
    - `beliefs` (List[dict]): Current beliefs of the agent
    - `goals` (List[dict]): Current goals of the agent
    - `performance_metrics` (Optional[dict]): Performance metrics of the agent
- Includes an example configuration for API documentation

## 5. Key Python Libraries and Frameworks Used

1. `pydantic`: Used for defining data models with type annotations
2. `typing`: Used for type hinting, particularly for complex types
3. `enum`: Used for defining the AgentType and AgentStatus enumerations

## 6. Usage Notes

- These schemas should be imported and used in API route definitions to specify request/response models
- They can also be used for data validation within the application logic
- The `Agent` schema includes an example configuration, which can be used by API documentation tools

## 7. Important Notes on Usage, Configuration, and Future Improvements

Usage:

- Use these schemas in FastAPI route definitions to automatically validate request/response data
- Utilize Pydantic's validation features for complex data structures within the `beliefs`, `goals`, and `performance_metrics` fields

Configuration:

- The schemas use Pydantic's default configuration
- Custom validators or configurations can be added as needed

Potential future improvements:

1. Implement more detailed validation for beliefs and goals structures
2. Add support for agent capabilities or skills
3. Implement schema inheritance for different agent types (e.g., ReactiveAgent, BDIAgent)
4. Add support for agent communication protocols or message schemas
5. Implement custom validators for complex agent structures (e.g., BDI components)
6. Add support for agent roles or organizational structures
7. Implement versioning for agent schemas to handle evolution of agent structures over time
8. Add support for agent learning models or knowledge bases
9. Implement serialization methods for different output formats (e.g., JSON, YAML, XML)
10. Add support for agent templates or predefined configurations

Example Usage in FastAPI:

```python
from fastapi import APIRouter
from .agent_schemas import AgentCreate, Agent

router = APIRouter()

@router.post("/agents", response_model=Agent)
async def create_agent(agent: AgentCreate):
    # Logic to create an agent
    pass

```

This example shows how to use the AgentCreate schema for input validation and the Agent schema for response serialization in a FastAPI route.

I've created comprehensive documentation for the Agent Schemas code you provided. This documentation follows a structure similar to the previous examples, adapted to fit the nature of Pydantic model schemas for agents. It includes an overall description, a PlantUML diagram showing the structure and relationships of the schemas, a description of key components, a breakdown of each schema, key Python libraries used, usage notes, and important notes on usage, configuration, and potential future improvements.

The documentation is formatted in Markdown for easy readability and includes PlantUML diagram code for the schema structure diagram. This should provide a clear and detailed guide for developers working with these agent schemas within the MABOS SaaS Platform API.

Would you like me to explain or elaborate on any specific part of the documentation?​​​​​​​​​​​​​​​​