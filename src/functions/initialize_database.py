from src.utils import execute_query, DB_TABLE
from src.utils import create_table_query


def initialize_database_handler(event, context):
    execute_query(
        create_table_query(DB_TABLE),
        context,
        commit=True,
    )

    return {"statusCode": 202, "body": {"detail": "Created"}}
