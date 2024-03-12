import internal.controller.forecast as forecast
import internal.controller.ping as ping
from flask import Flask
from jsonschema import ValidationError
import pkg.response.base as response
import http

from werkzeug.exceptions import BadRequest

def init_routes(app: Flask):
    app.route("/ping",methods=['GET'])(ping.ping)
    app.route("/forecast",methods=['POST'])(forecast.forecast)

def error_handler(app: Flask):
    @app.errorhandler(400)
    def bad_request(error: BadRequest):
        if isinstance(error.description, ValidationError):
            return response.error_response(error.description.message, http.HTTPStatus.BAD_REQUEST.value, http.HTTPStatus.BAD_REQUEST.phrase)
        return response.error_response("bad request", http.HTTPStatus.BAD_REQUEST.value, http.HTTPStatus.BAD_REQUEST.phrase)
        # if isinstance(error.description, ValidationError):
        #     original_error = error.description
        #     return response.error_response(original_error, 400, http.HTTPStatus.BAD_REQUEST.phrase)
        # return error