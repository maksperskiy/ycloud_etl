from src.functions import get_currencies, initialize_database, import_currencies

def invoke_get_currencies(event, context):
    get_currencies(event, context)

def invoke_import_currencies(event, context):
    import_currencies(event, context)

def invoke_initialize_database(event, context):
    initialize_database(event, context)
