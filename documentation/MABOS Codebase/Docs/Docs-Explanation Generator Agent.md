# Docs: Explanation Generator Agent

The ExplanationGeneratorAgent provides explanations and justifications for the system's actions and decisions. It enhances transparency and user trust, improving the MAS's explainability and user interaction. Here is detailed documentation for implementing the Explanation Generator Agent, including its role, BDI components, and how it fits into the goal-oriented business development and operation multi-agent system SaaS platform. It includes the requested PlantUML diagrams and a detailed explanation of the Explanation Generator Agent's code, as well as its connection with the LLM Agent for generating explanations for human stakeholders.

### Role and Purpose:

The Explanation Generator Agent is responsible for creating clear and understandable explanations for the actions and decisions made by the multi-agent system. It plays a crucial role in enhancing system transparency, building user trust, and improving the overall user experience by providing insights into the system's reasoning processes. This agent is essential for making complex decision-making processes more accessible to human stakeholders, thereby facilitating better human-agent interaction and system acceptance.

### BDI Components:

### a. Beliefs:

- Current system state and actions
- Historical data on system decisions
- User profiles and preferences
- Explanation requests
- Generated explanations
- Action data and reasoning

### b. Desires:

- Generate clear and accurate explanations
- Enhance system transparency
- Improve user trust and understanding
- Adapt explanations to user profiles
- Maintain a comprehensive log of system actions and explanations

### c. Intentions:

- Collect relevant data for explanation generation
- Process explanation requests
- Generate tailored explanations
- Collaborate with the LLM Agent for natural language processing
- Update explanation logs
- Communicate explanations to users or other agents

### Goals:

- G1: Generate clear and accurate explanations for system actions
- G2: Enhance system transparency and user trust
- G3: Adapt explanations to different user profiles and contexts
- G4: Maintain a comprehensive log of system actions and explanations
- G5: Collaborate effectively with the LLM Agent for natural language processing

### Plans:

- P1: CollectActionDataPlan: Plan to gather relevant data for explanation generation
- P2: GenerateExplanationPlan: Plan to create explanations based on collected data
- P3: ProcessExplanationRequestPlan: Plan to handle and respond to explanation requests
- P4: CollaborateWithLLMAgentPlan: Plan to interact with the LLM Agent for natural language processing
- P5: UpdateExplanationLogPlan: Plan to maintain a log of generated explanations

### Actions:

- Collect action data from various system components
- Generate explanations based on collected data
- Process and respond to explanation requests
- Collaborate with the LLM Agent for natural language processing
- Update and maintain explanation logs
- Communicate explanations to users or other agents
- Adapt explanations based on user profiles and contexts

### Knowledge:

- Explanation generation techniques
- System action and decision-making processes
- User profile information and preferences
- Natural language processing principles
- Interaction protocols with other agents, especially the LLM Agent
- Logging and data management practices

### PlantUML Diagrams:

### a. Workflow Diagram:

```
@startuml
|ExplanationGeneratorAgent|
start
:Receive Explanation Request;
:Collect Action Data;
:Generate Initial Explanation;
:Collaborate with LLM Agent;
:Refine Explanation;
:Deliver Explanation;
:Update Explanation Log;
stop
@enduml

```

### b. Goal Model (Using Activity Diagram):

```
@startuml
|ExplanationGeneratorAgent|
start
fork
  :G1: Generate Clear Explanations;
fork again
  :G2: Enhance Transparency;
fork again
  :G3: Adapt to User Profiles;
fork again
  :G4: Maintain Explanation Log;
fork again
  :G5: Collaborate with LLM Agent;
end fork
stop
@enduml

```

### c. Sequence Diagram (Interaction with other agents):

```
@startuml
participant "User" as U
participant "ExplanationGeneratorAgent" as EGA
participant "LLMAgent" as LLMA
participant "OtherAgents" as OA

U -> EGA: Request Explanation
activate EGA
EGA -> OA: Request Action Data
OA --> EGA: Provide Action Data
EGA -> EGA: Generate Initial Explanation
EGA -> LLMA: Request NLP Processing
activate LLMA
LLMA --> EGA: Provide Refined Explanation
deactivate LLMA
EGA -> EGA: Update Explanation Log
EGA -> U: Deliver Explanation
deactivate EGA
@enduml

```

