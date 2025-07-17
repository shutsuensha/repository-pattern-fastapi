from fastapi import Request
from fastapi.responses import JSONResponse

from app.users.exceptions import EmailAlreadyExists, UsernameAlreadyExists


async def email_exists_handler(request: Request, exc: EmailAlreadyExists):
    return JSONResponse(
        status_code=400, content={"detail": "User with this email already exists"}
    )


async def username_exists_handler(request: Request, exc: UsernameAlreadyExists):
    return JSONResponse(
        status_code=400, content={"detail": "User with this username already exists"}
    )
