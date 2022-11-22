from fastapi import status

from src.exceptions.application import ApplicationException


class AccessDeniedException(ApplicationException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Access denied"