### Detailed Code Explanation:

Here's a detailed explanation of the key components and methods for implementing the Explanation Generator Agent:

```python
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message
from models.goal_model import Goal
from models.belief_model import Belief
from models.plan_model import Plan

class ExplanationGeneratorAgent(Agent):
    def __init__(self, aid):
        super(ExplanationGeneratorAgent, self).__init__(aid)
        self.beliefs = []
        self.goals = []
        self.plans = []

    def setup(self):
        display_message(self.aid.name, "Setting up ExplanationGeneratorAgent")
        self.add_goal(Goal("GenerateExplanations", "Maintain"))
        self.add_plan(Plan("CollectActionDataPlan", self.collect_action_data))
        self.add_plan(Plan("GenerateExplanationPlan", self.generate_explanation))

    def act(self):
        display_message(self.aid.name, "Acting in ExplanationGeneratorAgent")
        self.execute_plans()

    def on_message(self, message: ACLMessage):
        display_message(self.aid.name, f"Received message: {message.content}")
        if message.performative == ACLMessage.REQUEST:
            self.handle_explanation_request(message)

    def add_goal(self, goal):
        self.goals.append(goal)

    def add_belief(self, belief):
        self.beliefs.append(belief)

    def add_plan(self, plan):
        self.plans.append(plan)

    def execute_plans(self):
        for plan in self.plans:
            if plan.is_applicable(self.beliefs, self.goals):
                plan.execute()

    def collect_action_data(self):
        display_message(self.aid.name, "Collecting data for explanation")
        action_data = self.gather_action_data()
        self.add_belief(Belief("ActionData", action_data))

    def generate_explanation(self):
        display_message(self.aid.name, "Generating explanation")
        action_data = self.get_belief("ActionData")
        if action_data:
            explanation = self.create_explanation(action_data)
            self.add_belief(Belief("GeneratedExplanation", explanation))

    def handle_explanation_request(self, message):
        content = message.content
        self.add_belief(Belief("ExplanationRequest", content))
        self.add_goal(Goal("ProcessExplanationRequest", "Achieve"))

    def gather_action_data(self):
        # Simulated action data collection
        return {"Action1": "Reason1", "Action2": "Reason2"}

    def create_explanation(self, action_data):
        # Simulated explanation generation
        return {"Action1": "Explanation for Action1", "Action2": "Explanation for Action2"}

    def get_belief(self, belief_name):
        for belief in self.beliefs:
            if belief.name == belief_name:
                return belief.value
        return None

```

### Implementation Details:

1. **Class Initialization**: The `ExplanationGeneratorAgent` class inherits from the base `Agent` class and initializes its beliefs, goals, and plans.
2. **Setup Method**: The `setup` method initializes the agent by adding the main goal "GenerateExplanations" and two plans: "CollectActionDataPlan" and "GenerateExplanationPlan".
3. **Act Method**: The `act` method executes the agent's plans.
4. **Message Handling**: The `on_message` method processes incoming messages, specifically handling explanation requests.
5. **Goal Management**: The `add_goal` method adds goals to the agent's list of goals.
6. **Belief Management**: The `add_belief` method adds beliefs to the agent's list of beliefs.
7. **Plan Management**: The `add_plan` method adds plans to the agent's list of plans.
8. **Plan Execution**: The `execute_plans` method executes applicable plans based on the agent's beliefs and goals.
9. **Action Data Collection**: The `collect_action_data` method gathers relevant data for explanation generation.
10. **Explanation Generation**: The `generate_explanation` method creates explanations based on collected action data.
11. **Request Handling**: The `handle_explanation_request` method processes incoming explanation requests.
12. **Data Gathering**: The `gather_action_data` method simulates the collection of action data.
13. **Explanation Creation**: The `create_explanation` method simulates the generation of explanations.
14. **Belief Retrieval**: The `get_belief` method retrieves the value of a specified belief.

### Architecture

The architecture for the Explanation Generator Agent, including its components, interactions, and how it fits into the larger Multi-Agent System (MAS) for the goal-oriented business development and operation SaaS platform.

### High-Level Architecture Diagram

