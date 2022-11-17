def insert_query(table, values):
    return f"""
    INSERT into {table}
    (code, num_code, char_code, nominal, name, value, date_req) 
    values {values};
    """

def select_query(table, date_req):
    return f"""
    SELECT * FROM {table} WHERE date_req = '{date_req}'
    """

def create_table_query(table):
    return f"""
    CREATE TABLE IF NOT EXISTS {table} (
        code varchar, 
        num_code int, 
        char_code varchar,
        nominal int,
        name varchar,
        value numeric(10,4),
        date_req date,
        PRIMARY KEY(date_req, code)
    );
    """