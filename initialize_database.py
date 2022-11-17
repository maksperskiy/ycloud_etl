from utils import execute_query, DB_TABLE


def initialize_database(event, context):
    execute_query(
        f"""
    CREATE TABLE IF NOT EXISTS {DB_TABLE} (
        code varchar, 
        num_code int, 
        char_code varchar,
        nominal int,
        name varchar,
        value numeric(10,4),
        date_req date,
        PRIMARY KEY(date_req, code)
    );
    """,
        context,
        commit=True,
    )

    return {"statusCode": 200, "body": {"detail": "success"}}
