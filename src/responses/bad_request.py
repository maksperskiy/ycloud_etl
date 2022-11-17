from .base import BaseResponse
from src.enums import StatusCode


class BadRequestResponse(BaseResponse):
    status_code = StatusCode.BAD_REQUEST
    detail = "Bad request"
    data = None
