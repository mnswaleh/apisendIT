"""Create application"""

from flask import Flask, Blueprint

from app.api.v1 import VERSION1


def create_app():
    """create app"""
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(VERSION1)

    return app
