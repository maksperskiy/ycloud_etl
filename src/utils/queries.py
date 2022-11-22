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
