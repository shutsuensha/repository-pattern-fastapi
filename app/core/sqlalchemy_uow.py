from sqlalchemy.ext.asyncio import AsyncSession

from app.core.uow import AbstractUnitOfWork
from app.users.repository import UserRepository


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: AsyncSession):
        super().__init__()
        self.session = session
        self.users = UserRepository(session)

    async def commit(self):
        self._committed = True
        await self.session.commit()
        await self._publish_domain_events()
        await self._publish_integration_events()


    async def rollback(self):
        await self.session.rollback()
