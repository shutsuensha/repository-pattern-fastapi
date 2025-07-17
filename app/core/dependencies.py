from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.sqlalchemy_uow import SQLAlchemyUnitOfWork


def get_uow(session: AsyncSession = Depends(get_async_session)) -> SQLAlchemyUnitOfWork:
    return SQLAlchemyUnitOfWork(session)
