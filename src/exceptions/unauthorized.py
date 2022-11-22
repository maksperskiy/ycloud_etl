from fastapi import status

from src.exceptions.application import ApplicationException


class UnauthorizedException(ApplicationException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Unauthorized"
