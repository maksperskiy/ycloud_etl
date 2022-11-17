from src.utils import execute_query, get_date_str, DB_TABLE, RESPONSE_KEYS, select_query
from src.responses import SuccessResponse, BadRequestResponse, NotFoundResponse


def get_currencies(event, context):
    try:
        date_req = get_date_str(event)
    except ValueError:
        return BadRequestResponse(detail="Bad date param")

    records = execute_query(
        select_query(DB_TABLE, date_req),
        context,
    )

    if not records:
        return NotFoundResponse(detail="Not found currencies for this date")

    data = [
        {key: record[i] for i, key in enumerate(RESPONSE_KEYS)} for record in records
    ]

    return SuccessResponse(data=data)
