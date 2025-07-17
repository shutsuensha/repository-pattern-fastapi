import logging
from dataclasses import dataclass

from app.core.domain_event import DomainEvent
from app.core.event_bus import event_bus

logger = logging.getLogger(__name__)


@dataclass
class UserRegistered(DomainEvent):
    user_id: int
    username: str
    email: str


async def send_welcome_email(event: UserRegistered):
    logger.info(
        f"[EVENT] Sending welcome email to user {event.email} (ID: {event.user_id})"
    )


event_bus.subscribe(UserRegistered, send_welcome_email)
