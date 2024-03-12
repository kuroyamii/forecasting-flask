from flask import Flask
import internal.controller.controller as controller


def initialize_routes(app: Flask):
    controller.init_routes(app)
    controller.error_handler(app)
