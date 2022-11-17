from src.utils import execute_query, DB_TABLE
from src.responses import CreatedResponse
from src.utils import create_table_query


def initialize_database(event, context):
    execute_query(
        create_table_query(DB_TABLE),
        context,
        commit=True,
    )

    return CreatedResponse()
