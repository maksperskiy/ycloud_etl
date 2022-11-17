import requests
import pandas as pd
from src.utils import (
    execute_query,
    get_date_str,
    DB_TABLE,
    CURRENCIES,
    CBR_URL,
    insert_query,
    select_query,
)


def import_currencies_handler(event, context):
    try:
        date_req = get_date_str(event)
    except ValueError:
        return {"statusCode": 400, "body": {"detail": "Bad date param"}}

    records = execute_query(select_query(DB_TABLE, date_req), context)

    if records:
        return {
            "statusCode": 409,
            "body": {"detail": "Conflict. Currencies for this date alteady exists."},
        }
    response = requests.get(CBR_URL, params={"date_req": date_req})
    if not response:
        return {"statusCode": 503, "detail": "Bad request to CBR"}

    df = pd.read_xml(response.content, encoding="ascii")
    df = df[df["CharCode"].isin(CURRENCIES)]
    df["Value"] = pd.to_numeric(df["Value"].str.replace(",", "."), downcast="float")

    insert_values = ",".join(
        [str(tuple(el + [date_req])) for el in df.T.to_dict("list").values()]
    )

    execute_query(insert_query(DB_TABLE, insert_values), context, commit=True)

    return {"statusCode": 200, "body": {"detail": "success"}}
