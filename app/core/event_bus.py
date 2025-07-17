import asyncio
import inspect
import logging
from collections import defaultdict
from collections.abc import Callable, Coroutine
from typing import Any

from app.core.integration_event import IntegrationEvent

logger = logging.getLogger(__name__)


class EventBus:
    def __init__(self):
        self._subscribers: dict[
            type, list[Callable[[Any], Coroutine[Any, Any, None]]]
        ] = defaultdict(list)

    def subscribe(
        self, event_type: type, handler: Callable[[Any], Coroutine[Any, Any, None]]
    ):
        self._subscribers[event_type].append(handler)

    async def publish(self, event: Any):
        event_type = type(event)
        # Получаем всех подписчиков для текущего типа и его базовых классов
        handlers = self._collect_handlers(event_type)

        await asyncio.gather(
            *(self._safe_handler(handler, event) for handler in handlers),
            return_exceptions=True,
        )

    def _collect_handlers(self, event_type: type) -> list[Callable]:
        """
        Собирает обработчики для типа события и его базовых классов.
        """
        handlers = []
        for cls in inspect.getmro(event_type):  # MRO: event → base → object
            if cls in self._subscribers:
                handlers.extend(self._subscribers[cls])
        return handlers

    async def _safe_handler(self, handler: Callable[[Any], Coroutine], event: Any):
        try:
            await handler(event)
        except Exception as e:
            logger.error(
                f"[EventBus] Ошибка при обработке {type(event).__name__} в {handler.__name__}: {e}",
                exc_info=True,
            )

    async def publish_integration_event(self, event: IntegrationEvent):
        # здесь логика отправки события в брокер (RabbitMQ/Kafka)
        logger.info(f"[INTEGRATION EVENT] {type(event).__name__} -> {event.__dict__} -> отправить в Kafka")
        pass


# Глобальный экземпляр
event_bus = EventBus()
