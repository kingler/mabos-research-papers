# Code: fipa_acl.py

```python
from enum import Enum
from typing import Any, Optional

class Performative(Enum):
    INFORM = "inform"
    REQUEST = "request"
    AGREE = "agree"
    REFUSE = "refuse"
    PROPOSE = "propose"
    ACCEPT_PROPOSAL = "accept-proposal"
    REJECT_PROPOSAL = "reject-proposal"
    QUERY_IF = "query-if"
    NOT_UNDERSTOOD = "not-understood"

class FIPAACLMessage:
    def __init__(self, sender: str, receiver: str, performative: Performative, content: Any,
                 conversation_id: Optional[str] = None, in_reply_to: Optional[str] = None):
        self.sender = sender
        self.receiver = receiver
        self.performative = performative
        self.content = content
        self.conversation_id = conversation_id
        self.in_reply_to = in_reply_to

    def to_dict(self) -> dict:
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "performative": self.performative.value,
            "content": self.content,
            "conversation_id": self.conversation_id,
            "in_reply_to": self.in_reply_to
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'FIPAACLMessage':
        return cls(
            sender=data["sender"],
            receiver=data["receiver"],
            performative=Performative(data["performative"]),
            content=data["content"],
            conversation_id=data.get("conversation_id"),
            in_reply_to=data.get("in_reply_to")
        )

    def __str__(self):
        return f"FIPAACLMessage(sender={self.sender}, receiver={self.receiver}, performative={self.performative.value}, content={self.content})"
```