from .base import BaseResponse
from src.enums import StatusCode


class ConflictResponse(BaseResponse):
    status_code = StatusCode.CONFLICT
    detail = "Conflict"
    data = None
