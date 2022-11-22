from datetime import date
from fastapi import APIRouter, Depends, Query, Security, status

from src.api.handlers import CurrencyHandler
from src.api.middlewares.auth import has_access
from src.api.middlewares.database import in_session


from src.schemas.responses.currency.currency import CurrenciesResponse


router = APIRouter(prefix="/currency", tags=["Currencies"])


@router.get("", response_model=CurrenciesResponse)
@in_session()
async def get(
    date_req: date = Query(date.today()),
    handler: CurrencyHandler = Depends(),
    _=Security(has_access),
):
    return await handler.get_currencies(date_req)


@router.get("/import", status_code=status.HTTP_201_CREATED)
async def get(
    date_req: date = Query(date.today()),
    handler: CurrencyHandler = Depends(),
    _=Security(has_access),
):
    return await handler.import_currencies(date_req)
