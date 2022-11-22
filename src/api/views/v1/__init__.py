from fastapi import APIRouter
from .currency.currency import router as currency_router

router = APIRouter(prefix="/v1")

router.include_router(currency_router)
