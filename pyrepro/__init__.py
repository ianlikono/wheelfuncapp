import json
import logging

import azure.functions as func
import psycopg2


def main(req: func.HttpRequest) -> func.HttpResponse:
    """Test function
    """
    logging.info(f"Hello world")
    return func.HttpResponse(json.dumps({'success': 'ok'}), status_code=200)

