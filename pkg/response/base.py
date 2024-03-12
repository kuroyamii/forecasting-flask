from flask import jsonify, make_response
import http


class BaseResponse:
    def __init__(self, code, message, errors, data):
        self.code = int(code)
        self.message = message
        self.errors = errors
        self.data = data

    def json(self):
        return jsonify({"code": self.code, "message": self.message, "errors": self.errors, "data": self.data})




def success_response(data):
    return make_response(BaseResponse(200, http.HTTPStatus.OK.phrase, None, data).json(), 200)

def error_response(error,code, phrase):
    return make_response(BaseResponse(code, phrase, error, None).json(), code)