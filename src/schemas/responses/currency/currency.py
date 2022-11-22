from typing import List
from datetime import date
from src.schemas.responses.base import BaseResponse


class CurrencyResponse(BaseResponse):
    code: str
    num_code: int
    char_code: str
    nominal: int
    name: str
    value: float
    date_req: date


class CurrenciesResponse(BaseResponse):
    data: List[CurrencyResponse]
