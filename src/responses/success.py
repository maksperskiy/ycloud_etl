from .base import BaseResponse
from src.enums import StatusCode


class SuccessResponse(BaseResponse):
    status_code = StatusCode.SUCCESS
    detail = None
    data = None
