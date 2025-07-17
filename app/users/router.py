from fastapi import APIRouter, Depends

from app.core.dependencies import get_uow
from app.core.sqlalchemy_uow import SQLAlchemyUnitOfWork
from app.users.schemas import UserCreate, UserRead
from app.users.service import UserService

router = APIRouter()


@router.post("/", response_model=UserRead)
async def register_user(
    user_data: UserCreate,
    uow: SQLAlchemyUnitOfWork = Depends(get_uow),
):
    service = UserService(uow)
    async with uow:
        user = await service.register_user(user_data)
        await uow.commit()
        return user
