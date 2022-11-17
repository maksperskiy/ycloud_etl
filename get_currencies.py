from utils import execute_query, get_date_str, DB_TABLE


def get_currencies(event, context):
    try:
        date_req = get_date_str(event)
    except ValueError:
        return {"statusCode": 400, "body": {"detail": "Bad date param"}}

    records = execute_query(
        f"""
        SELECT * FROM {DB_TABLE} WHERE date_req = '{date_req}'
        """,
        context,
    )

    if not records:
        return {"statusCode": 404, "detail": "Not found currencies for this date"}

    keys = ["id", "numCode", "charCode", "nominal", "name", "value", "dateReq"]

    data = [{keys[i]: record[i] for i in range(0, len(keys), 1)} for record in records]

    return {"statusCode": 200, "body": {"data": data}}
