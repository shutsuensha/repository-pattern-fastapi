from dataclasses import dataclass

from app.core.integration_event import IntegrationEvent


@dataclass
class UserCreatedEvent(IntegrationEvent):
    user_id: int
    username: str
    email: str
