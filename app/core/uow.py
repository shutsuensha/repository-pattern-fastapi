from abc import ABC, abstractmethod

from app.core.domain_event import DomainEvent
from app.core.event_bus import event_bus
from app.core.integration_event import IntegrationEvent


class AbstractUnitOfWork(ABC):
    def __init__(self):
        self._domain_events: list[DomainEvent] = []
        self._integration_events: list[IntegrationEvent] = []
        self._committed = False

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type or not self._committed:
            await self.rollback()
            self._domain_events.clear()
            self._integration_events.clear()

    def collect_domain_event(self, event: DomainEvent):
        self._domain_events.append(event)

    def collect_integration_event(self, event: IntegrationEvent):
        self._integration_events.append(event)

    async def _publish_domain_events(self):
        for event in self._domain_events:
            await event_bus.publish(event)
        self._domain_events.clear()
    
    async def _publish_integration_events(self):
        for event in self._integration_events:
            await event_bus.publish_integration_event(event)
        self._integration_events.clear()

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    async def rollback(self): ...
