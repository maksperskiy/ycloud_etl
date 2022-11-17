import psycopg2
from .core import DB_NAME, DB_USER, DB_PORT, DB_HOST, DB_PASSWORD


def execute_query(query: str, context, commit: bool = False):
    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD or context.token["access_token"],
        host=DB_HOST,
        port=DB_PORT,
        sslmode="require",
    )

    result = None
    cur = conn.cursor()
    try:
        cur.execute(query)
        if commit:
            conn.commit()
        result = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        cur.close()
    conn.close()

    return result
