from app.core.uow import AbstractUnitOfWork
from app.users.events.domain import UserRegistered
from app.users.events.integration import UserCreatedEvent
from app.users.exceptions import EmailAlreadyExists, UsernameAlreadyExists
from app.users.schemas import UserCreate, UserRead


class UserService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def register_user(self, data: UserCreate) -> UserRead:
        if await self.uow.users.get_by_email(data.email):
            raise EmailAlreadyExists()

        if await self.uow.users.get_by_username(data.username):
            raise UsernameAlreadyExists()

        user = await self.uow.users.create(data)

        self.uow.collect_domain_event(
            UserRegistered(user_id=user.id, email=user.email, username=user.username)
        )

        self.uow.collect_integration_event(
            UserCreatedEvent(user.id, user.username, user.email)
        )

        return UserRead.model_validate(user)
