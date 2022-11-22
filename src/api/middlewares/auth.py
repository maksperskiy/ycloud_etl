from fastapi import Depends, Header

from src.exceptions import AccessDeniedException

from src.core.settings import settings



async def has_access(token: str = Header(alias="x-auth")):
    print(token)
    if token != settings.static_token:
        raise AccessDeniedException
