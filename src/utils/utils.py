from datetime import date, datetime


def get_date_str(event):
    query_params = event.get("queryStringParameters", None) if event else None
    date_req = None
    if query_params:
        date_req = query_params.get("date_req", None)
        if datetime.strptime(date_req, "%d/%m/%Y") > datetime.today():
            raise ValueError
    if not date_req:
        date_req = date.today().strftime("%d/%m/%Y")
    return date_req

def to_camel_case(snake_case_string: str) -> str:
    string = snake_case_string.replace("_", " ").title().replace(" ", "")
    return string[0].lower() + string[1:]
