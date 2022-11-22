from fastapi import status

from src.exceptions.application import ApplicationException


class BadRequestException(ApplicationException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Bad request"
