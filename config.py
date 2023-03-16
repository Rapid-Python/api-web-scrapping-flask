from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from flask_cors import CORS
from functools import wraps

app = Flask(__name__)

load_dotenv()

CORS(app, resources={
    r"/api/*": {
        "origins": os.getenv('CORS_ORIGINS'),
        "methods": ["GET", "HEAD", "POST", "OPTIONS", "PUT", "DELETE"],
        "max_age": 30
    }})
app.config['CORS_HEADERS'] = 'Content-Type'

# common exception Handler for whole app or all routes function
def get_http_exception_handler(app):
    """Overrides the default http exception handler to return JSON."""
    handle_http_exception = app.handle_http_exception

    @wraps(handle_http_exception)
    def ret_val(exception):
        exc = handle_http_exception(exception)
        return jsonify({'code': exc.code, 'message': exc.description}), exc.code

    return ret_val

# Override the HTTP exception handler.
app.handle_http_exception = get_http_exception_handler(app)

naukri_cookies = os.getenv('NAUKRI_COOKIES')

debug_flag = os.getenv('DEBUG_FLAG')

