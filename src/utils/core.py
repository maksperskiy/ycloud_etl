import os


CBR_URL = "https://www.cbr.ru/scripts/XML_daily.asp?date_req"
CURRENCIES = ["RUB", "USD", "EUR"]
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
DB_TABLE = os.getenv("DB_TABLE", "\"public\".etl_currencies")

RESPONSE_KEYS = ["id", "numCode", "charCode", "nominal", "name", "value", "dateReq"]
