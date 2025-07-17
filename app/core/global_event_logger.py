import logging

from app.core.domain_event import DomainEvent
from app.core.event_bus import event_bus

logger = logging.getLogger(__name__)


async def log_all_events(event: DomainEvent):
    logger.info(f"[GLOBAL EVENT] {type(event).__name__} → {event.__dict__}")


event_bus.subscribe(DomainEvent, log_all_events)
