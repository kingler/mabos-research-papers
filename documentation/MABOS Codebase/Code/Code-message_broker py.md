# Code: message_broker.py

```python
# message_broker.py
import asyncio
from typing import Dict, List, Callable, Coroutine
from communication.fipa_acl import FIPAACLMessage

class MessageBroker:
    def __init__(self):
        self.subscriptions: Dict[str, List[Callable[[FIPAACLMessage], Coroutine]]] = {}

    async def subscribe(self, topic: str, callback: Callable[[FIPAACLMessage], Coroutine]):
        """
        Subscribe to a topic with a callback function.
        """
        if topic not in self.subscriptions:
            self.subscriptions[topic] = []
        self.subscriptions[topic].append(callback)

    async def unsubscribe(self, topic: str, callback: Callable[[FIPAACLMessage], Coroutine]):
        """
        Unsubscribe from a topic.
        """
        if topic in self.subscriptions and callback in self.subscriptions[topic]:
            self.subscriptions[topic].remove(callback)

    async def publish(self, topic: str, message: FIPAACLMessage):
        """
        Publish a message to a topic.
        """
        if topic in self.subscriptions:
            tasks = [callback(message) for callback in self.subscriptions[topic]]
            await asyncio.gather(*tasks)

class Agent:
    def __init__(self, name: str, broker: MessageBroker):
        self.name = name
        self.broker = broker

    async def send_message(self, topic: str, receiver: str, performative: str, content: str):
        message = FIPAACLMessage(sender=self.name, receiver=receiver, performative=performative, content=content)
        await self.broker.publish(topic, message)

    async def receive_message(self, message: FIPAACLMessage):
        print(f"{self.name} received: {message}")

# Example usage
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