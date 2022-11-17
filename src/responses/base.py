from typing import Any
from src.enums import StatusCode


class BaseResponse:
    status_code = StatusCode.INTERNAL_SERVER_ERROR
    detail = "Internal server error"
    data = None

    def __init__(self, status_code: int = None, detail: Any = None, data: Any = None):
        super(BaseResponse, self).__init__(
            status_code=status_code or self.status_code, detail=detail or self.detail
        )

    def __call__(self) -> dict:
        return {
            "statusCode": self.status_code,
            "body": {"detail": self.detail, "data": self.data},
        }
