from src.utils import execute_query, get_date_str, DB_TABLE, RESPONSE_KEYS, select_query


def get_currencies_handler(event, context):
    try:
        date_req = get_date_str(event)
    except ValueError:
        return {"statusCode": 400, "body": {"detail": "Bad date param"}}

    records = execute_query(
        select_query(DB_TABLE, date_req),
        context,
    )

    if not records:
        return {"statusCode": 404, "detail": "Not found currencies for this date"}

    data = [
        {key: record[i] for i, key in enumerate(RESPONSE_KEYS)} for record in records
    ]

    return {"statusCode": 200, "body": {"data": data}}
