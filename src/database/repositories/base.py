from src.api.middlewares.database import session


class BaseRepository:
    @classmethod
    async def execute(cls, query, flush: bool = False):
        result = await session.get().execute(query)
        if flush:
            await session.get().flush()
        return result
    