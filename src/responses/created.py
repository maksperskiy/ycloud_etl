from .base import BaseResponse
from src.enums import StatusCode


class CreatedResponse(BaseResponse):
    status_code = StatusCode.CREATED
    detail = "Created"
    data = None
