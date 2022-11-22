import functools
from contextvars import ContextVar
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.core import async_session_factory


session: ContextVar[AsyncSession] = ContextVar("session")


def in_session(*, commit: bool = False):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            async with async_session_factory() as session_:
                session.set(session_)
                response = await func(*args, **kwargs)
                if commit:
                    await session.get().commit()
            return response

        return wrapper

    return decorator
