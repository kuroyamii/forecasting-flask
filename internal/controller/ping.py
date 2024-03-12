from flask import Flask, request, jsonify
import pkg.response.base as response
import internal.controller.forecast as forecast

def ping():
    return response.success_response("pong")
 