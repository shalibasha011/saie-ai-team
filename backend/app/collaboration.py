from datetime import datetime
from typing import Any


def create_message(
    sender: str,
    receiver: str,
    message_type: str,
    content: Any
):
    return {
        "id": f"{sender}-{receiver}-{datetime.utcnow().timestamp()}",
        "sender": sender,
        "receiver": receiver,
        "message_type": message_type,
        "content": content,
        "timestamp": datetime.utcnow().isoformat(),
        "status": "created"
    }