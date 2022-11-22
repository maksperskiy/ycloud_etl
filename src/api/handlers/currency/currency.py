from typing import List
import requests
from datetime import date
from pydantic import parse_obj_as

from fastapi import status
from src.core.settings import settings
from src.database.repositories import CurrencyRepository
from src.exceptions import NotFoundException, ApplicationException, BadRequestException

from src.schemas.responses.currency.currency import CurrenciesResponse


class CurrencyHandler:
    @classmethod
    async def import_currencies(cls, date_req: date):
        date_req = date_req.strftime("%d/%m/%Y")
        response = requests.get(settings.FUNC_URL, params={"date_req": date_req})
        if response.status_code == status.HTTP_409_CONFLICT:
            raise BadRequestException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Conflict. Currencies for this date alteady exists.",
            )
        if not response:
            raise ApplicationException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="CBR service unavailable.",
            )

    @classmethod
    async def get_currencies(cls, date_req: date) -> CurrenciesResponse:
        result = await CurrencyRepository.get_currencies(date_req)
        if not result:
            raise NotFoundException(detail="Not found currencies for this date.")
        return CurrenciesResponse(data=result)
