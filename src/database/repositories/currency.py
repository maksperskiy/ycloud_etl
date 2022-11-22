from sqlalchemy import select
from datetime import date
from src.database.repositories import BaseRepository
from src.database.models import Currency

class CurrencyRepository(BaseRepository):
    __model__ = Currency

    @classmethod
    async def get_currencies(cls, date_req: date) -> __model__:
        query = select(Currency).filter(Currency.date_req==date_req)
        result = await cls.execute(query)
        return result.scalars().all()
