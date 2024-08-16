# Docs: Message Broker

## 1. Overall Description and Purpose

This code implements a simple message broker system for facilitating communication between agents in a multi-agent system. It includes two main classes:

1. `MessageBroker`: Manages subscriptions and message distribution.
2. `Agent`: Represents an agent that can send and receive messages.

The purpose of this code is to provide a flexible and extensible framework for asynchronous, topic-based communication between agents. It allows agents to subscribe to topics of interest, publish messages to specific topics, and receive messages asynchronously. This pattern is particularly useful in distributed systems, event-driven architectures, and multi-agent systems where decoupled, scalable communication is essential.

## 2. PlantUML Class Diagram

The following PlantUML diagram illustrates the structure of the Message Broker system:

```
@startuml
class MessageBroker {
  - subscriptions: Dict[str, List[Callable[[FIPAACLMessage], Coroutine]]]
  + subscribe(topic: str, callback: Callable[[FIPAACLMessage], Coroutine]): Coroutine
  + unsubscribe(topic: str, callback: Callable[[FIPAACLMessage], Coroutine]): Coroutine
  + publish(topic: str, message: FIPAACLMessage): Coroutine
}

class Agent {
  - name: str
  - broker: MessageBroker
  + send_message(topic: str, receiver: str, performative: str, content: str): Coroutine
  + receive_message(message: FIPAACLMessage): Coroutine
}

class FIPAACLMessage

Agent --> MessageBroker : uses
MessageBroker ..> FIPAACLMessage : handles
Agent ..> FIPAACLMessage : uses
@enduml

```

## 3. Data Schema Description

1. `MessageBroker` (Class):
    - `subscriptions` (Dict[str, List[Callable[[FIPAACLMessage], Coroutine]]]): A dictionary mapping topics to lists of callback coroutines
2. `Agent` (Class):
    - `name` (str): The name of the agent
    - `broker` (MessageBroker): A reference to the message broker used by the agent

## 4. Breakdown of Functions/Methods

### MessageBroker Class

### `__init__(self)`

- Purpose: Initialize a new MessageBroker object
- Parameters: None
- Return value: None
- Key logic: Initializes an empty dictionary for subscriptions

### `async def subscribe(self, topic: str, callback: Callable[[FIPAACLMessage], Coroutine])`

- Purpose: Subscribe to a topic with a callback function
- Parameters:
    - `topic` (str): The topic to subscribe to
    - `callback` (Callable[[FIPAACLMessage], Coroutine]): The coroutine to be called when a message is published to the topic
- Return value: None
- Key logic: Adds the callback to the list of subscribers for the given topic

### `async def unsubscribe(self, topic: str, callback: Callable[[FIPAACLMessage], Coroutine])`

- Purpose: Unsubscribe from a topic
- Parameters:
    - `topic` (str): The topic to unsubscribe from
    - `callback` (Callable[[FIPAACLMessage], Coroutine]): The coroutine to be removed from the subscribers list
- Return value: None
- Key logic: Removes the callback from the list of subscribers for the given topic

### `async def publish(self, topic: str, message: FIPAACLMessage)`

- Purpose: Publish a message to a topic
- Parameters:
    - `topic` (str): The topic to publish the message to
    - `message` (FIPAACLMessage): The message to be published
- Return value: None
- Key logic: Calls all subscribed callbacks for the given topic with the provided message

### Agent Class

### `__init__(self, name: str, broker: MessageBroker)`

- Purpose: Initialize a new Agent object
- Parameters:
    - `name` (str): The name of the agent
    - `broker` (MessageBroker): The message broker to be used by the agent
- Return value: None
- Key logic: Stores the name and broker reference

### `async def send_message(self, topic: str, receiver: str, performative: str, content: str)`

- Purpose: Send a message to a specific topic
- Parameters:
    - `topic` (str): The topic to publish the message to
    - `receiver` (str): The intended receiver of the message
    - `performative` (str): The performative of the message
    - `content` (str): The content of the message
- Return value: None
- Key logic: Creates a FIPAACLMessage and publishes it to the specified topic using the broker

### `async def receive_message(self, message: FIPAACLMessage)`

- Purpose: Handle received messages
- Parameters:
    - `message` (FIPAACLMessage): The received message
- Return value: None
- Key logic: Prints the received message (in a real system, this would process the message)

## 5. Key Python Libraries Used

The code uses the following Python standard libraries:

1. `asyncio`: Used for asynchronous programming, allowing non-blocking operations.
2. `typing`: Used for type hinting, improving code readability and enabling better static type checking. Specifically, it uses `Dict`, `List`, `Callable`, and `Coroutine`.

## 6. Other Class Imports and Their Relationships

The code imports `FIPAACLMessage` from `communication.fipa_acl`. This class is used to represent the messages exchanged between agents.

## 7. Important Notes on Usage, Limitations, and Future Improvements

Usage:

- Create a `MessageBroker` instance to manage communication.
- Create `Agent` instances, passing the `MessageBroker` to them.
- Use the `subscribe` method of `MessageBroker` to subscribe agents to topics.
- Agents can send messages using their `send_message` method.
- The broker will asynchronously deliver messages to subscribed agents.

Limitations:

- The current implementation doesn't handle errors in callback functions.
- There's no built-in support for message persistence or delivery guarantees.
- The system assumes all agents are running in the same process.

Potential future improvements:

1. Implement error handling for callback functions to prevent one faulty subscriber from affecting others.
2. Add support for message persistence and delivery guarantees (e.g., at-least-once delivery).
3. Implement a distributed version of the message broker for multi-process or networked environments.
4. Add support for wildcard topic subscriptions (e.g., "market.*.stocks").
5. Implement message filtering capabilities for subscribers.
6. Add support for message priorities and quality of service levels.
7. Implement a mechanism for flow control to handle high message volumes.
8. Add support for message expiration and time-to-live.
9. Implement security features such as authentication and authorization for publishing and subscribing.
10. Add monitoring and metrics collection for system performance analysis.

Example Usage:

```python
async def main():
    broker = MessageBroker()
    agent1 = Agent("Agent1", broker)
    agent2 = Agent("Agent2", broker)

    # Subscribe agents to topics
    await broker.subscribe("market_data", agent1.receive_message)
    await broker.subscribe("market_data", agent2.receive_message)

    # Agent1 sends a message
    await agent1.send_message("market_data", "Agent2", "inform", "Stock prices updated")

    # Allow some time for message processing
    await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())

```

This example demonstrates how to create a message broker, create agents, subscribe them to topics, and send messages between them. The asynchronous nature of the system allows for efficient handling of multiple agents and messages.