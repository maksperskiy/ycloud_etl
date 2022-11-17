from .base import BaseResponse
from src.enums import StatusCode


class NotFoundResponse(BaseResponse):
    status_code = StatusCode.NOT_FOUND
    detail = "Not found"
    data = None
