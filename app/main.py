from fastapi import FastAPI

from app.core import global_event_logger  # noqa
from app.core.exception_handlers import email_exists_handler, username_exists_handler
from app.core.logging import setup_logging
from app.users.events import domain  # noqa
from app.users.exceptions import EmailAlreadyExists, UsernameAlreadyExists
from app.users.router import router as users_router

setup_logging()

app = FastAPI()
app.include_router(users_router, prefix="/users", tags=["Users"])


app.add_exception_handler(EmailAlreadyExists, email_exists_handler)
app.add_exception_handler(UsernameAlreadyExists, username_exists_handler)
