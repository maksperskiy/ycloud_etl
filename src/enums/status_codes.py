from enum import Enum

class StatusCode(Enum, str):
    SUCCESS = 200
    CREATED = 202
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409
    INTERNAL_SERVER_ERROR = 500
