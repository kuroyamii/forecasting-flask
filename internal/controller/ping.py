from flask import Flask, request, jsonify
import pkg.response.base as response

def ping():
    return response.success_response("pong")


def init_routes(app: Flask):
    app.route("/ping",methods=['GET'])(ping)
    