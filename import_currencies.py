import requests
import pandas as pd
from utils import execute_query, get_date_str, DB_TABLE, CURRENCIES


def import_currencies(event, context):
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

    if records:
        return {
            "statusCode": 409,
            "body": {"detail": "Conflict. Currencies for this date alteady exists."},
        }
    response = requests.get(
        f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={date_req}"
    )
    if not response:
        return {"statusCode": 503, "detail": "Bad request to CBR"}

    df = pd.read_xml(response.content, encoding="ascii")
    df = df[df["CharCode"].isin(CURRENCIES)]
    df["Value"] = pd.to_numeric(df["Value"].str.replace(",", "."), downcast="float")

    insert_values = ",".join(
        [str(tuple(el + [date_req])) for el in df.T.to_dict("list").values()]
    )
    query = f"""
    INSERT into {DB_TABLE}
    (code, num_code, char_code, nominal, name, value, date_req) 
    values {insert_values};
    """
    execute_query(query, context, commit=True)

    return {"statusCode": 200, "body": {"detail": "success"}}