```
@startuml
package "ExplanationGeneratorAgent" {
  [BDI Core]
  [Action Data Collector]
  [Explanation Generator]
  [Request Handler]
  [LLM Collaborator]
  [Explanation Log]
  [Communication Module]
}
cloud "External Systems" {
  [Action Data Sources]
  [User Interfaces]
}
actor "Human Stakeholder"
package "MAS Platform" {
  [LLMAgent]
  [OtherAgents]
  [Message Broker]
  [Shared Resources]
}
"ExplanationGeneratorAgent" -- "MAS Platform" : Interacts with
"ExplanationGeneratorAgent" -- "External Systems" : Collects data from
"ExplanationGeneratorAgent" -- Human Stakeholder : Provides explanations to
@enduml

```

### Component Descriptions

**a. BDI Core:**

- Manages the agent's beliefs, desires, and intentions
- Implements the reasoning cycle for decision-making
- Coordinates the execution of plans based on current goals and beliefs

**b. Action Data Collector:**

- Gathers relevant data from various system components for explanation generation
- Processes and structures the collected data for use in explanations

**c. Explanation Generator:**

- Creates initial explanations based on collected action data
- Adapts explanations to different user profiles and contexts

**d. Request Handler:**

- Processes incoming explanation requests from users or other agents
- Prioritizes and manages multiple explanation requests

**e. LLM Collaborator:**

- Interfaces with the LLM Agent for natural language processing
- Refines and enhances explanations using advanced language models

**f. Explanation Log:**

- Maintains a comprehensive record of generated explanations
- Provides historical context for future explanation generation

**g. Communication Module:**

- Handles communication with other agents within the MAS
- Manages the exchange of information with external systems and user interfaces

### Connection with LLM Agent

The Explanation Generator Agent collaborates closely with the LLM Agent to enhance the quality and naturalness of the generated explanations. Here's how they interact:

1. **Initial Explanation Generation**: The Explanation Generator Agent creates an initial explanation based on the collected action data.
2. **LLM Processing Request**: The agent sends this initial explanation to the LLM Agent for further processing and refinement.
3. **Natural Language Enhancement**: The LLM Agent applies advanced natural language processing techniques to improve the clarity, coherence, and naturalness of the explanation.
4. **Contextual Adaptation**: The LLM Agent may adapt the language and complexity of the explanation based on the user profile provided by the Explanation Generator Agent.
5. **Refined Explanation**: The LLM Agent returns the refined explanation to the Explanation Generator Agent.
6. **Final Processing**: The Explanation Generator Agent may perform final adjustments before delivering the explanation to the human stakeholder.

This collaboration ensures that the explanations are not only accurate and informative but also easily understandable and tailored to the specific needs of human stakeholders.

### Key Features and Capabilities

### a. Adaptive Explanation Generation:

- The agent can generate explanations tailored to different user profiles and contexts.
- It uses a combination of structured data and natural language processing to create clear and informative explanations.

### b. Seamless LLM Integration:

- Collaborates effectively with the LLM Agent to enhance explanation quality.
- Leverages advanced language models for more natural and context-aware explanations.

### c. Comprehensive Action Tracking:

- Maintains detailed logs of system actions and their corresponding explanations.
- Provides historical context for generating consistent and coherent explanations over time.

### d. Real-time Explanation Processing:

- Handles explanation requests in real-time, providing timely insights into system actions.
- Balances the need for quick responses with the generation of thorough explanations.

### e. Multi-modal Explanation Support:

- Capable of generating explanations in various formats (text, structured data, visualizations) to suit different user needs and interfaces.

### Scalability and Performance Considerations

- The agent is designed to handle a large volume of explanation requests simultaneously.
- It uses efficient data structures for quick retrieval of action data and previously generated explanations.
- The collaboration with the LLM Agent is optimized to minimize latency in explanation generation.
- Asynchronous processing is used where possible to improve responsiveness and throughput.

### Security and Compliance

- Implements role-based access control for sensitive action data and explanations.
- Maintains an audit trail of all explanation requests and generated explanations.
- Ensures compliance with data privacy regulations when handling and explaining user-related actions.
- Supports encryption of sensitive data during the explanation generation and communication process.

This architecture provides a robust and flexible foundation for the Explanation Generator Agent, allowing it to effectively create and manage explanations within the multi-agent system. The integration with the LLM Agent enhances its capability to provide clear, context-aware, and user-friendly explanations, thereby improving the overall transparency and user trust in the system.